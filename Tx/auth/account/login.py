async def login_user(request, *args, **kwargs):
    """
    :func: `Tx.dao.login_user` is authenticate for
    for generating JWT.
    """
    username = request.json.get("email", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise AuthenticationFailed("Email or Password field is empty")
    # from IPython import embed; embed()

    select_user = await User.query.where(User.email == email).gino.first()

    if select_user is not None and select_user.verify_password(password) is not False:

        return select_user

        # login user

    else:

        raise AuthenticationFailed("Invalid Email or Password")
