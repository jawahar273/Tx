"""
Input model are created as a pre-processing
set in improving/converting the user text in
a understandable way. For example if the given
text must be searched in stackover flow and the
result can be taken to engine.
"""

from abc import ABC, abstractmethod

from raven.config import PROCESSED_INPUT


class AbstractInput(ABC):
    @abstractmethod
    def __init__(self, *args, **kwarg):

        raise NotImplementedError("`__init__` is not implemented")

    @abstractmethod
    def processed(self):

        raise NotImplementedError("processed() is not implemented")


class BaseInput(AbstractInput):
    def __init__(self, txObject):
        """
        Get the input object as .. py:class:: `Dict`
        .. notes::
            txObject.update({'text': 'Value must be upates on each function',})
        """
        if txObject:
            self.pre_loading_set(txObject)

    def pre_loading_set(self, txObject):
        self.input_value = self.get_object(txObject)
        self.return_object = {}
        self.delete(txObject)

    def get_object(self, txObject):

        temp = {}
        temp.update({key: txObject[key] for key in self.get_access_keys()})
        return temp

    def delete(self, txObject):

        for key in self.get_access_keys():
            if txObject.get(key):
                del txObject[key]

        self.return_object.update(txObject)

    def get_access_keys(self):
        """
        Which return the current object
        access keys which will be used internally by input object
        class.
        """
        return ("input_params",)

    def processed(self):
        """
        This method must be implemented on each new sub class.
        return must of dict type with `key`: 'PROCESSED_INPUT'.
        """
        self.return_object.update({PROCESSED_INPUT: self.return_object["text"].strip()})

    # def next(self, to_input):
    #     pass
