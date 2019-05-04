from Bot.Bot_layer.abstract_layer import BaseLayer
from Bot.config import PROCESSED_INPUT, COMMANDS, STOPLAYER, STOPLAYERNAME
from Bot.utils import parse_cmd


"""
Each Child must inheridate :class: CMDBaseLayer
for matching their command from the user.
"""


class CMDBaseLayer(BaseLayer):
    def __init__(self, param=None):

        super(CMDBaseLayer, self).__init__(param)
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
