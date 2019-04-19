
from .abstract_layer import TxBaseLayer


class TxSampleTestLayer(TxBaseLayer):

    def __init__(self, params):
        """
        Get the input data from the layer/input
        ..notes:
        1. check the given is in the required data type
            if not raise error
        2. processed data must be return with in response function
        """
        super(TxSampleTestLayer, self).__init__(params)

    def response(self, txObject):

        print("from test layer", type(txObject))
        super(TxSampleTestLayer, self).response(txObject)
        return txObject