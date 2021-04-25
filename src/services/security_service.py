from src.repositories import UsersRepository


class SecurityService:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    def authenticate(self, user_login: str, user_password: str):
        user = self.users_repository.get_by_login(user_login)
        if user != None:
            return "ok"
        return None
