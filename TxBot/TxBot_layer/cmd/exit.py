from sys import exit

from TxBot_layer.cmd.cmd_base_layer import TxCMDBaseLayer
from config import PROCESSED_INPUT, cmd_keywords
from utils import parse_cmd


class TxExitLayer(TxCMDBaseLayer):

    def __init__(self, param=None):

        super(TxExitLayer, self).__init__(param)

    def response(self, txObject):

        if self.check_cmd(cmd_keywords['EXIT']['name'], txObject):

            exit(0)

        return txObject
