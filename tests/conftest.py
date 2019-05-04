from sys import path as sys_path
from os import path as os_path

sys_path.insert(0, os_path.join(os_path.dirname(os_path.abspath(__file__)), ".."))
from utils import env_str

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TEST_MODULE = env_str("TEST_MODULE", "ALL")
if TEST_MODULE == "all":

    from conftest_tx import *
    from conftest_bot import *

elif TEST_MODULE == "tx":

    from conftest_tx import *

elif TEST_MODULE == "txbot":

    from conftest_bot import *
