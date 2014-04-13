Djangobench
===========

A harness and a set of benchmarks for measuring Django's performance over
time.

Running the benchmarks
----------------------

Here's the short version::

    mkvirtualenv djangobench
    pip install -e git://github.com/django/djangobench.git#egg=djangobench
    git clone git://github.com/django/django.git
    cd django
    djangobench --control=1.2 --experiment=master

Okay, so what the heck's going on here?

First, ``djangobench`` doesn't test a single Django version in isolation --
that wouldn't be very useful. Instead, it benchmarks an "experiment" Django
against a "control", reporting on the difference between the two and
measuring for statistical significance.

Because a Git clone can contain all the project development history, you can
test against a single repository specifying individual commit IDs, tag (as we've
done above) and even possibly branches names with the ``--control`` and
``--experiment`` options.

Before ``djangobench`` 0.10 you had to use ``--vcs=git`` to get this behavior.
Now it's the default. There is also support for Mercurial (``--vcs=hg``).

Another way to use ``djangobench``, is to run it against two complete Django
source trees, you can specify this mode by using ``--vcs=none``. By default it
looks for directories named ``django-control`` and ``django-experiment`` in the
current working directory::

    djangobench --vcs=none

but you can change that by using the ``--control`` or ``--experiment`` options::

    djangobench --vcs=none --control pristine --experiment work

Now, it's impractical to install the Django source code trees under test (this
is particularly true in the two-trees scenario): ``djangobench`` works its magic
by mucking with ``PYTHONPATH``.

However, the benchmarks themselves need access to the ``djangobench`` module, so
you'll need to install it.

You can specify the benchmarks to run by passing their names on the command
line.

This is an example of not-statistically-significant results::

    Running 'startup' benchmark ...
    Min: 0.138701 -> 0.138900: 1.0014x slower
    Avg: 0.139009 -> 0.139378: 1.0027x slower
    Not significant
    Stddev: 0.00044 -> 0.00046: 1.0382x larger

Python 3
~~~~~~~~

Not only is ``djangobench`` Python 3 compatible, but can also be used to
compare Python 2 vs Python 3 code paths. To do this, you need to provide the
full paths to the corresponding Python executables in ``--control-python`` and
``--experiment-python``. The short version (assuming you have also the
``djangobench`` environment setup like above)::

    mkvirtualenv djangobench-py3 -p python3
    pip install -e git://github.com/django/djangobench.git#egg=djangobench
    cd django
    djangobench --vcs=none --control=. --experiment=. \
        --control-python=~/.virtualenvs/djangobench/bin/python \
        --experiment-python=~/.virtualenvs/djangobench-py3/bin/python \

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

**Please write new benchmarks and send us pull requests on Github!**
