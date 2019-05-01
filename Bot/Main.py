# encoding: utf-8
from unidecode import unidecode
import telepot
import requests
from datetime import datetime
from pytz import timezone
import time
import json

bot_token = '823857629:AAFwWPAHsYANt6Za3bZcYFazY1-Cof7kxNw'
telegram = telepot.Bot(bot_token)

def resposta(ra):
    try:
        url = "http://senaiweb.fieb.org.br/MinhaAula/api/aulas?ra=" + ra
        objeto = requests.get(url).json()
    except:
        return ("Algum erro ocorreu, confira seu RA")

    nomeProfessor = objeto[0]['professor']
    turno = objeto[0]['turno']
    codTurma = objeto[0]['codTurma']
    dtInicial = objeto[0]['dtInicial']
    dtFinal = objeto[0]['dtFinal']
    curso = unidecode(objeto[0]['curso'])
    disciplina = objeto[0]['disciplina']
    predio = objeto[0]['predio']
    bloco = objeto[0]['bloco']
    sala = objeto[0]['sala']
    data = objeto[0]['data']
    horaInicial = objeto[0]['horaInicial']
    horaFinal = objeto[0]['horaFinal']

    nomeCurso = curso + '\n'

    if 'Tecnico em Manutencao Automotiva' in curso:
        retorno = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
    if 'Tecnico em Desenvolvimento de Sistemas' in curso:
        retorno = bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
    if 'Tecnico em Eletrotecnica' in curso:
        retorno = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
        resp = (nomeCurso + retorno)

    if len(objeto) == 2:
        retorno = ""
        nomeProfessor = objeto[1]['professor']
        turno = objeto[1]['turno']
        codTurma = objeto[1]['codTurma']
        dtInicial = objeto[1]['dtInicial']
        dtFinal = objeto[1]['dtFinal']
        curso = unidecode(objeto[1]['curso'])
        disciplina = objeto[1]['disciplina']
        predio = objeto[1]['predio']
        bloco = objeto[1]['bloco']
        sala = objeto[1]['sala']
        data = objeto[1]['data']
        horaInicial = objeto[1]['horaInicial']
        horaFinal = objeto[1]['horaFinal']

        if 'Tecnico em Manutencao Automotiva' in curso:
            retorno2 = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
        if 'Tecnico em Desenvolvimento de Sistemas' in curso:
            retorno2 = bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
        if 'Tecnico em Eletrotecnica' in curso:
            retorno2 = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal

        resp = (resp + "\n\n " + retorno2)

    return resp


def pegaHorario():
    data_e_hora_atual = datetime.now()
    horaAtual = data_e_hora_atual.strftime('%H:%M')

    if horaAtual == "00:00":
        return True


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

