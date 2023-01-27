from enum import StrEnum

class PasswordError(StrEnum):
    PASSWORD_LENGTH_ERROR = "password must be mor than 7 'character'."
    PASSWORD_TYPE_ERROR = "password must be 'number' and 'character'. "
    PASSWORD_CHECK = "wrong password"

class UserNameError(StrEnum):
    USERNAME_TYPE_ERROR = "username must be 'string'."
    USERNAME_CHARACTER_ERROR = "username must be started by character."
    USER_NAME_CHECK = "username dose not exist"

class PhoneError(StrEnum):
    PHONE_TYPE_ERROR = "phone must be 'number'."
    PHONE_NUMBER_ERROR = "the first number must be '0'."
    PHONE_LENGTH_ERROR = "the phone number must be include '11' number"

class HELP(StrEnum):
    HELP_LIST = ("for search use search's key"'\n'
        "for edit list use edit's key"'\n'
        "for remove items from list use remove's key"'\n'
        "for exit the list use exit's key"'\n'
    )