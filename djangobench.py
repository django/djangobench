#!/usr/bin/env python

"""
Run us some Django benchmarks.
"""

import os
import subprocess
import sys
import tempfile
import urllib

import argparse
from unipath import DIRS, FSPath as Path

import perf

BENCMARK_DIR = Path(__file__).parent.child('benchmarks')

def main(control, experiment, benchmarks, trials, benchmark_dir=BENCMARK_DIR):
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
    control_env = {
        'PYTHONPATH': ":".join([
            Path(benchmark_dir).absolute(),
            Path(control).parent.absolute(),
            Path(__file__).parent
        ]),
    }
    experiment_env = {
        'PYTHONPATH': ":".join([
            Path(benchmark_dir).absolute(),
            Path(experiment).parent.absolute(),
            Path(__file__).parent
        ]),
    }
    
    results = []

    for benchmark in discover_benchmarks(benchmark_dir):
        if not benchmarks or benchmark.name in benchmarks:
            print "Running '%s' benchmark ..." % benchmark.name
            settings_mod = '%s.settings' % benchmark.name
            control_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            experiment_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            
            control_data = run_benchmark(benchmark, trials, control_env)
            experiment_data = run_benchmark(benchmark, trials, experiment_env)
            
            options = argparse.Namespace(
                track_memory = False, 
                diff_instrumentation = False,
                benchmark_name = benchmark.name,
                disable_timelines = True,
                control_label = control_label,
                experiment_label = experiment_label,
            )
            result = perf.CompareBenchmarkData(control_data, experiment_data, options)
            print result
            print
    
def discover_benchmarks(benchmark_dir):
    for app in Path(benchmark_dir).listdir(filter=DIRS):
        if app.child('benchmark.py').exists() and app.child('settings.py').exists():
            yield app

def run_benchmark(benchmark, trials, env):
    """
    Similar to perf.MeasureGeneric, but modified a bit for our purposes.
    """
    perf.RemovePycs()
    command = [sys.executable, '%s/benchmark.py' % benchmark]
    times = []
    for i in range(trials):
        output = perf.CallAndCaptureOutput(command, env, track_memory=False, inherit_env=[])
        stdout, stderr, mem_usage = output
        times.extend(float(line) for line in stdout.splitlines())
    return perf.RawData(times, mem_usage, inst_output=stderr)

def get_django_version(djangodir):
    out, err, _ = perf.CallAndCaptureOutput(
        [sys.executable, '-c' 'import django; print django.get_version()'],
        env = {'PYTHONPATH': Path(djangodir).parent.absolute()}
    )
    return out.strip()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--control',
        default = 'django-control/django',
        help = "Path to the Django code tree to use as control."
    )
    parser.add_argument(
        '--experiment',
        default = 'django-experiment/django',
        help = "Path to the Django version to use as experiment."
    )
    parser.add_argument(
        '-t', '--trials',
        type = int,
        default = 50,
        help = 'Number of times to run each benchmark.'
    )
    parser.add_argument(
        'benchmarks',
        metavar = 'name',
        default = None,
        help = "Benchmarks to be run.  Defaults to all.",
        nargs = '*'
    )
    args = parser.parse_args()
    main(args.control, args.experiment, args.benchmarks, args.trials)
