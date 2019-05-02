# encoding: utf-8
#Não usados
from pytz import timezone
import time

#from unidecode import unidecode
import telepot
#import requests
from datetime import datetime
import json
import ChatBot





bot_token = '823857629:AAFwWPAHsYANt6Za3bZcYFazY1-Cof7kxNw'
chat_bot = ChatBot.Chatbot("Guilherme")
telegram = telepot.Bot(bot_token)







#Usuarios = [{"username": "ADM", "chatid": "ADM", "ra": "ADM"}]
def recebendoMsg(msg):
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    try:
        Usuarios = Usuarios = json.load(open('Usuarios.json', 'r'))
    except:
        Usuarios = []

    updates = telegram.getUpdates()
    primeiroNome = updates[-1]['message']['from']['first_name']
    frase = msg['text']
    if '/start' in frase:
        telegram.sendMessage(chatID, "Seja bem vindo ao MinhaAula!\n Digite seu RA para começar")
    if '162.' in frase:
        #print(len(Usuarios))
        if len(Usuarios) != 0:
            Usuarios = json.load(open('Usuarios.json', 'r'))
            #print("USUARIO CARREGADO")

        usuariojson = {'first_name': primeiroNome, 'chatid': str(chatID), 'ra': frase}
        Usuarios.append(usuariojson)
        #print(len(Usuarios))
        with open('Usuarios.json', 'w') as arquivo:
            json.dump(Usuarios, arquivo)
            arquivo.close()
        i=0
        while i < len(Usuarios):
            if str(chatID) in Usuarios[i]['chatid']:
                telegram.sendMessage(chatID, "Sua conta já está cadastrada no JSON")
                break
            i += 1

    if '/consultarUsuarios' in frase:
        with open('Usuarios.json', 'r') as arquivo:
            Usuarios = json.load(arquivo)
            arquivo.close()
        i = 0
        #telegram.sendMessage(chatID, str(len(Usuarios)))
        while i < len(Usuarios):
            telegram.sendMessage(chatID,
                                 "\nPrimeiro nome: " + Usuarios[i]['first_name'] + "\nChatID: " + str(Usuarios[i]['chatid']) + "\nRA: " +
                                 str(Usuarios[i]['ra']))
            i += 1
    if '/minhasala' in frase:
        Usuarios = Usuarios = json.load(open('Usuarios.json', 'r'))
        i=0
        while i < len(Usuarios):
            if primeiroNome == Usuarios[i]['first_name']:
                #print(Usuarios[i]["ra"])
                telegram.sendMessage(chatID, resposta(Usuarios[i]["ra"]))
                break
            i += 1

telegram.message_loop(recebendoMsg)
while True:
    pass
    #if Usuarios:
        #pass
        # Colocar parte de enviar mensagem no horário

