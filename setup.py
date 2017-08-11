import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="djangobench",
    version="0.10",
    description="A harness and a set of benchmarks for measuring Django's performance over time.",
    long_description=read('README.rst'),
    url='https://github.com/django/djangobench',
    license='BSD',
    author='Jacob Kaplan-Moss',
    author_email='jacob@jacobian.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Benchmark'
    ],
    entry_points={
        'console_scripts': ['djangobench=djangobench.main:main']
    }
)
