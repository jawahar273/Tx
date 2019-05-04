from time import sleep
from urllib import parse
from requests import exceptions, get

from Bot.Bot_response.abstract_response import BaseResponse


class Pwned(BaseResponse):
    def __init__(self, scope=None):

        super(Pwned, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def check_for_breach(self, email):
        """
        Check the given email is haven pwned in
        the data breatch by some sites.
        Inspired by .. _Leon: https://github.com/leon-ai/leon.

        @param email a email address to check for pwned.
        """

        # Delay for 2 seconds before
        # making request to accomodate API usage policy

        url = f"/api/v2/breachedaccount/{parse.quote_plus(email)}"
        truncate = "?truncateResponse=true"

        try:
            response = get(f"https://haveibeenpwned.com{url}")
            status_code = response.status_code

            if status_code == 404:

                return None

            elif status_code == 200:

                data = []

                for index, b in enumerate(response.json()):

                    data.extend(
                        [
                            {
                                "url": "http://" + b["Domain"],
                                "name": b["Name"],
                                "total": b["PwnCount"],
                            }
                        ]
                    )

                return {"statusCode": 200, "msg": data}

            elif status_code == 403:
                return {
                    "statusCode": status_code,
                    "msg": "accessed by unauthorized/banned clients",
                }
            elif status_code == 503:
                return {"statusCode": static_code, "msg": "site is unavailable"}

            return status_code
        except exceptions.RequestException as e:
            return {
                "statusCode": 500,
                "msg": "Somthing is wrong in making this request",
            }

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Pwned, self).render(class_name=self.class_name, sub_path="_global")

        for slot in self.scope["slots"]:

            if slot["slotName"] == "email":
                _range = slot["range"]
                rawValue = self.scope["input"]
                breatch = self.check_for_breach(slot["rawValue"])
                break
        return self.render_template.render(pretty=pretty, breatchs=breatch["msg"])
