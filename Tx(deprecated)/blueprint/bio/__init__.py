from sanic.blueprints import Blueprint
from sanic.response import json, html
from sanic_openapi import doc

from Bot.Bot_engine.default_engine import DefaultEngine as Engine
from Bot.Bot_input.rest_input import RESTInput
from Bot.Bot_output.rest_output import RESTOutput
from Bot.Bot_layer.cmd.wiki import WikiLayer

from config.stage import settings
from utils import render_template_file as render_template

profile = Blueprint("Profile", url_prefix="/p")


__input = RESTInput(settings.engine_param)
__output = RESTOutput()
__engine = Engine(__input, __output, settings.engine_param)
__engine.add([WikiLayer({})])


@profile.route("/")
@doc.summary("Get Profile details")
@doc.produces({"status": str, "msg": str, "errCode": int, "html": str})
async def bot_intro(request):

    return html(render_template("profile/intro.html"))


@profile.route("/<query>")
@doc.summary("Get Profile details")
@doc.produces({"status": str, "msg": str, "errCode": int, "html": str})
async def profile_details(request, query):

    __input.step(query)

    # render_format = ''
    if request.args.get("pretty") == "true":

        return json({"status": "ok", "html": __engine.go(pretty="json.html")})

    else:

        return html(__engine.go(pretty="base.html"))
