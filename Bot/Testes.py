# encoding: utf-8
from unidecode import unidecode
import telepot
import requests
from datetime import datetime
from pytz import timezone
import time
import json
import subprocess as s

class Usuario:
    def __init__(self, username, chatid, ra):
        self.username = username
        self.chatid = chatid
        self.ra = ra
us = Usuario("Guilherme", 123, 123456789)

Usuarios = []
usuario1 = {}
usuario2 = {}
usuario3 = {}
usuario1 = {'username': str(us.username),'chatid': str(us.chatid), 'ra': str(us.ra)}
usuario2 = {'username': "Gabriel",'chatid': "456", 'ra': "123456789"}
usuario3 = {'username': "Vita",'chatid': "789", 'ra': "123456789"}
usuario4 = {'username': "Issa",'chatid': "789", 'ra': "123456789"}
Usuarios = []
Usuarios.append(usuario1)
Usuarios.append(usuario2)

#Usuarios.append(u2)
#Usuarios.append(u3)


with open('Usuarios.json', 'w') as arquivo:
    json.dump(Usuarios, arquivo)
'''    
with open('Usuarios.json', 'a') as arquivo:
    arquivo.write("\nteste")
'''


with open('Usuarios.json', 'r') as arquivo:
    Usuarios = json.load(arquivo)
    print(Usuarios)
    print(len(Usuarios))
Usuarios.append(usuario3)
with open('Usuarios.json', 'w') as arquivo:
    json.dump(Usuarios, arquivo)

with open('Usuarios.json', 'r') as arquivo:
    Usuarios = json.load(arquivo)
    print(Usuarios)
    print(len(Usuarios))
chatID = 1234
i=0
while i < len(Usuarios):
    if str(chatID) in Usuarios[i]['chatid']:
        print("DEU CERTO")
    i +=1


