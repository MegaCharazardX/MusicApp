import re

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

gmail = RegEx(input("Enter Gmail Address : "))
print(gmail.IsGmailValid())