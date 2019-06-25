from os import getenv
from importlib import import_module
from datetime import datetime 

from walrus import Walrus
from huey import RedisHuey

settings = import_module(getenv("CONFIG", "config.local"))
logger = settings.logger

db = Walrus(
    host=getenv('REDIS-HOST', 'localhost'),
    port=getenv('REDIS-PORT', 6379),
    db=getenv('REDIS-DB', 1)
)

Huey = RedisHuey(
    host=getenv('REDIS-HOST', 'localhost'),
    port=getenv('REDIS-PORT', 6379),
    db=getenv('REDIS-DB', 2)
)

# from blinker import signal

# from scheduler import HEARTBEAT

# SCHEDULER_SIGNAL = signal('SCHEDULER')
# heartbeat_meta = {
#     'last_checkpoint': None
# }

# def check_heartbeat_schedular(sender):

#     heartbeat_meta['last_checkpoint'] = datetime.now()

# HEARTBEAT.connect(check_heartbeat_schedular)