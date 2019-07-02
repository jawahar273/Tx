

===============
To Get Starting
===============

To get start with Tx-Bot might be difficult at first sight. Don't worry here are
some instruction to get start with the bot. ``Step: 1`` is installing the piece of the  code.

.. warning::

     Hey if you thought the below section is hard to read then read this section :doc:`usage`.

Step: 2
-------

Use of a CLI thing so called ``scaff.py`` which intensify  generate scaffolding for us, which a half
way through. There are two major sub division to remember in working with Tx-Bot one
is ``storage`` is folder which contain of sub folder along with intents sets(``intents set`` are collection of
intent and organized in such a way for human classification) and other folder is called 
``Bot_response`` which contain the code to executed if the engine choose the response to show.


.. note::

     Please use `--help` before running the CLI to know what it is generating.

Step: 3 (optional)
------------------

Human do love to interaction with people but with bot(who cares??? ah...).
Who knows you may love it but not
at first site. Through training might need regressively. 

Step: 4
-------

Choose a nice folder for saving the dataset by using the ``python scaff.py train`` with proper
argument you can successfully save the dataset under the  default name ``dataset.json``(it can be changed
with extra arguments).
