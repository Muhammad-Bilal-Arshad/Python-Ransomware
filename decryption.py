import os
from cryptography.fernet import Fernet
os.chdir('E:\VALO\Riot Games\Riot Client')
files =[]
for file in os.listdir():
    if file == "main.py" or file =="thekey.key" or file == "main2.py" or file =="RiotClientCrashHandler.exe":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)
os.chdir('H:\EH')
#pening keyfile reading it and storing it inside a variable
with open("thekey.key","rb") as key:
    secretkey = key.read()
os.chdir('E:\VALO\Riot Games\Riot Client')
#decrypting files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open (file, "wb") as thefile:
            thefile.write(contents_decrypted)