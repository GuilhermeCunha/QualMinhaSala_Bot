import Funções
#import Main
import sys # Descobrir qual o sistema operacional
from unidecode import unidecode  # Tirar acentos de uma string
import subprocess as s # Não sei ainda

class Chatbot():
    def __init__(self, nome):
        self.nome = nome

    def escuta(self, frase=None):
        if frase == None:
            return 0

        frase = str(frase)
        frase = frase.lower()
        frase = unidecode(frase)
        return frase

    def pensa(self, primeiroNome, chatID, frase):
        if 'teste' in frase:
            return "O teste funcionou"
        if '/cadastrar' in frase:
            return "Escreva seu RA para cadastrar sua conta"
        if '192.' in frase:
            conta = {'first_name': primeiroNome, 'chatid': str(chatID), 'ra': frase}
            #Adicionar conta ao banco
            return "Conta cadastrada com sucesso"
        if '/minhasala' in frase:
            #consultar se a conta está no banco de dados
            ra = 1 #Ra = consulta no banco do RA da pessoa que mandou a mensagem
            return Funções.resposta(ra)
        if '/contascadastradas' in frase:
            return 0 #Todas as contas cadastradas no banco
        return 'Função não configurada'

    #def fala(self,chatID, frase):
