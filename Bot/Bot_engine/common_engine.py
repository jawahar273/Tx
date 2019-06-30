"""
Common engine will only return the layer's result
as it is.
# @depreacted mode

"""
from Bot.Bot_layer.test_layer import SampleTestLayer

from .abstract_engine import BaseEngine
from Bot.config import FOR_OUTPUT, PROCESSED_INPUT


class CommonEngine(BaseEngine):

    def __init__(self, input_object, output_object, engine_param=None):
        super(CommonEngine, self).__init__(input_object, output_object, engine_param)

    def add(self, layer):

        super(CommonEngine, self).add(layer)

    def go(self, _next, args):

        super(CommonEngine, self).go()
        self.input_object = _next(args)
        self.response_object[FOR_OUTPUT] = self.response_object[PROCESSED_INPUT]
        # return self.response_object
