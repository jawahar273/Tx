.. highlight:: shell

============
Installation
============


Stable release
--------------

.. To install Tx, run this command in your terminal:

.. .. code-block:: console

..     $ pip install Tx

This is the preferred method to install Tx, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for Tx can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/jawahar273/Tx

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/jawahar273/Tx/tarball/master

.. Once you have a copy of the source, you can install it with:

.. .. code-block:: console

..    $ python setup.py install 


.. _Github repo: https://github.com/jawahar273/Tx
.. _tarball: https://github.com/jawahar273/Tx/tarball/master


Pipenv
------

Pipenv automatically create and manages the dependency using ``pip``, ``virtualenv`` and adding/removing
the packages using ``Pipfile`` and ``Pipfile.lock``. One of the main object is remove the
dependency on ``requirement.txt`` file.

.. code-block:: bash

    pip install --user pipenv


The ``requirements/*.txt`` is compartable with Pipenv for recurrent installing of packages.

.. code-block:: bash

    # step: 1 (for development/production)
    pipenv install -r requirements/base.txt
    # setp: 2 (for development only)
    pipenv install -r requirements/local.txt --dev
    # setp: 3 (only if you are need CLI)
    pipenv install -r requirements/CLI.txt
    # setp: 3 (only if you need Sanic)
    pipenv install -r requirements/sanic.txt
