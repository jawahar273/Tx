from sqlalchemy_utils import EmailType, PasswordType

from Tx.model import DATABASE as db


class User(DATABASE.Model):
    __tablename__ = "users"

    id = db.Column(
        db.BigInteger(), primary_key=True, nullable=False, autoincrement=True
    )
    # name = db.Column(db.Unicode(), nullable=False)
    email = db.Column(EmailType(), index=True, nullable=False)
    password = db.Column(
        PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"])
    )
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean(), default=False, nullable=False)

    def verify_password(self, password):
        """
        Verfiy the give password with the DB passowrd values
        """

        return self.password == password

    def to_dict(self):
        """
        Return the dict for Sanic it is very useful for
        sending json if the instance SELECTED based on 
        query condtion.
        """
        properties = ["id", "email", "is_active"]
        return {prop: getattr(self, prop, None) for prop in properties}

    def __str__(self):
        return "{}<{}>".format(self.name, self.id)

    def __repr__(self):
        return self.__str__()
