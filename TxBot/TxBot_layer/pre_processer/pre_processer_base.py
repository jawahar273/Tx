
from TxBot_layer.abstract_layer import TxBaseLayer
from config import ASSERTTYPE

class TxPreProcesserBase(TxBaseLayer):

    def __init__(self, param=None):

        self.return_object = None
        self.assert_type = param.get(ASSERTTYPE, str)

    def response(self, txObject):
        pass
