from TxBot_layer.abstract_layer import TxBaseLayer
from config import PROCESSED_INPUT, cmd_keywords, STOPLAYER, STOPLAYERNAME
from utils import parse_cmd


"""
Each Child must inheridate :class: TxCMDBaseLayer
for matching their command from the user.
"""


class TxCMDBaseLayer(TxBaseLayer):
    def __init__(self, param=None):

        super(TxCMDBaseLayer, self).__init__(param)
        self.keyword = None

    """
    Output must be passed through :func: response method.
    """

    def response(self, txObject):
        pass

    """
    Prasing the command from the user.
    """

    def check_cmd(self, keyword, txObject):
        self.keyword = parse_cmd(keyword, False)
        if txObject[PROCESSED_INPUT].startswith(self.keyword):
            return True
        return False

    def __str__(self):

        return self.keyword
