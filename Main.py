import telepot
import ChatBot
from Banco import Banco
from Funções import pegaHorario
from Funções import resposta
import time

bot_token = '823857629:AAFwWPAHsYANt6Za3bZcYFazY1-Cof7kxNw'
banco = Banco()
bot = ChatBot.Chatbot("CHATBOT", banco)
telegram = telepot.Bot(bot_token)

def recebendoMsg(msg):
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    updates = telegram.getUpdates()
    primeiroNome = updates[-1]['message']['from']['first_name']

    frase = bot.escuta(frase=msg['text'])

    if frase != 0:
        resposta = bot.pensa(primeiroNome, chatID, frase)
        if(resposta == "Criador"):
            telegram.sendMessage(chatID, "*Guilherme Cunha*\n_Aluno de Desenvolvimento de Sitemas do SENAI CIMATEC_",
                                 parse_mode='Markdown')
            telegram.sendContact(chatID, "5571992711726", "Guilherme", "Cunha", disable_notification=None,
                                 reply_to_message_id=None, reply_markup=None)
        else:
            telegram.sendMessage(chatID, resposta)

telegram.message_loop(recebendoMsg)

while True:
    horario = pegaHorario()
    if horario == "12:00":
        for aux in banco.Usuarios.find():
            chatid = aux['chatid']
            ra = aux['ra']
            telegram.sendMessage(chatid, "-Aviso Automático-\n" + resposta(ra))
        time.sleep(60)