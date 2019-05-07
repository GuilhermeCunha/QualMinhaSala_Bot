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

        if '/start' == frase:
            return "Seja bem vindo ao MinhaAula!\n Digite seu RA para finalizar a criação da sua conta!"

        if '/consultar' in frase:
            texto = str(frase)
            mensagem = texto.split(" ")
            return Funções.resposta(mensagem[1])

        if '162.' in frase and len(frase) == 10:
            usuario = {'first_name': primeiroNome, 'chatid': str(chatID), 'ra': frase}
            if self.banco.acharUsuario(usuario):
                return "Conta já cadastrada"
            self.banco.inserirUsuario(usuario)
            return "Conta cadastrada com sucesso\n\nOBS: Estou configurado para enviar mensagens automáticas avisando onde será a sua aula às 12:00 de todos os dias da semana, caso queira saber mais sobre a ativação/desativação deste serviço, escreva: /sabersobremensagens\n\nPara saber quais as funções disponíveis, escreva: /comandos"
        if '/sabersobremensagens' == frase:
            return "Ao cadastrar uma conta em meu sistema, estou configurado para te enviar onde será sua sala em todos os dias úteis da semana às 12:00.\n\n" \
                   "Caso queira desabilitar este serviço, e quem sabe reativálo futuramente, consulte o comando: /comandos."
        if '/minhasala' == frase:
            ra = self.banco.acharRAporID(chatID)
            if ra:
                return Funções.resposta(ra)
            else:
                return "Conta não encontrada"

        if '/desativarmensagensautomaticas' == frase:
            usuario = {'first_name': primeiroNome, 'chatid': str(chatID)}
            if self.banco.desativarMensagensAutomaticas(usuario):
                return "Você não receberá mais mensagens automáticas"
            else:
                return "Algum erro ocorreu"

        if '/ativarmensagensautomaticas' == frase:
            usuario = {'first_name': primeiroNome, 'chatid': str(chatID)}
            print(usuario)
            if self.banco.ativarMensagensAutomaticas(usuario):
                return "As suas mensagens automáticas estão habilitadas!"
            else:
                return "Algum erro ocorreu"

        if '/comandos' == frase:
            return "/minhasala   Para receber onde será a sua sala" \
                   "\n/consultar <RA>   Para consultar a sala de um RA não vinculado a conta" \
                   "\n/descadastrar   Para remover a sua conta do nosso sistema" \
                   "\n/criadopor   Para saber quem é meu criador"\
                   "\n/desativarmensagensautomaticas   Para desativar as mensagens automáticas às 12:00"\
                   "\n/ativarmensagensautomaticas   Para ativar as mensagens automáticas às 12:00"

        if '/contascadastradas' == frase:
            return self.banco.listarUsuarios()

        if '/descadastrar' == frase:
            usuario = {'chatid': str(chatID)}
            print(usuario)
            if self.banco.removerUsuario(usuario):
                self.banco.ativarMensagensAutomaticas(usuario)
                return "Conta deletada com sucesso"
            return "Esta conta não foi encontrada"

        if '/criadopor' == frase:
            return "Criador"

        return

