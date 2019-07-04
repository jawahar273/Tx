from mediawiki import MediaWiki
from mediawiki.exceptions import DisambiguationError

from raven.layer.cmd.cmd_base_layer import CMDBaseLayer
from raven.config import PROCESSED_INPUT, COMMANDS, STOPLAYER
from raven.utils import parse_cmd_value


class WikiLayer(CMDBaseLayer):
    """
    Getting the Summary for the give keyword if it
    available in the wikipedia.
    """

    def __init__(self, param=None):

        super(WikiLayer, self).__init__(param)

    def response(self, txObject):

        super(WikiLayer, self).response(txObject)

        if self.check_cmd(COMMANDS["WIKI"]["name"], txObject):

            key_value = parse_cmd_value(txObject[PROCESSED_INPUT])

            respose_value = None
            try:

                wikipedia = MediaWiki()

                try:

                    respose_value = wikipedia.page(key_value).summary

                except DisambiguationError as e:

                    respose_value = str(e)

                txObject[PROCESSED_INPUT] = respose_value
                STOPLAYER.send()

            except ConnectionError as e:

                txObject[PROCESSED_INPUT] = str(e)

        return txObject
