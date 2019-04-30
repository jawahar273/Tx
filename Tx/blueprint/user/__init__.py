from sanic import Blueprint
from sanic.response import json

from Tx.dao import UserDAO
from config.stage import settings

email_regex = settings.EMAIL_VALID_REGEX

user = Blueprint(name="user", url_prefix="/user")


@user.route("/<user_id:int>")
async def get_user(request, user_id):
    user = await UserDAO.get_user(user_id)
    return json(user.to_dict())


# @user.route(f"/login/<email:{email_regex}>/<password>/", methods=["POST"])
# async def login_user(request, email, password):
#     status = await UserDAO.login_user(email, password)
#     return json(status)
