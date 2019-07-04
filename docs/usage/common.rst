
.. warning:: 

    ..code-block:: bash
    
        flask run --no-reload
    
    Run the flask with auto reload disable.
    

Resourceful Command
--------------------

Snips NLU has courpus dependency and this courpus can be diffrent language but in ``Raven``
we are currently concentrating only on english. This commnad is recommented if you are going
start working raven bot.

.. code-block:: bash

    python -m snips_nlu download en


tui.py
******

To run the bot in the TUI which can test or to run in production.

.. code-block:: bash

    python tui.py


Scheduler
*********

`Huey <https://huey.readthedocs.io>`_ is light weight task queue which schedule tasks to execute at a given time, or after a given delay,
schedule recurring tasks, like a crontab, task prioritization, task pipelines etc..

.. automodule:: maintainer

.. automodule:: raven.response.response_schedule

