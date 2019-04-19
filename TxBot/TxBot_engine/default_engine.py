import json

from snips_nlu import SnipsNLUEngine

from TxBot_layer.test_layer import TxSampleTestLayer
from .abstract_engine import TxBaseEngine

from config import PROCESSED_INPUT, FOR_OUTPUT

"""
Default Engine module will be used for manging the NLU engine.
"""


class TxDefaultEngine(TxBaseEngine):
    def __init__(self, input_object, output_object, engine_param=None):

        super(TxDefaultEngine, self).__init__(input_object, output_object, engine_param)
        self.engine = SnipsNLUEngine()
        # get the path of the dataset
        self.train_model(engine_param.get("dataset_path"))

    def train_model(self, path):

        with open(path) as dataset_file:

            self.engine.fit(json.load(dataset_file))

    def parse(self, request_text):

        return self.engine.parse(request_text)

    def add(self, layer):

        super(TxDefaultEngine, self).add(layer)

    def go(self, _next, args):
        super(TxDefaultEngine, self).go()

        if self.break_layer:
            # getting the result from the NLP engine.
            self.return_object[FOR_OUTPUT] = self.return_object[PROCESSED_INPUT]
        else:
            self.return_object[FOR_OUTPUT] = self.parse(
                self.return_object[PROCESSED_INPUT]
            )

        super().to_output(self.return_object)
        self.input_object = _next(args)
