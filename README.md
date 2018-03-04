 Github Action Bot
==================

Github bot that interacts with repository webhooks pointing to it. You just need to activate webhooks in your repository
(or organization) and create a custom hook handler in the code to interact with Github or any other service

Main example provided in this code, reads comments from the original repository Pull Requests and looks for the bot 
invocation with a ``@boot do-something`` like command and performs corresponding actions.


This project also provides a best-practices template Python project which integrates several different tools.
It saves you work by setting up a number of things, including documentation, code checking, and unit test runners.

Tools included and used:

* [Paver](http://paver.github.io/paver/) for running miscellaneous tasks
* [Setuptools](http://pythonhosted.org/setuptools/merge.html) for distribution
* [Sphinx](http://sphinx-doc.org/) for documentation
* [flake8](https://pypi.python.org/pypi/flake8) for source code checking
* [pytest](http://pytest.org/latest/) for unit testing
* [mock](http://www.voidspace.org.uk/python/mock/) for mocking (not required by the template, but included anyway)
* [tox](http://testrun.org/tox/latest/) for testing on multiple Python versions



Project Setup
=============

1. Clone this repo
2. (Recommended) Create a venv for this project
3. Install dependencies with `` pip install -r requirements.txt`` and the development dependencies with 
`` pip install -r requirements-dev.txt`` if you need to develop or test the project

Instructions
------------

If you're testing or developing this project on your own computer, please follow the instructions provided by
GitHub to install a custom webhook forwarder from Internet to your local machine (default port is also ``4567``)

[Github Tutorial](https://developer.github.com/webhooks/configuring/)

After the forwarder setup, run the application with
``python ``
After the server hosting this bot app is ready to receive Github Webhooks, please

Using Paver
-----------

The ``pavement.py`` file comes with a number of tasks already set up for you. You can see a full list by typing ``paver help`` in the project root directory. The following are included::

    Tasks from pavement:
    lint             - Perform PEP8 style check, run PyFlakes, and run McCabe complexity metrics on the code.
    doc_open         - Build the HTML docs and open them in a web browser.
    coverage         - Run tests and show test coverage report.
    doc_watch        - Watch for changes in the Sphinx documentation and rebuild when changed.
    test             - Run the unit tests.
    get_tasks        - Get all paver-defined tasks.
    commit           - Commit only if all the tests pass.
    test_all         - Perform a style check and run all unit tests.

For example, to run the both the unit tests and lint, run the following in the project root directory::

    paver test_all

To build the HTML documentation, then open it in a web browser::

    paver doc_open


Supported Python Versions
=========================

Github Bot PR project supports the following versions out of the box:

* CPython 2.6, 2.7, 3.3
* PyPy 1.9


Authors
=======

* Carlos Escura
