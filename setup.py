"""libtmux lives at <https://github.com/tony/libtmux>.

libtmux
-------

Manage tmux workspaces from JSON and YAML, pythonic API, shell completion.

"""
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

about = {}
with open("libtmux/__about__.py") as fp:
    exec(fp.read(), about)

with open('requirements/test.txt') as f:
    tests_reqs = [line for line in f.read().split('\n') if line]

if sys.version_info[0] > 2:
    readme = open('README.rst', encoding='utf-8').read()
else:
    readme = open('README.rst').read()

history = open('CHANGES').read().replace('.. :changelog:', '')


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name=about['__title__'],
    version=about['__version__'],
    url='http://github.com/tony/libtmux/',
    download_url='https://pypi.python.org/pypi/libtmux',
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__email__'],
    description=about['__description__'],
    long_description=readme,
    packages=['libtmux'],
    include_package_data=True,
    tests_require=tests_reqs,
    cmdclass={'test': PyTest},
    zip_safe=False,
    keywords=about['__title__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Topic :: Utilities",
        "Topic :: System :: Shells",
    ],
)
