from requests import exceptions, get
from loguru import logger

from Bot.Bot_response.abstract_response import BaseResponse


class Getmyip(BaseResponse):
    def __init__(self, scope=None):

        super(Getmyip, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def get_ip(self):
        try:

            result = get("https://api.ipify.org/?format=text")
            logger.debug("Getting ip addres of the user ")

            return result.text

        except exceptions.RequestException:

            return "ahh some error occur"

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Getmyip, self).render(class_name=self.class_name, sub_path="_global")
        return self.render_template.render(pretty=pretty, ip_addr=self.get_ip())
