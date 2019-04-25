from sanic.blueprints import Blueprint
from sanic.response import json, html
from sanic_openapi import doc

from TxBot.TxBot_engine.default_engine import TxDefaultEngine as Engine
from TxBot.TxBot_input.rest_input import RESTInput
from TxBot.TxBot_output.rest_output import RESTOutput
from TxBot.TxBot_layer.cmd.wiki import TxWikiLayer 

profile = Blueprint("Profile", url_prefix="/p")

engine_param = {
    'dataset_path': 'TxBot/storage/_profile/dataset/dataset.json',
    'next_class': 'TxBot.TxBot_input.rest_input.RESTInput',
    'input_params': {},
    # 'output_class': 'TxBot_output.cli_output.CLIOutput',
    'is_next': False,
}

__input = RESTInput(engine_param)
__output = RESTOutput()
__engine = Engine(__input, __output,engine_param)
__engine.add([TxWikiLayer({})])


@profile.route("/<query>")
@doc.summary("Get Profile details")
@doc.produces({"status": str, "msg": str, "errCode": int, "html": str})
async def profile_details(request, query):

    __input.step(query)
    

    return html(__engine.go())
