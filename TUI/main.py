from os.path import dirname, join, split

from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession

from Bot.Bot_engine.default_engine import DefaultEngine as Engine
from Bot.Bot_input.rest_input import RESTInput
from Bot.Bot_output.rest_output import RESTOutput
from Bot.Bot_layer.cmd.wiki import WikiLayer

from config.stage import settings
from utils import render_template_file as render_template

reset_input = RESTInput(settings.engine_param)
rest_output = RESTOutput()
engine = Engine(reset_input, rest_output, settings.engine_param)
engine.add([WikiLayer({})])

welcome_text = """
<ansigreen>
Hi, this is a welcome line from me to tell you that I am a bot
handcraft for handling the function that I am tasked in handling as best I could.
</ansigreen>
"""

def entryPoint():
    session = PromptSession()

    print_formatted_text(HTML(welcome_text))

    while True:
        try:
            text = session.prompt('#> ')
            reset_input.step(text)
            style = Style.from_dict({
                'h1': '#00695C',
                'h2': '#00796B',
                'h3': '#00897B',
                'h4': '#00897B',
                'h5': '#009688',
                'a': '#ECEFF1 underline',
                'p': '#548bb5'
            })
            print_formatted_text(HTML(engine.go(pretty="json.html")), style=style)
        except KeyboardInterrupt:
            print_formatted_text('Sleep Mode!!!!.....')
            break
        except EOFError:
            break


    # print_formatted_text(HTML(engine.go(pretty="base.html")), style=style)

    # render_format = ''
    # if request.args.get("pretty") == "true":

    #     return json({"status": "ok", "html": engine.go(pretty="json.html")})

    # else:

    #     return print_formatted_text(engine.go(pretty="base.html"))
