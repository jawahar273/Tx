from abc import ABC, abstractmethod

from TxBot.utils import import_class
from TxBot.config import FOR_OUTPUT


class TxAbstractOutput(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("__init__() is not implemented")

    @abstractmethod
    def output(self, *args, **kwargs):
        raise NotImplementedError("output() is not implemented")


class TxBaseOutput(TxAbstractOutput):
    def __init__(self, txObject=None):
        pass

    def output(self, txObject):

        return txObject[FOR_OUTPUT]
