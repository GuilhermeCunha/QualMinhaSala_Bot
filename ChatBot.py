import Funções
from Banco import Banco
from unidecode import unidecode  # Tirar acentos de uma string
import pymongo # Acessar banco de dados
#import sys # Descobrir qual o sistema operacional
#import subprocess as s # Não sei ainda

class Chatbot():
    def __init__(self, nome, banco):
        self.nome = nome
        self.banco = banco

    def escuta(self, frase=None):
        if frase == None:
            return 0

        frase = str(frase)
        frase = frase.lower()
        frase = unidecode(frase)
        return frase

    def pensa(self, primeiroNome, chatID, frase):
        if '/cadastrar' in frase:
            return "Escreva seu RA para cadastrar sua conta"
        if '/consultar' in frase:
            texto = str(frase)
            mensagem = texto.split(" ")
            return Funções.resposta(mensagem[1])
        if '162.' in frase:
            usuario = {'first_name': primeiroNome, 'chatid': str(chatID), 'ra': frase}
            if self.banco.acharUsuario(usuario):
                return "Conta já cadastrada"
            self.banco.inserirUsuario(usuario)
            return "Conta cadastrada com sucesso"
        if '/minhasala' in frase:
            ra = self.banco.acharRAporID(chatID)
            if ra:
                return Funções.resposta(ra)
            else:
                return "Conta não encontrada"
        if '/funcoes' in frase:
            return "/Cadastrar\n/Consultar\n192.\n/minhasala\n/contascadastradas"
        if '/contascadastradas' in frase:
            return self.banco.listarUsuarios()
        return 'Função não configurada'

    #def fala(self,chatID, frase):
