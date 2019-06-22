======
Tx-Bot
======

Tx-Bot Module provide the nessary class from intergating the chat-bot
objects. TxBot is like general purpose chat build based with the help
of `snips-nlu`. Snips-nlp is an Natural Language Understanding engine which
is a part of Natural Language Process, where NLU help the machine
to understand the given task at the hand. Such as `What will be the weather in paris at 9pm?` this example can be divided into near human
understanding with the help of snips-nlp.


  .. code:: json

        {
           "...",
           "slots": [
              {
                 "value": "paris",
                 
              },
              {
                 "value": {
                    "kind": "Time",
                    "value": "2018-02-08 20:00:00 +00:00"
                 },
                 "entity": "snips/datetime",
                 "..."
              }
           ]
        }


TxBot is basicaly divided into 5 parts which is `Input`, `Engine`, `Layers` and `Output`.

    .. code-block:: js

        Input --> Engine --> Response(Action) --> Ouput
                    ^
                    |
                    |
                  Layers(also can act as MiddleWare)

Intra dependency folder in default config
=======================================

This section is used to describe the intera dependency for an successfull completetion
of the intent and its code corresponding.  If an new internt and response are created
using the cmd then `dummy` will be created under the following main folder.

.. code-block::

   storage
      | _global
         | dummy

   Bot_response
      | _global
         | dummy

      | template
         | _global
            | dummy
