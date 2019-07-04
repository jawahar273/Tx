from raven.response.abstract_response import BaseResponse


class ProfileImage(BaseResponse):
    def __init__(self):
        super(ProfileImage, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    def render(self):
        pass
