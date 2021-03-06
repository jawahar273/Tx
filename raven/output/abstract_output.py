from abc import ABC, abstractmethod

from raven.utils import import_class
from raven.config import FOR_OUTPUT

from utils import import_class


class AbstractOutput(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):

        raise NotImplementedError("__init__() is not implemented")

    @abstractmethod
    def output(self, *args, **kwargs):

        raise NotImplementedError("output() is not implemented")


class BaseOutput(AbstractOutput):
    def __init__(self, txObject: dict = None):
        """
        All the attribute start with underscore
        is treated as parameter from outside or engine.
        """
        self._tag_remove = None

    def wrapper(self, output):

        if self._tag_remove is None:

            return output

        return self._tag_remove(output)

    def output(self, txObject: dict):

        return self.wrapper(txObject[FOR_OUTPUT])

    def params(self, oparams: dict) -> None:

        if oparams is not None:

            tag_remove = oparams.get("tag_remove")

            if tag_remove:

                self._tag_remove = import_class(tag_remove)
