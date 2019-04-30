from sanic import Sanic
from sanic.response import redirect

# ##JWT token
from sanic_jwt import initialize

# ##BluePrint
from Tx.blueprint.user import user
from Tx.blueprint.health import health
from Tx.blueprint.bio import profile

# ##Database
from Tx.model import DATABASE
from Tx.auth import login_user

# ##Utils
from Tx.util import setup_database_creation_listener
from Tx.util import setup_rate_limiter


app = Sanic(__name__)

# ##Static files.
app.static("static", "./templates/static")

limiter = setup_rate_limiter(app)

# ##Boostraping Database connection
setup_database_creation_listener(app, DATABASE)

# ##Boostraping Authentication

# intialize must be place top of blueprint if the
# blueprint requires authentication.
# [link](https://sanic-jwt.readthedocs.io/en/latest/pages/initialization.html#instance)
initialize(app, authenticate=login_user)

# app.blueprint(openapi_blueprint)
if app.config["DEBUG"]:

    from sanic_openapi import swagger_blueprint, doc  # openapi_blueprint

    app.blueprint(swagger_blueprint)


app.blueprint(health)
app.blueprint(profile)
app.blueprint(user)


@app.route("/")
async def default(request):
    return redirect("/p", status=301)


@app.route("/<query>")
async def default(request, query):
    return redirect(f"/p/{query}", status=301)
