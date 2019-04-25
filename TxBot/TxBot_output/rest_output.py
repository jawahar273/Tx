
from .abstract_output import TxBaseOutput


class RESTOutput(TxBaseOutput):
    def __init__(self, txObject=None):

        super(RESTOutput, self).__init__(txObject)

    def output(self, txObject):

        return super(RESTOutput, self).output(txObject)

