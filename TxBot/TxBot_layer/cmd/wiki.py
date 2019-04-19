from mediawiki import MediaWiki
from mediawiki.exceptions import DisambiguationError

from TxBot_layer.cmd.cmd_base_layer import TxCMDBaseLayer
from config import PROCESSED_INPUT, cmd_keywords, STOPLAYERNAME
from utils import parse_cmd, parse_cmd_value


"""
Getting the Summary for the give keyword if it
available in the wikipedia.
"""


class TxWikiLayer(TxCMDBaseLayer):
    def __init__(self, param=None):

        super(TxWikiLayer, self).__init__(param)

    def response(self, txObject):

        super(TxWikiLayer, self).response(txObject)

        if self.check_cmd(cmd_keywords["WIKI"]["name"], txObject):

            key_value = parse_cmd_value(txObject[PROCESSED_INPUT])
            wikipedia = MediaWiki()
            respose_value = None

            try:

                respose_value = wikipedia.page(key_value).summary

            except DisambiguationError as e:

                respose_value = str(e)

            txObject[PROCESSED_INPUT] = respose_value
            STOPLAYER.send()
        return txObject
