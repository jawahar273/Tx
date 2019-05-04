from TxBot_layer.pre_processer.pre_processer_base import TxPreProcesserBase
from config import PROCESSED_INPUT, COMMANDS, ASSERTTYPE


class TxTokenization(TxPreProcesserBase):
    def __init__(self, arg):
        super(TxTokenization, self).__init__(params={ASSERTTYPE: str})

    def response(self, txObject):

        assert isinstance(
            txObject[PROCESSED_INPUT], str
        ), f"input must in the type of {self.assert_type}"

        txObject[PROCESSED_INPUT] = txObject[PROCESSED_INPUT].split(" ")
        return txObject
