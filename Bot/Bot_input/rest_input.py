from .abstract_input import BaseInput


class RESTInput(BaseInput):
    def __init__(self, txObject):
        self.txObject = txObject

    def processed(self):

        super(RESTInput, self).processed()
        return self.return_object

    def step(self, text):
        """
        Extra step for handling the input to the
        bot with custom method.
        """
        self.txObject.update({"text": text})
        super(RESTInput, self).__init__(self.txObject)
