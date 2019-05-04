from .abstract_output import BaseOutput


class RESTOutput(BaseOutput):
    def __init__(self, txObject=None):

        super(RESTOutput, self).__init__(txObject)

    def output(self, txObject):

        return super(RESTOutput, self).output(txObject)
