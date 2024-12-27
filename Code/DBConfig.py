import os
import sqlite3

Dir = "E:/Dhejus/Songs"

class DBConfig:
    def __init__(self):
        self.SelectQuery = "SELECT {} FROM {}"
        self.UpdateQuery = "UPDATE {} SET {}"
        self.con = sqlite3.connect("MusicPlayerDataBase.db")
        self.cur = self.con.cursor()

    def initDB(self):
        
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS "UserDetails" 
                            (
                                "UID"	INTEGER NOT NULL UNIQUE,
                                "UName"	NUMERIC UNIQUE,
                                "UGmail"	INTEGER,
                                "UDOB"	Date NOT NULL,
                                "UPassword"	TEXT NOT NULL,
                                "UIsAdmin"	INTEGER NOT NULL DEFAULT 0,
                                "UIsActive"	INTEGER NOT NULL DEFAULT 0,
                                "UFName"	TEXT,
                                "ULName"	TEXT,
                                PRIMARY KEY("UID" AUTOINCREMENT)
                            );
                        """)
        
        self.cur.execute("""
                            CREATE TABLE "Music" 
                            (
                                "MID"	INTEGER NOT NULL UNIQUE,
                                "MName"	INTEGER,
                                "MPath"	INTEGER,
                                PRIMARY KEY("MID" AUTOINCREMENT)
                            );
                        """)
        
    def ScanForMusic(self, Dir = r"E:/Dhejus/Songs"):
        for root, _ , files in os.walk(Dir):
            for file in files :
                print(file)
                if file.endswith((".mp3", ".wav", "m4a")):
                    file_path = os.path.join(root, file)
                    title = os.path.splitext(file)[0]
                    self.cur.execute("INSERT INTO Music (MName, MPath) VALUES(?, ?)", (title, file_path))
        self.con.commit()            
                
    def Select(self, Table, Condition = "", Feilds = "*"):
        if Condition :
            tempSelectQuery = self.SelectQuery + " WHERE {}"
            tempQry = tempSelectQuery.format(Feilds, Table, Condition)
            print(tempQry)
            result = self.cur.execute(tempQry)
            for i in result:
                print(i)
        else:
            tempQry = self.SelectQuery.format(Feilds, Table)
            result = self.cur.execute(tempQry)
            for i in result:
                print(i)
    
    def Update(self, Table, assignment, Condition = ""):
        if Condition:
            tempUpdateQuery = self.UpdateQuery + " WHERE {}"
            tempQuery = tempUpdateQuery.format(Table,assignment, Condition)
            self.cur.execute(tempQuery)
        else: 
            tempQuery = self.SelectQuery.format(Table, assignment )
            self.cur.execute(tempQuery)
            
                
        
DBConfig().Select(Table="Music")                  

    