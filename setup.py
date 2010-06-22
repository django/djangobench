import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "djangobench",
    version = "0.9",
    description = "A harness and a set of benchmarks for measuring Django's performance over time.",
    long_description = read('README.rst'),
    url = 'http://github.com/jacobian/djangobench',
    license = 'BSD',
    author = 'Jacob Kaplan-Moss',
    author_email = 'jacob@jacobian.org',
    packages = find_packages(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Benchmark'
    ],
    install_requires = ['argparse==1.1', 'Unipath==0.2.1'],
        
    entry_points = {
        'console_scripts': ['djangobench = djangobench.main:main']
    }
)