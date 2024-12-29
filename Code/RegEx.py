import re
from DBConfig import DBOperation

VALID = "Valid"
INVALID = "Invalid"

class RegEx:
    def __init__(self, string, RegularExpresion = re.compile(r"^\b[a-zA-Z0-9]+@[a-z]+.[a-z]\b")):
        self.string = string
        self.RegularExpresion = RegularExpresion
        self.ismatch = self.RegularExpresion.match(self.string)
        
    def IsGmailValid(self):
        if self.ismatch is None:
            return False
        else:
            return True
        
    def IsPasswordStrong(self, password):
        """
            At least 8 characters long.
            Contains at least one uppercase letter (A-Z).
            Contains at least one lowercase letter (a-z).
            Contains at least one digit (0-9).
            Contains at least one special character (@#$%^&*! or others).
            Must not contain or be a combination of variations of the word "password"
        """
        self.__PasswordRegEx = re.compile(r"^(?!.*([Pp][Aa@][Ss$5][Ss$5][Ww][Oo0][Rr][Dd])).(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]{8,}$")
        if re.match(self.__PasswordRegEx, password):
            return "Strong Password"
        else:
            return "Weak Password"
        
        
gmail = RegEx(input("Enter Gmail Address : "))
print(gmail.IsPasswordStrong("password"))