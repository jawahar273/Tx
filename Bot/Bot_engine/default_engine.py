import json

from snips_nlu import SnipsNLUEngine
from loguru import logger

from .abstract_engine import BaseEngine

from Bot.config import PROCESSED_INPUT, FOR_OUTPUT, NLUSCOPE
from Bot.utils import import_response_intent

from config.stage import LOG_PATH
from utils import path_join

logger.add(f'{path_join(LOG_PATH,"engine.log")}')


class DefaultEngine(BaseEngine):
    """
    Default Engine module will be used for managing the NLU engine.
    """

    def __init__(self, input_object, output_object, engine_param=None):

        super(DefaultEngine, self).__init__(input_object, output_object, engine_param)
        self.engine_name = "default_engine"
        logger.info("Initializing the engine..")
        self.engine = SnipsNLUEngine()
        # get the path of the dataset
        dataset_path = engine_param.get("dataset_path")
        self.train_model(dataset_path)

    def train_model(self, path):
        """
        Train the NLU JSON format by SNIP NLU.

        :param str path: path of the dataset.json
        """
        with open(path) as dataset_file:

            self.engine.fit(json.load(dataset_file))
        logger.info("Successfully loading the trained data sets")

    def parse(self, request_text):
        """
        Parser the given user's text using the the
        Snip NLU engine.
        """
        engine = self.engine.parse(request_text)

        return engine

    def response(self, scope):
        """
        Get the :class:`Dict` status from NLU or command
        execution successfully, the one
        response class :mod:`Bot.Bot_response`
        imported.
        """

        intent_name = scope["intent"]["intentName"] or "defaultIntent_default"
        logger.debug(f"getting the intent class name: {intent_name}")

        return import_response_intent(intent_name)(scope=scope)

    def command_success_response(self, txObject):
        """
        Find if there the given user's text is related
        to command request. if then change the scope
        intent name as ``commandsIntent_command``.
        """
        logger.debug(f"getting the intent class name as: commandsIntent_command")

        txObject.update(
            {NLUSCOPE: {"intent": {"intentName": "commandsIntent_command"}}}
        )

    def add(self, layer):
        """
        Add the layer function into the engine's
        list for executing of the layer function.
        
        :param: :mod:`Bot.Bot_layer.abstract_layer` layer the object
        of function are added as layer into the engine for concurrency
        exection.
        """
        super(DefaultEngine, self).add(layer)

    def go(self, pretty="base.html"):
        """
        :param: pretty is the name of the file where the meta data or base line of html
            are saved and it is parsed along with return result. Currently base.html and json.html
            is taken as parameter.
        """
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

        # DEPRECATED:
        super().next()
        logger.debug(f"running the parser ")

        return output_result
