#!/usr/bin/env python

"""
Run us some Django benchmarks.
"""

import os
import subprocess
import sys
import tempfile

import argparse
from unipath import DIRS, FSPath as Path

import perf


BENCMARK_DIR = Path(__file__).parent.child('benchmarks')

def main(control, experiment, benchmarks, benchmark_dir=BENCMARK_DIR):
    if benchmarks:
        print "Running benchmarks: %s" % " ".join(benchmarks)
    else:
        print "Running all benchmarks"
    print "Control: Django %s (in %s)" % (get_django_version(control), control)
    print "Experiment: Django %s (in %s)" % (get_django_version(experiment), experiment)
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
    
    # TODO: make this configurable, or, better, make it an option
    # to run until results are significant or some ceiling is hit.
    trials = 5
    
    results = []

    for benchmark in discover_benchmarks(benchmark_dir):
        if not benchmarks or benchmark.name in benchmarks:
            print "Running '%s' benchmark ..." % benchmark.name
            settings_mod = '%s.settings' % benchmark.name
            control_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            experiment_env['DJANGO_SETTINGS_MODULE'] = settings_mod
            
            control_data = perf.MeasureCommand(
                [sys.executable, '%s/benchmark.py' % benchmark],
                iterations = trials,
                env = control_env,
                track_memory = False,
            )
            
            experiment_data = perf.MeasureCommand(
                [sys.executable, '%s/benchmark.py' % benchmark],
                iterations = trials,
                env = experiment_env,
                track_memory = False,
            )
            
            options = argparse.Namespace(
                track_memory = False, 
                diff_instrumentation = False,
                benchmark_name = benchmark.name,
                disable_timelines = True
            )
            result = perf.CompareBenchmarkData(control_data, experiment_data, options)
            print result
            print
    
def discover_benchmarks(benchmark_dir):
    for app in Path(benchmark_dir).listdir(filter=DIRS):
        if app.child('benchmark.py').exists() and app.child('settings.py').exists():
            yield app

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
        'benchmarks',
        metavar = 'name',
        default = None,
        help = "Benchmarks to be run.  Defaults to all.",
        nargs = '*'
    )
    args = parser.parse_args()
    main(args.control, args.experiment, args.benchmarks)
