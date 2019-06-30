"""
Schedule mainter is main module to run separated along with TxBot as is scheduler the
task given by it. Huey will work along with the following dependency
for flexibility such as  `RedisDB <https://redis.io/>`_ and along with 
`Walrus <https://walrus.readthedocs.io/>`_ a lightweight Python utilities for working
with `redis-py <https://github.com/andymccurdy/redis-py>`_.

    .. code-block:: bash

        huey_consumer maintainer.Huey -w 2 -c 2

"""

from config.stage import Huey

from Bot.Bot_response.response_schedule import *
