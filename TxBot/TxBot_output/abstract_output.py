from abc import ABC, abstractmethod

from utils import import_class
from config import FOR_OUTPUT


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
        """
        """
        from IPython import embed; embed()

        return txObject

    # def next(self, to_input):
    #     print('calling abstract output')
    #     to_input['is_next'] = True

    #     self.next_fun().next(to_input)
