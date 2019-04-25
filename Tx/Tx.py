from sanic import Sanic
from sanic.response import json
from sanic_openapi import swagger_blueprint, doc # openapi_blueprint
from Tx.blueprint.health import health
from Tx.blueprint.bio import profile
from Tx.model import DATABASE
from Tx.blueprint.user import user
from Tx.util import setup_database_creation_listener
from Tx.util import setup_rate_limiter


app = Sanic(__name__)

limiter = setup_rate_limiter(app)


# app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)

app.blueprint(health)
app.blueprint(profile)
app.blueprint(user)
setup_database_creation_listener(app, DATABASE)


@app.route("/")
async def default(request):
    return json({"message": "hello Sanic!"})
