import json

from snips_nlu import SnipsNLUEngine

from .abstract_engine import BaseEngine

from Bot.config import PROCESSED_INPUT, FOR_OUTPUT, NLUSCOPE
from Bot.utils import import_response_intent

# from config.stage.settings import logger
from config.stage import logger

class DefaultEngine(BaseEngine):
    """
    Default Engine module will be used for manging the NLU engine.
    """

    def __init__(self, input_object, output_object, engine_param=None):

        super(DefaultEngine, self).__init__(input_object, output_object, engine_param)
        self.engine_name = "default_engine"
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
        """
        Get the :class: `Dict` status from NLU or command
        execution successfully, the one
        response class :module: `Bot.Bot_response`
        imported.
        """

        intent_name = scope["intent"]["intentName"] or "defaultIntent_default"

        return import_response_intent(intent_name)(scope=scope)

    def command_success_response(self, txObject):

        txObject.update(
            {NLUSCOPE: {"intent": {"intentName": "commandsIntent_command"}}}
        )

    def add(self, layer):

        super(DefaultEngine, self).add(layer)

    def go(self, pretty="base.html"):

        # super() must be called
        super(DefaultEngine, self).go()

        if self.break_layer:
            # getting the result from the NLP engine.
            self.return_object[FOR_OUTPUT] = self.return_object[PROCESSED_INPUT]

            self.command_success_response(self.return_object)

        else:

            self.return_object[NLUSCOPE] = self.parse(
                self.return_object[PROCESSED_INPUT]
            )


        del self.return_object[PROCESSED_INPUT]

        # after success of getting return value from the NLU
        # or command status the return value are pass into
        # response object for template parsing.

        _class = self.response(self.return_object[NLUSCOPE])

        if self.break_layer:

            self.return_object[FOR_OUTPUT] = _class.render(
                self.return_object, pretty=pretty
            )

        else:

            self.return_object[FOR_OUTPUT] = _class.render(pretty=pretty)

        output_result = super().to_output(self.return_object)

        super().next()

        return output_result
