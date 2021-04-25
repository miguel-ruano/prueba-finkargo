from src.models import User

class UsersRepository:
    """
    Repositorio de usuarios del sistema
    """

    def save(self, user:User) -> User :
        if user != None:
            return user.save()
        return None

    def get_by_login(self, login:str) -> User :
        return User.objects(login = login).first()

    def exist_by_login(self, login:str) -> bool:
        return User.objects(login = login).first() != None
