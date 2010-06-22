#!/usr/bin/env python

"""
Run us some Django benchmarks.
"""

import sys
import argparse
from unipath import DIRS, FSPath as Path
from djangobench import perf

BENCMARK_DIR = Path(__file__).parent.child('benchmarks').absolute()

def run_benchmarks(control, experiment, benchmarks, trials, dump_times=False, benchmark_dir=BENCMARK_DIR):
    if benchmarks:
        print "Running benchmarks: %s" % " ".join(benchmarks)
    else:
        print "Running all benchmarks"

    control_label = get_django_version(control)
    experiment_label = get_django_version(experiment)
    print "Control: Django %s (in %s)" % (control_label, control)
    print "Experiment: Django %s (in %s)" % (experiment_label, experiment)
    print

    # Calculate the subshell envs that we'll use to execute the
    # benchmarks in.
    control_env = {'PYTHONPATH': ':'.join([
        Path(control).absolute(),
        Path(benchmark_dir),
    ])}
    experiment_env = {'PYTHONPATH': ':'.join([
        Path(experiment).absolute(), 
        Path(benchmark_dir),
    ])}

    for benchmark in discover_benchmarks(benchmark_dir):
        if not benchmarks or benchmark.name in benchmarks:
            print "Running '%s' benchmark ..." % benchmark.name
            settings_mod = '%s.settings' % benchmark.name
            control_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            experiment_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            
            try:
                control_data = run_benchmark(benchmark, trials, control_env, dump_times)
                experiment_data = run_benchmark(benchmark, trials, experiment_env, dump_times)
            except SkipBenchmark, reason:
                print "Skipped: %s\n" % reason
                continue

            options = argparse.Namespace(
                track_memory = False,
                diff_instrumentation = False,
                benchmark_name = benchmark.name,
                disable_timelines = True,
                control_label = control_label,
                experiment_label = experiment_label,
            )
            result = perf.CompareBenchmarkData(control_data, experiment_data, options)
            print format_benchmark_result(result, len(control_data.runtimes))
            print

def discover_benchmarks(benchmark_dir):
    for app in Path(benchmark_dir).listdir(filter=DIRS):
        if app.child('benchmark.py').exists() and app.child('settings.py').exists():
            yield app

class SkipBenchmark(Exception):
    pass

def run_benchmark(benchmark, trials, env, dump_times=False):
    """
    Similar to perf.MeasureGeneric, but modified a bit for our purposes.
    """
    # Remove Pycs, then call the command once to prime the pump and
    # re-generate fresh ones This makes sure we're measuring as little of
    # Python's startup time as possible.
    perf.RemovePycs()
    command = [sys.executable, '%s/benchmark.py' % benchmark]
    out, _, _ = perf.CallAndCaptureOutput(command, env, track_memory=False, inherit_env=[])
    if out.startswith('SKIP:'):
        raise SkipBenchmark(out.replace('SKIP:', '').strip())

    # Now do the actual mesurements.
    data_points = []
    for i in range(trials):
        output = perf.CallAndCaptureOutput(command, env, track_memory=False, inherit_env=[])
        stdout, stderr, mem_usage = output
        if dump_times: print stdout
        data_points.extend(float(line) for line in stdout.splitlines())
    return perf.RawData(data_points, mem_usage, inst_output=stderr)

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

def get_django_version(djangodir):
    out, err, _ = perf.CallAndCaptureOutput(
        [sys.executable, '-c' 'import django; print django.get_version()'],
        env = {'PYTHONPATH': Path(djangodir).absolute()}
    )
    return out.strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--control',
        default = 'django-control',
        help = "Path to the Django code tree to use as control."
    )
    parser.add_argument(
        '--experiment',
        default = 'django-experiment',
        help = "Path to the Django version to use as experiment."
    )
    parser.add_argument(
        '-t', '--trials',
        type = int,
        default = 5,
        help = 'Number of times to run each benchmark.'
    )
    parser.add_argument(
        '--dump-times',
        dest = 'dump_times',
        action = 'store_true',
        default = False,
        help = 'Dump raw times to stdout. Careful - prints a *lot* of data!',
    )
    parser.add_argument(
        'benchmarks',
        metavar = 'name',
        default = None,
        help = "Benchmarks to be run.  Defaults to all.",
        nargs = '*'
    )
    args = parser.parse_args()
    run_benchmarks(args.control, args.experiment, args.benchmarks, args.trials, args.dump_times)

if __name__ == '__main__':
    main()
