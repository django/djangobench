#!/usr/bin/env python

"""
Run us some Django benchmarks.
"""

import subprocess
import argparse
import email
import simplejson
import sys
from djangobench import perf
from unipath import DIRS, FSPath as Path

__version__ = '0.10'

DEFAULT_BENCHMARK_DIR = Path(__file__).parent.child('benchmarks').absolute()

def run_benchmarks(control, experiment, benchmark_dir, benchmarks, trials, vcs=None, record_dir=None, profile_dir=None, continue_on_error=False):
    if benchmarks:
        print "Running benchmarks: %s" % " ".join(benchmarks)
    else:
        print "Running all benchmarks"

    if record_dir:
        record_dir = Path(record_dir).expand().absolute()
        if not record_dir.exists():
            raise ValueError('Recording directory "%s" does not exist' % record_dir)
        print "Recording data to '%s'" % record_dir

    control_label = get_django_version(control, vcs=vcs)
    experiment_label = get_django_version(experiment, vcs=vcs)
    branch_info = "%s branch " % vcs if vcs else ""
    print "Control: Django %s (in %s%s)" % (control_label, branch_info, control)
    print "Experiment: Django %s (in %s%s)" % (experiment_label, branch_info, experiment)
    print

    # Calculate the subshell envs that we'll use to execute the
    # benchmarks in.
    if vcs:
        control_env = {
            'PYTHONPATH': '%s:%s' % (Path.cwd().absolute(), Path(benchmark_dir)),
        }
        experiment_env = control_env.copy()
    else:
        control_env = {'PYTHONPATH': '%s:%s' % (Path(control).absolute(), Path(benchmark_dir))}
        experiment_env = {'PYTHONPATH': '%s:%s' % (Path(experiment).absolute(), Path(benchmark_dir))}

    for benchmark in discover_benchmarks(benchmark_dir):
        if not benchmarks or benchmark.name in benchmarks:
            print "Running '%s' benchmark ..." % benchmark.name
            settings_mod = '%s.settings' % benchmark.name
            control_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            experiment_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            if profile_dir is not None:
                control_env['DJANGOBENCH_PROFILE_FILE'] = Path(profile_dir, "con-%s" % benchmark.name)
                experiment_env['DJANGOBENCH_PROFILE_FILE'] = Path(profile_dir, "exp-%s" % benchmark.name)
            try:
                if vcs: switch_to_branch(vcs, control)
                control_data = run_benchmark(benchmark, trials, control_env)
                if vcs: switch_to_branch(vcs, experiment)
                experiment_data = run_benchmark(benchmark, trials, experiment_env)
            except SkipBenchmark, reason:
                print "Skipped: %s\n" % reason
                continue
            except RuntimeError, error:
                if continue_on_error:
                    print "Failed: %s\n" % error
                    continue
                raise

            options = argparse.Namespace(
                track_memory = False,
                diff_instrumentation = False,
                benchmark_name = benchmark.name,
                disable_timelines = True,
                control_label = control_label,
                experiment_label = experiment_label,
            )
            result = perf.CompareBenchmarkData(control_data, experiment_data, options)
            if record_dir:
                record_benchmark_results(
                    dest = record_dir.child('%s.json' % benchmark.name),
                    name = benchmark.name,
                    result = result,
                    control = control_label,
                    experiment = experiment_label,
                    control_data = control_data,
                    experiment_data = experiment_data,
                )
            print format_benchmark_result(result, len(control_data.runtimes))
            print

def discover_benchmarks(benchmark_dir):
    for app in Path(benchmark_dir).listdir(filter=DIRS):
        if app.child('benchmark.py').exists() and app.child('settings.py').exists():
            yield app

class SkipBenchmark(Exception):
    pass

def run_benchmark(benchmark, trials, env):
    """
    Similar to perf.MeasureGeneric, but modified a bit for our purposes.
    """
    # Remove Pycs, then call the command once to prime the pump and
    # re-generate fresh ones. This makes sure we're measuring as little of
    # Python's startup time as possible.
    RemovePycs()
    command = [sys.executable, '%s/benchmark.py' % benchmark]
    out, _, _ = perf.CallAndCaptureOutput(command + ['-t', 1], env, track_memory=False, inherit_env=[])
    if out.startswith('SKIP:'):
        raise SkipBenchmark(out.replace('SKIP:', '').strip())

    # Now do the actual mesurements.
    output = perf.CallAndCaptureOutput(command + ['-t', str(trials)], env, track_memory=False, inherit_env=[])
    stdout, stderr, mem_usage = output
    message = email.message_from_string(stdout)
    data_points = [float(line) for line in message.get_payload().splitlines()]
    return perf.RawData(data_points, mem_usage, inst_output=stderr)

def record_benchmark_results(dest, **kwargs):
    kwargs['version'] = __version__
    simplejson.dump(kwargs, open(dest, 'w'), default=json_encode_custom)

def json_encode_custom(obj):
    if isinstance(obj, perf.RawData):
        return obj.runtimes
    if isinstance(obj, perf.BenchmarkResult):
        return {
            'min_base'    : obj.min_base,
            'min_changed' : obj.min_changed,
            'delta_min'   : obj.delta_min,
            'avg_base'    : obj.avg_base,
            'avg_changed' : obj.avg_changed,
            'delta_avg'   : obj.delta_avg,
            't_msg'       : obj.t_msg,
            'std_base'    : obj.std_base,
            'std_changed' : obj.std_changed,
            'delta_std'   : obj.delta_std,
        }
    if isinstance(obj, perf.SimpleBenchmarkResult):
        return {
            'base_time'    : obj.base_time,
            'changed_time' : obj.changed_time,
            'time_delta'   : obj.time_delta,
        }
    raise TypeError("%r is not JSON serializable" % obj)

def supports_color():
    return sys.platform != 'win32' and hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

class colorize(object):
    GOOD = INSIGNIFICANT = SIGNIFICANT = BAD = ENDC = ''
    if supports_color():
        GOOD = '\033[92m'
        INSIGNIFICANT = '\033[94m'
        SIGNIFICANT = '\033[93m'
        BAD = '\033[91m'
        ENDC = '\033[0m'

    @classmethod
    def colorize(cls, color, text):
        return "%s%s%s" % (color, text, cls.ENDC)

    @classmethod
    def good(cls, text):
        return cls.colorize(cls.GOOD, text)

    @classmethod
    def significant(cls, text):
        return cls.colorize(cls.SIGNIFICANT, text)

    @classmethod
    def insignificant(cls, text):
        return cls.colorize(cls.INSIGNIFICANT, text)

    @classmethod
    def bad(cls, text):
        return cls.colorize(cls.BAD, text)

def format_benchmark_result(result, num_points):
    if isinstance(result, perf.BenchmarkResult):
        output = ''
        delta_min = result.delta_min
        if 'faster' in delta_min:
            delta_min = colorize.good(delta_min)
        elif 'slower' in result.delta_min:
            delta_min = colorize.bad(delta_min)
        output += "Min: %f -> %f: %s\n" % (result.min_base, result.min_changed, delta_min)

        delta_avg = result.delta_avg
        if 'faster' in delta_avg:
            delta_avg = colorize.good(delta_avg)
        elif 'slower' in delta_avg:
            delta_avg = colorize.bad(delta_avg)
        output += "Avg: %f -> %f: %s\n" % (result.avg_base, result.avg_changed, delta_avg)

        t_msg = result.t_msg
        if 'Not significant' in t_msg:
            t_msg = colorize.insignificant(t_msg)
        elif 'Significant' in result.t_msg:
            t_msg = colorize.significant(t_msg)
        output += t_msg

        delta_std = result.delta_std
        if 'larger' in delta_std:
            delta_std = colorize.bad(delta_std)
        elif 'smaller' in delta_std:
            delta_std = colorize.good(delta_std)
        output += "Stddev: %.5f -> %.5f: %s" %(result.std_base, result.std_changed, delta_std)
        output += " (N = %s)" % num_points
        output += result.get_timeline()
        return output
    else:
        return str(result)

def get_django_version(loc, vcs=None):
    if vcs:
        switch_to_branch(vcs, loc, do_cleanup=True)
        pythonpath = Path.cwd()
    else:
        pythonpath = Path(loc).absolute()
    out, err, _ = perf.CallAndCaptureOutput(
        [sys.executable, '-c' 'import django; print django.get_version()'],
        env = {'PYTHONPATH': pythonpath}
    )
    return out.strip()

def switch_to_branch(vcs, branchname, do_cleanup=False):
    if vcs == 'git':
        cmd = ['git', 'checkout', branchname]
    elif vcs == 'hg':
        cmd = ['hg', 'update', '-C', branchname]
    else:
        raise ValueError("Sorry, %s isn't supported (yet?)" % vcs)
    if do_cleanup:
        RemovePycs(vcs=vcs)
    subprocess.check_call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def RemovePycs(vcs=None):
    if vcs == 'git':
        cmd = ['git', 'clean', '-fdX']
        subprocess.check_call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        perf.RemovePycs()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--control',
        metavar = 'PATH',
        default = 'django-control',
        help = "Path to the Django code tree to use as control."
    )
    parser.add_argument(
        '--experiment',
        metavar = 'PATH',
        default = 'django-experiment',
        help = "Path to the Django version to use as experiment."
    )
    parser.add_argument(
        '--vcs',
        choices = ['git', 'hg', 'none'],
        default = 'git',
        help = 'Use a VCS for control/experiment. Makes --control/--experiment specify branches, not paths.'
    )
    parser.add_argument(
        '-t', '--trials',
        type = int,
        default = 50,
        help = 'Number of times to run each benchmark.'
    )
    parser.add_argument(
        '-r', '--record',
        default = None,
        metavar = 'PATH',
        help = 'Directory to record detailed output as a series of JSON files.',
    )

    parser.add_argument(
        '--benchmark-dir',
        dest = 'benchmark_dir',
        metavar = 'PATH',
        default = DEFAULT_BENCHMARK_DIR,
        help = ('Directory to inspect for benchmarks. Defaults to the '
                'benchmarks included with djangobench.'),
    )
    parser.add_argument(
        'benchmarks',
        metavar = 'name',
        default = None,
        help = "Benchmarks to be run.  Defaults to all.",
        nargs = '*'
    )
    parser.add_argument(
        '-p',
        '--profile-dir',
        dest = 'profile_dir',
        default = None,
        metavar = 'PATH',
        help = 'Directory to record profiling statistics for the control and experimental run of each benchmark'
    )
    parser.add_argument(
        '--continue-on-error',
        dest = 'continue_on_error',
        action = 'store_true',
        help = 'Continue with the remaining benchmarks if any fail',
    )

    args = parser.parse_args()
    run_benchmarks(
        control = args.control,
        experiment = args.experiment,
        benchmark_dir = args.benchmark_dir,
        benchmarks = args.benchmarks,
        trials = args.trials,
        vcs = None if args.vcs == 'none' else args.vcs,
        record_dir = args.record,
        profile_dir = args.profile_dir,
        continue_on_error = args.continue_on_error
    )

if __name__ == '__main__':
    main()
