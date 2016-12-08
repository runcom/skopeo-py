#!/usr/bin/env python
from setuptools import setup, find_packages

with open('./requirements.txt') as reqs_txt:
    requirements = [line for line in reqs_txt]

def readme():
    with open('README.rst') as f:
        return f.read()

version = None
exec(open('skopeo/version.py').read())

setup(name='skopeo',
        version=version,
        description='Python wrapper for the skopeo CLI',
        long_description=readme(),
        url='https://github.com/runcom/skopeo-py',
        maintainer='Antonio Murdaca',
        maintainer_email='runcom@linux.com',
        keywords='',
        packages=find_packages(exclude=["tests.*", "tests"]),
        test_suite='tests',
        install_requires=requirements,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: Apache Software License',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Utilities',
            ],
        zip_safe=False)
