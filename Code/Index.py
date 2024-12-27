from customtkinter import *
from pygame import mixer
import Stack
import random
import RegEx
import Crypter
import DBConfig

class User:
    def __init__(self, _User = "", IsAdmin = False, IsSignedIn = False):
        self.__User = _User
        self.IsAdmin = IsAdmin
        self.IsSignedIn = IsSignedIn
        
    def isAdmin(self):
        if self.IsAdmin == True :
            return True
        else:
            return False
        
    def isSignedIn(self):
        if self.IsAdmin == True :
            return True
        else:
            return False
    
    def User(self):    
        if self.__User != "":
            return self.__User
        else:
            return None
            
class App(CTk):
    
    def __init__(self):
        super().__init__()
        
        #=-=-=-=-=-=-=VARIABLES=-=-=-=-=-=-=-==
        AppUser = User("HariDhejus", True, False)
        print(AppUser.isAdmin())
        
        #=-=-=-=-=-=-=CTk-INIT=-=-=-=-==-=-=-=
        set_appearance_mode("dark")
        self.title("Music Player")
        self.geometry("400x600")
        self.iconbitmap(r"Icons\favicon (1).ico")
        
        #=-==-=-=-=-=-=PROGRAM-=-=-=-=-=-=-=-=
        self.__headerFrame = CTkFrame(self)
        self.__headerFrame.place(relx =0 , rely = 0, relwidth = 1, relheight = 0.1)
        
        self.__progressBar = CTkProgressBar(self.__headerFrame, width = 100, height=2, progress_color="skyblue")
        self.__progressBar.place(relx =0.25, rely = 1, relwidth = .5, relheight = .02)
        
    
    def Header(self):
        self.headerFrame = CTkFrame(self, fg_color="skyblue")
        self.headerFrame.place(relx = 0.25, rely = 0.25, relwidth = 1, relheight = 0.2)

if __name__ == "__main__":
    App().mainloop()