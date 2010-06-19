Djangobench
===========

This is a harness for a (to-be-written) set of benchmarks for measuring
Django's performance over time.

Running the benchmarks
----------------------

This doesn't test a single Django version in isolation -- that wouldn't be
very useful. Instead, it benchmarks an "experiment" Django against a
"control", reporting on the difference between the two and measuring for
statistical significance.

So to run this, you'll need two complete Django source trees. By default
``djangobench.py`` looks for directories named ``django-control`` and
``django-experiment`` here in this directory, but you can change that
by using the ``--control`` or ``--experiment`` options.

So, for example, to benchmark Django 1.2 against trunk::

    svn co http://code.djangoproject.com/svn/django/tags/releases/1.2/ django-control
    svn co http://code.djangoproject.com/svn/django/trunk django-experiment
    ./djangobench
    
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
file, and an executable ``benchmarks.py`` that gets run by the harness.
This file should print timing data to stdout.

See the ``startup`` directory benchmark for an example.

Please write new benchmarks and send me pull requests on Github!

TODO
----

* Right now each benchmark gets run multiple times by the harness,
  incurring startup overhead. The startup benchmark shows this is a non-trivial amount of time,
  so there really needs to be a way for individual benchmarks to run n-trials in-process
  to avoid that overhead and warmup time. Unladen's ``perf.py`` supports this; the harness
  code needs to, also.
  
* The number of trials is hard-coded. This should be an --option, or,
  better yet, it could be automatically determined by running trials
  until the results reach a particular confidence internal or some large
  ceiling is hit.
  
* Lots and lots and lots more benchmarks. Some ideas:

    * template rendering (something useful, not the unladen one)
    * ORM queries
    * ORM overhead compared to cursor.execute()
    * signal/dispatch
    * datastructures (specifically MultiDict)
    * url resolving and reversing
    * form/model validation
    * holistic request/response round-trip time
    * middleware (piecemeal and standard "stacks" together)