from pygame import mixer
import random
from DBConfig import DBOperation

mixer.init()

randomsong = random.randint(1, 115)
result = DBOperation().Select("Music", f"MID = {randomsong} AND MPath LIKE '%.mp3' ", "MPath")
rowset =[]
for i in result:
    print(i)
    rowset.append(i[0])
    
print(rowset)    
mixer.music.load(rowset[0])
mixer.music.play()
input()
mixer.music.stop