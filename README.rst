Tx
==

Tx is an umbrella package which is has intergation Tx-Bot(small NLU chatbot) and Tx(Sanic web framework).

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%Sanic-ff69b4.svg
     :target: https://github.com/harshanarayana/cookiecutter-sanic
     :alt: Built with Cookiecutter Sanic


:License: MIT

.. warning::

     This project is still under hatching. So please support me till it hatches and spines of
     around the whole world, fast than speed of 'SuperMan'.

.. contents:: Table of Contents

----------
Installing 
----------

The Tx-Bot can be installed in very simple manner by just pulling a clone from github repository
and with your magical mind from `master`. Through if you preferred to go with traditional way
of following just like me don't worry I will help in your journey to dark side of the moon
where no one has ever gone through OFFICIALLY.

.. code-block:: bash

     git clone https://github.com/jawahar273/Tx.git TX
     cd Tx

To let all hell to lose. Follow the belove command for installing the Tx-Bot inside your computer.


.. code-block:: python

     pip install -r requirement/local.txt # for developement
     pip install -r requirement/production.txt # for production

     # for installing the Snip language resource
     python -m snips_nlu download en # for english language

---------------
To Get Starting
---------------

To get start with Tx-Bot might be difficult at first sight. Don't worry here are
some instruction to get start with the bot. `Step: 1` is installing the piece of the  code.

Step: 2
-------

Use of a CLI thing so called `scaff.py` which intensify  generate scaffolding for us, which a half
way through. There are two major sub division to remember in working with Tx-Bot one
is `storage` is folder which contain of sub folder along with intents sets(`intents set` are collection of
intent and organized in such a way for human classification &#x1F916;) and other folder is called 
`Bot_response` which contain the code to executed if the engine choose the response to show.


.. note::

     Please use `--help` before running the CLI to know what it is generating.

Step: 3 (optional)
------------------

Human do love to interaction with people but with bot(who cares??? ah...).
Who knows you may love it but not
at first site. Through training might need regressively. 

Step: 4
-------

Choose a nice folder for saving the dataset by using the `python scaff.py train` with proper
argument you can successfully save the dataset under the  default name `dataset.json`(it can be changed
with extra arguments).

.. note:: 

     There is below section which contain little details about architecure Tx-bot where for
     github is good at playing hide and seek you may see it.