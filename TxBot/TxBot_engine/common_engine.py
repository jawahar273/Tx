from TxBot_layer.test_layer import TxSampleTestLayer

from .abstract_engine import TxBaseEngine
from config import FOR_OUTPUT, PROCESSED_INPUT

"""
Common engine will only return the layer's result
as it is.
"""


class TxCommonEngine(TxBaseEngine):
    def __init__(self, input_object, output_object, engine_param=None):
        super(TxCommonEngine, self).__init__(input_object, output_object, engine_param)

    def add(self, layer):

        super(TxCommonEngine, self).add(layer)

    def go(self, _next, args):

        super(TxCommonEngine, self).go()
        self.input_object = _next(args)
        self.response_object[FOR_OUTPUT] = self.response_object[PROCESSED_INPUT]
        # return self.response_object
