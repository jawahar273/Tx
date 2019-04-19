"""
Layer for engine is like drop out which help in stop the
engine to run unnessary. For example if you run a command
there is not need for running NLU. 
"""
from abc import ABC, abstractmethod


class TxAbstractLayer(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):

        raise NotImplementedError("__init__() is not implemented")

    @abstractmethod
    def response(self, *args, **kwargs):

        raise NotImplementedError("response() is not implemented")


class TxBaseLayer(TxAbstractLayer):
    def __init__(self, params):
        """
        Get the input data from the layer/input
        ..notes:
        1. check the given is in the required data type
            if not raise error
        2. processed data must be return with in response function
        """
        self.params = params

    def response(self, txObject=None):
        """
        response() must be defined by each sub class.
        Every subclass response must return `txObject` object
        """
        pass

    def on_success(self, txObject):
        """
        Wraper function for passing :func: `response` on the event of
        success.
        """
        pass

    def on_fails(self, txObject):
        """
        Wraper function for passing :func: `response` on the event of
        fails.
        """
        pass
