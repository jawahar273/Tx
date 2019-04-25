
from TxBot_response.abstract_response import TxBaseResponse


class ProfileImage(TxBaseResponse):

    def __init__(self):
        super(ProfileImage, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    def render(self):
        pass

