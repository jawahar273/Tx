from sanic_jwt.exceptions import AuthenticationFailed

from Tx.model.user import User


class UserDAO(User):
    @classmethod
    async def get_user_by_id(cls, user_id: int) -> User:
        user = await cls.get_or_404(user_id)
        return user
