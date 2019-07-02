
Development
-----------

Development section will be used to describe the nessary step for bootstraping with 
``Raven``. After cloneing the repo the some of the sequenice of command are recommneded for
handling some issue.


Pre-commit
**********

`Pre-commit <https://github.com/pre-commit/pre-commit>`_ is used to execute some function which can be defined in ``.pre-commit-config.yaml``.
To work around with the package following command are recommneded.

.. code-block:: bash

    $ pre-commit install # Initializing pre-commit
        pre-commit installed at .git/hooks/pre-commit
    $ pre-commit run # installing the pre-commit config packages.
        [INFO] Initializing environment for https://github.com/ambv/black.
        [INFO] Installing environment for https://github.com/ambv/black.
        [INFO] Once installed this environment will be reused.
        [INFO] This may take a few minutes...
        black................................................(no files to check)Skipped


merge_dev.py
************

.. automodule:: merge_dev
