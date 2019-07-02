"""
-----
Pwned
-----
Do you know about data breach? If not then you should have atleast awareness
of data breach.  data breach is the intentional or unintentional release of secure or private/confidential information to an untrusted environment. Other terms for this 
phenomenon include unintentional information disclosure, data leak and also data spill. [#]_

To check if your personal information has been breach in of the organization that you have
been using in your day to day life or in the past. The response used Have I Been Pwned. [#]_

For example:

.. code-block:: yaml

    - have my email id Claudine85@alo.com been hacked
    - Check email id Nathanial112@hotmail.com been data breach


.. [#] Accouding to `Wikipedia <https://en.wikipedia.org/wiki/Data_breach>`_
.. [#] Get more detail from the `link <https://en.wikipedia.org/wiki/Have_I_Been_Pwned%3F>`_
"""
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
        the data breach by some sites.
        Inspired by .. _Leon: https://github.com/leon-ai/leon.

        @param email a email address to check for pwned.
        """
        # Delay for 2 seconds before
        # making request to accomodate API usage policy

        _email = parse.quote_plus(email)
        url = f"/api/v2/breachedaccount/{_email}"
        # truncate = "?truncateResponse=true"

        try:
            response = get(f"https://haveibeenpwned.com{url}")

            status_code = response.status_code

            if status_code == 404:

                return {
                    "statusCode": status_code,
                    "msg": {
                        "loop": False,
                        "data": f"Nothing found so far for the this mail address {email}",
                    },
                }

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

                return {
                    "statusCode": 200,
                    "msg": {
                        "loop": True,
                        "data": data,
                        "email": _email.encode("utf-8"),
                    },
                }

            elif status_code == 403:

                return {
                    "statusCode": status_code,
                    "msg": {
                        "loop": False,
                        "data": "accessed by unauthorized/banned clients",
                    },
                }

            elif status_code == 503:

                return {
                    "statusCode": status_code,
                    "msg": {"loop": False, "data": "site is unavailable"},
                }

            return status_code

        except exceptions.RequestException:

            return {
                "statusCode": 500,
                "msg": {
                    "loop": False,
                    "data": "Somthing is wrong in making this request",
                },
            }

    def level_of_compormised(self, data):

        total_compormised = len(data["data"])
        msg = []

        if total_compormised == 0:

            msg = ["Please make concern for privacy around you"]

        elif total_compormised > 1 and total_compormised <= 3:

            msg = ["Change password", "Use it for only truly trust website"]

        else:

            msg = [
                "Change password from time to time",
                "Please make concern for privacy around you",
            ]

        return {"compromised_sites": total_compormised, "recommentes": msg}

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Pwned, self).render(class_name=self.class_name, sub_path="_global")

        breach = None
        # change this code for `get_slot_by_name`
        for slot in self.scope["slots"]:

            if slot["slotName"] == "email":
                # _range = slot["range"]
                # rawValue = self.scope["input"]
                breach = self.check_for_breach(slot["rawValue"])
                breach["msg"]["breach_level"] = self.level_of_compormised(breach["msg"])
                break

        if breach is None:
            breach = {"msg": {"loop": False, "data": "Please provide mail address"}}
        return self.render_template.render(
            pretty=pretty, breachs=breach["msg"], len=len
        )
