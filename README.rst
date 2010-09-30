Djangobench
===========

A harness and a set of benchmarks for measuring Django's performance over
time.

Running the benchmarks
----------------------

Here's the short version::

    mkvirtualenv --no-site-packages djangobench
    pip install -e git://github.com/jacobian/djangobench.git#egg=djangobench
    svn co http://code.djangoproject.com/svn/django/tags/releases/1.2/ django-control
    svn co http://code.djangoproject.com/svn/django/trunk django-experiment
    djangobench
    
Okay, so what the heck's going on here?

First, ``djangobench`` doesn't test a single Django version in isolation --
that wouldn't be very useful. Instead, it benchmarks an "experiment" Django
against a "control", reporting on the difference between the two and
measuring for statistical significance.

So to run this, you'll need two complete Django source trees. By default
``djangobench`` looks for directories named ``django-control`` and
``django-experiment`` in the current working directory, but you can change
that by using the ``--control`` or ``--experiment`` options.

Now, because you need two Django source trees, you can't exactly install
them: ``djangobench`` works its magic by mucking with ``PYTHONPATH``.
However, the benchmarks themselves need access to the ``djangobench``
module, so you'll need to install it.

If you're feeling fancy, you can use one of them there newfangled DVCSes instead
and test against a single repository containing branches::

    git clone git@github.com:django/django.git
    djangobench --vcs=git --control=1.2 --experiment=trunk
    
Git's the only supported VCS right now, but patches are welcome.

At the time of this writing Django's trunk hasn't significantly diverged
from Django 1.2, so you should expect to see not-statistically-significant
results::

    Running 'startup' benchmark ...
    Min: 0.138701 -> 0.138900: 1.0014x slower
    Avg: 0.139009 -> 0.139378: 1.0027x slower
    Not significant
    Stddev: 0.00044 -> 0.00046: 1.0382x larger
    
Writing new benchmarks
----------------------

Benchmarks are very simple: they're a Django app, along with a settings
file, and an executable ``benchmarks.py`` that gets run by the harness. The
benchmark script needs to honor a simple contract:

    * It's an executable Python script, run as ``__main__`` (e.g. ``python
      path/to/benchmark.py``). The subshell environment will have
      ``PYTHONPATH`` set up to point to the correct Django; it'll also have
      ``DJANGO_SETTINGS_MODULE`` set to ``<benchmark_dir>.settings``.
      
    * The benchmark script needs to accept a ``--trials`` argument giving
      the number of trials to run.
      
    * The output should be simple RFC 822-ish text -- a set of headers,
      followed by data points::
      
            Title: some benchmark
            Description: whatever the benchmark does
        
            1.002
            1.003
            ...
        
      The list of headers is TBD.

There's a couple of utility functions in ``djangobench.utils`` that assist
with honoring this contract; see those functions' docstrings for details.

The existing benchmarks should be pretty easy to read for inspiration. The
``query_delete`` benchmark is probably a good place to start.

**Please write new benchmarks and send me pull requests on Github!**