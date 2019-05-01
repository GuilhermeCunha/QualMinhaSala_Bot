# encoding: utf-8
from unidecode import unidecode
import telepot
import requests
from datetime import datetime
from pytz import timezone
import time

bot_token = '823857629:AAFwWPAHsYANt6Za3bZcYFazY1-Cof7kxNw'
telegram = telepot.Bot(bot_token)


class Usuario():
    def __init__(self, chatID):
        self.chatID = chatID
        self.ra = None

    def addRa(self, ra):
        self.ra = ra

    def getchatid(self):
        return self.chatID

def resposta(ra):
    try:
        url = "http://senaiweb.fieb.org.br/MinhaAula/api/aulas?ra=" + ra
        objeto = requests.get(url).json()

        Desenvolvimento = 'Técnico em Desenvolvimento de Sistemas'
        Eletrotecnica = 'Técnico em Eletrotécnica'
        Manutencao = 'Técnico em Manutenção Automotiva'

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

        return resp
    except:
        return ("Algum erro ocorreu, confira seu RA")

Usuarios = []
RAs = []
def recebendoMsg(msg):
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    frase = msg['text']
    data_e_hora_atual = datetime.now()
    horaAtual = data_e_hora_atual.strftime('%H:%M')
    primeiroAcesso = True
    if chatID in Usuarios:
        primeiroAcesso = False

    if primeiroAcesso == True:
        telegram.sendMessage(chatID, "ID Cadastrado\nAgora digite seu RA para concluir o cadastro")
        Usuarios.append(chatID)
        i = 0
        primeiroAcesso = False

    if '162.' in frase and len(frase) == 10:
        RAs.append(frase)
        telegram.sendMessage(chatID, "RA cadastrado\n Escreva /comousar para saber como o sistema funciona")
    #if 'horario' in frase:
        #dataUTC = datetime.now(timezone('UTC'))
        #dataBahia = dataUTC.astimezone(timezone('America/Bahia'))
        #horaBahia = dataBahia.strftime('%H:%M')
        #telegram.sendMessage(chatID, horaBahia)

    if 'consultarconta' in frase:
        cont = 0
        while cont < len(Usuarios):
            if chatID == Usuarios[cont]:
                telegram.sendMessage(chatID,"ChatID: " + str(Usuarios[cont]) + "\nRA: " + RAs[cont])
                break
            cont += 1

    if '/cadastrarhorario' in frase:
        cont = 0
        while cont < len(Usuarios):
            if chatID == Usuarios[cont]:
                break
            cont += 1
        mensagem = str(frase)
        texto = mensagem.split(" ")
        dias = int(texto[2])
        telegram.sendMessage(chatID, "Você receberá onde será a sua sala às " + texto[1] + " durante os próximos " + texto[2] + " dias.")

        dataUTC = datetime.now(timezone('UTC'))
        dataBahia = dataUTC.astimezone(timezone('America/Bahia'))
        horaBahia = dataBahia.strftime('%H:%M')

        while horaBahia != texto[1]:
            dataUTC = datetime.now(timezone('UTC'))
            dataBahia = dataUTC.astimezone(timezone('America/Bahia'))
            horaBahia = dataBahia.strftime('%H:%M')

        contDias = 0
        while(contDias < dias):
            telegram.sendMessage(chatID, resposta(RAs[cont]))
            time.sleep(86400)
            contDias += 1


    if 'Bom dia' in frase:
        resp = "Ótimo dia para nós!"
    if '/comousar' in frase:
        resp = "A utilização é bem simples, para saber qual o local da sua sala basta escrever /minhasala ou clicar no comando /minhasala para obter " \
               "a informação!\nSe pretende consultar a sala de alguma outra pessoa, basta digitar consultar e o RA da pessoa " \
               "ex: consultar 123.456789" \
               "\nCaso queira predefinir um horário específico para receber onde será a sua aula escreva /avancado para saber mais!"
    if '/avancado' in frase:
        resp = "Para configurar um horário específico, você devera informar um horário e a quantidade de dias que esse " \
               "horário será utilizado. Por exemplo, se você quiser ser notificado as 11:00 dos próximos 5 dias, escreva: " \
               "/cadastrarhorario 11:00 5\nObs: Ao configurar um horário/quantidade de dias específos, você não poderá " \
               "executar outros comandos como : /desenvolvidopor, /contato ... etc"

    if 'consultar' in frase:
        mensagem = str(frase)
        texto = mensagem.split(" ")
        telegram.sendMessage(chatID, resposta(texto[1]))
    if '/contribuidores' in frase:
        resp = "Agradecimentos a Eduardo Correia e Felipe Bastos"
    if '/desenvolvidopor' in frase:
        telegram.sendMessage(chatID, "*Guilherme Cunha*\n_Aluno de Desenvolvimento de Sitemas_", parse_mode='Markdown')
        telegram.sendContact(chatID, "5571992711726", "Guilherme", "Cunha", disable_notification=None,
                             reply_to_message_id=None, reply_markup=None)
    if '/contato' in frase:
        telegram.sendContact(chatID, "5571992711726", "Guilherme", "Cunha", disable_notification=None,
                             reply_to_message_id=None, reply_markup=None)
    if '/minhasala' in frase:
        cont = 0
        while cont < len(Usuarios):
            if chatID == Usuarios[cont]:
                telegram.sendMessage(chatID, resposta(RAs[cont]))
                break
            cont += 1
    if '123.456789' in frase:
        resp = "CIMATEC X - Xº ANDAR na sala X"
    if 'Quem te criou?' in frase:
        resp = 'Guilherme Cunha, aluno de Desenvolvimento de Sistemas'

    telegram.sendMessage(chatID, resp)


#telegram.getUpdates()
telegram.message_loop(recebendoMsg)

while True:
    pass
