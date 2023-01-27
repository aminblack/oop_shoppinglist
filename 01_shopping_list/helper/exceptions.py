from .messages import (PasswordError,
UserNameError,
PhoneError
)



class WrongUserNameException(ValueError):
    def __str__(self):
        return UserNameError.USERNAME_CHARACTER_ERROR

class TypeUserNameException(TypeError):
    def __str__(self):
        return UserNameError.USERNAME_TYPE_ERROR

class CheckUsernameException(TypeError):
    def __str__(self):
        return UserNameError.USER_NAME_CHECK

class WrongPassWordException(ValueError):
    def __str__(self):
        return PasswordError.PASSWORD_LENGTH_ERROR

class TypePassWordException(TypeError):
    def __str__(self):
        return PasswordError.PASSWORD_TYPE_ERROR

class CheckPasswordException(TypeError):
    def __str__(self):
        return PasswordError.PASSWORD_CHECK

class TypePhoneException(TypeError):
    def __str__(self):
        return PhoneError.PHONE_TYPE_ERROR

class WrongPhoneNumberException(ValueError):
    def __str__(self):
        return PhoneError.PHONE_NUMBER_ERROR

class WrongPhoneLengthException(ValueError):
    def __str__(self):
        return PhoneError.PHONE_LENGTH_ERROR

