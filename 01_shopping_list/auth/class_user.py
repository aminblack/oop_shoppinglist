from helper.exceptions import(
    WrongUserNameException,
    TypeUserNameException,
    WrongPassWordException,
    TypePassWordException,
    TypePhoneException,
    WrongPhoneNumberException,
    WrongPhoneLengthException,
    CheckUsernameException,
    CheckPasswordException
)

class Users:

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name},{self.username},{self.password})'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeUserNameException()
        if not value[0].isalpha():
            raise WrongUserNameException()
        self.__username = value

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypePassWordException("password must be 'string'.")
        if len(value) < 8:
            raise WrongPassWordException()
        if value.isnumeric():
            raise TypePassWordException()
        self.__password = value

class Customers(Users):

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str):
            raise TypeError("phone must be 'string'.")
        if not value.isnumeric():
            raise TypePhoneException()
        if not value[0] == '0':
            raise WrongPhoneNumberException()
        if len(value) < 11:
            raise WrongPhoneLengthException()
        self.__phone = value

    def login(self, username, password):
        ch_us = self.check_username(username)
        ch_pa = self.check_password(password)
        if not ch_us == True:
            raise CheckUsernameException()
        if not ch_pa == True:
            raise CheckPasswordException()
        return "ok"

    def register(self, username:str, password:str, phone:str)-> None:
        self.username = username
        self. password = password
        self.phone = phone

    @staticmethod
    def read_username_password():
        with open('users.txt', 'r') as us:
            user_password = us.readlines()
            return user_password

    def check_username(self, username):
        return True if (username + '\n') in self.read_username_password() else False

    def check_password(self, password):
        return True if (password + '\n') in self.read_username_password() else False






