
from .abstract_input import TxBaseInput


class RESTInput(TxBaseInput):

    def __init__(self, txObject):
        self.txObject = txObject

    def processed(self):

        super(RESTInput, self).processed()
        return self.return_object

    def step(self, text):
        self.txObject.update({'text': text})
        super(RESTInput, self).__init__(self.txObject)
