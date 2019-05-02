import telepot
import ChatBot

bot_token = '823857629:AAFwWPAHsYANt6Za3bZcYFazY1-Cof7kxNw'
bot = ChatBot.Chatbot("CHATBOT")
telegram = telepot.Bot(bot_token)

def recebendoMsg(msg):
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    updates = telegram.getUpdates()
    primeiroNome = updates[-1]['message']['from']['first_name']

    frase = bot.escuta(frase=msg['text'])

    if frase != 0:
        resposta = bot.pensa(primeiroNome, chatID, frase)
        telegram.sendMessage(chatID, resposta)


telegram.message_loop(recebendoMsg)
while True:
    pass
    #Acrescentar função de envio de mensagem automática ao chegar no horário