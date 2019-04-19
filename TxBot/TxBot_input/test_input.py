
from .abstract_input import TxBaseInput


class TxSampleTestInput(TxBaseInput):

    def __init__(self, txobject):
        """
        Get the input object as `Dict`
        """
        super(TxSampleTestInput, self).__init__(txobject)


    def get_object(self, txobject):

        return super(TxSampleTestInput, self).get_object(txobject)


    def delete(self, txobject):
        """
        Delete the input related key in txobject
        """
        super(TxSampleTestInput, self).delete(txobject)


    def get_access_keys(self):
        """
        Response for distributing keys
        """
        return super(TxSampleTestInput, self).get_access_keys()

    def processed(self):
        """
        Input raw data are processed.
        """
        super(TxSampleTestInput, self).processed()

        self.return_object.update({'process_input': self.input_value['text']})
        print("pri", self.return_object, type(self.return_object))
        return self.return_object

    def next(self):
        pass