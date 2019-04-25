import json

from snips_nlu import SnipsNLUEngine

from .abstract_engine import TxBaseEngine

from TxBot.config import PROCESSED_INPUT, FOR_OUTPUT
from TxBot.utils import import_response_intent


class TxDefaultEngine(TxBaseEngine):
    """
    Default Engine module will be used for manging the NLU engine.
    """
    def __init__(self, input_object, output_object, engine_param=None):

        super(TxDefaultEngine, self).__init__(
            input_object, output_object, engine_param
        )
        self.engine_name = 'default_engine'
        self.engine = SnipsNLUEngine()
        # get the path of the dataset
        dataset_path = engine_param.get("dataset_path")
        self.train_model(dataset_path)

    def train_model(self, path):

        with open(path) as dataset_file:

            self.engine.fit(json.load(dataset_file))

    def parse(self, request_text):

        engine = self.engine.parse(request_text)
        return engine

    def response(self, scope):

        intent_name = scope['intent']['intentName'] or 'defaultIntent_default'
        # from IPython import embed; embed()
        return import_response_intent(intent_name)

    def add(self, layer):

        super(TxDefaultEngine, self).add(layer)

    def go(self):

        # super() must be called
        super(TxDefaultEngine, self).go()

        if self.break_layer:
            # getting the result from the NLP engine.
            self.return_object[FOR_OUTPUT] = self.return_object[PROCESSED_INPUT]

        else:

            self.return_object[FOR_OUTPUT] = self.parse(
                self.return_object[PROCESSED_INPUT]
            )

            # from IPython import embed; embed()

            _class = self.response(
                self.return_object[FOR_OUTPUT]
            )()

            self.return_object = _class.render()



        output_result = super().to_output(
            self.return_object
        )

        self.next()

        return output_result
