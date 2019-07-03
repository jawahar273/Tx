from os.path import dirname, join, split

from socketio import Client
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession

from config.stage import settings

welcome_text = """
<ansigreen>
Hi, this is a welcome line from me to tell you that I am a bot \
handcraft for handling the function that I am tasked in handling as best I could.
Mode: CLI
</ansigreen>
"""

ws = Client()

style = Style.from_dict(
    {
        "h1": "#00695C",
        "h2": "#00796B",
        "h3": "#00897B",
        "h4": "#00897B",
        "h5": "#009688",
        "a": "#ECEFF1 underline",
        "p": "#548bb5",
    }
)


@ws.on("from_server")
def from_server(data):

    print_formatted_text(HTML(data["response"]), style=style)


class entryPoint:
    """
    Intergating with prompt tool kit is used for handling the history of
    the cli and for key binding.
    """

    def __init__(self):
        self.ws = ws
        self.session = PromptSession()
        self.ws.connect(f"http://{settings.HOSTNAME}:5000/")

        while True:
            try:
                text = self.session.prompt("#> ")

                if text == "" or not text:
                    continue
                self.emit_to_server(text)

            except KeyboardInterrupt:
                print_formatted_text("Sleep Mode!!!!.....")
                break
            except EOFError:
                break
            finally:
                self.ws.disconnect()

    def emit_to_server(self, text):
        self.ws.emit("from_client", data={"text": text})


# temp: solution
class entryPoint2:
    """
    Intergating with prompt tool kit is used for handling the history of
    the cli and for key binding.
    """

    def __init__(self):
        self.ws = ws
        self.session = PromptSession()

        while True:
            try:
                text = self.session.prompt("#> ")

                if text == "" or not text:
                    continue
                self.run(text)

            except KeyboardInterrupt:
                print_formatted_text("Sleep Mode!!!!.....")
                ws.disconnect()
                break
            except EOFError:
                break

    def run(self, text):

        self.client = Client()
        self.ws.connect(f"http://{settings.HOSTNAME}:5000/")

        self.ws.emit("from_client", data={"text": text})
        self.ws.sleep(0.5)
        self.ws.disconnect()
