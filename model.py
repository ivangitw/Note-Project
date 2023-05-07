class User:
    def __init__(self,
                 login,
                 password):
        self.__login = login
        self.__password = password
        
    @property
    def login(self):
        return self.__login

    def check_data(self,
                   login,
                   password):
        if self.__login == login and self.__password == password:
            return True
        else:
            return False


