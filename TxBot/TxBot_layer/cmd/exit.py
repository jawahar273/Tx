from sys import exit

from TxBot.TxBot_layer.cmd.cmd_base_layer import TxCMDBaseLayer
from TxBot.config import PROCESSED_INPUT, COMMANDS
from TxBot.utils import parse_cmd


class TxExitLayer(TxCMDBaseLayer):

    def __init__(self, param=None):

        super(TxExitLayer, self).__init__(param)

    def response(self, txObject):

        if self.check_cmd(COMMANDS['EXIT']['name'], txObject):

            exit(0)

        return txObject
