# @deprecated
from sys import exit

from Bot.Bot_layer.cmd.cmd_base_layer import CMDBaseLayer
from Bot.config import PROCESSED_INPUT, COMMANDS
from Bot.utils import parse_cmd


class ExitLayer(CMDBaseLayer):
    def __init__(self, param=None):

        super(ExitLayer, self).__init__(param)

    def response(self, txObject):

        if self.check_cmd(COMMANDS["EXIT"]["name"], txObject):

            exit(0)

        return txObject
