from src.repositories import UsersRepository
from src.models import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import random
import string


class SecurityService:
    def __init__(self, users_repository: UsersRepository, security: dict):
        self.users_repository = users_repository
        self.security = security

    @property
    def SECRET_KEY(self):
        return self.security["secret_key"]

    @property
    def SESSION_TIME(self):
        return self.security["session_time"]

    def authenticate(self, user_login: str, user_password: str):
        user = self.users_repository.get_by_login(user_login)
        if user != None and check_password_hash(
            pwhash=user.password,
            password=user_password + user.salt,
        ):
            token = jwt.encode(
                payload={
                    "user": user.login,
                    "exp": datetime.datetime.utcnow()
                    + datetime.timedelta(minutes=self.SESSION_TIME),
                },
                key=self.SECRET_KEY,
                algorithm="HS256",
            )
            return {"token": token}
        raise ValueError("invalid_credentials")

    def init_seeds(self):
        user_seed = (
            self.security["seeds"]["user"]
            if self.security["seeds"] != None and self.security["seeds"]["user"]
            else None
        )
        if user_seed != None and not self.users_repository.exist_by_login(
            user_seed["login"]
        ):
            user = User()
            user.login = user_seed["login"]
            user.salt = self.__generate_salt_key()
            hashed_password = self.__hash_password(
                password=user_seed["pass"], salt=user.salt
            )
            user.password = hashed_password
            self.users_repository.save(user=user)
            return user
        return None

    def check_token(self, headers: list) -> User:
        token = None
        if "x-access-tokens" in headers:
            token = headers["x-access-tokens"]

        if not token:
            raise ValueError("token_missing")

        try:
            data = jwt.decode(jwt=token, key=self.SECRET_KEY, algorithms="HS256")
            user = self.users_repository.get_by_login(data["user"])
            if user is None:
                raise ValueError("invalid_user")
            return user
        except Exception as error:
            raise ValueError("invalid_token")

    def __generate_salt_key(self):
        return "".join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            for _ in range(10)
        )

    def __hash_password(self, password: str, salt: str):
        return generate_password_hash(password + salt, method="sha256")
