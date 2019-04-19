
from TxBot_layer.test_layer import TxSampleTestLayer 

from .abstract_engine import TxBaseEngine

class TxSampleTestEngine(TxBaseEngine):

    def __init__(self, input_object, output_object, engine_param=None):
        super(TxSampleTestEngine, self).__init__(input_object, output_object, engine_param)

    def add(self, layer):
        super(TxSampleTestEngine, self).add(layer)

    def go(self):
        super(TxSampleTestEngine, self).go()
        return self.response_object