from Banco import Banco
import ChatBot
import Funções
from datetime import datetime
from datetime import date
from pytz import timezone
banco = Banco()

#banco.inserirUsuario(usuario)
#print(banco.numeroUsuarios())
#print(banco.listarUsuarios())
#print(banco.listarUsuarios())
#lista = []
#for aux in banco.Usuarios.find():
 #   print(aux['first_name'])
  #  lista.append(aux)
   # print(aux)
#print("\n")
#banco.inserirUsuario(usuarioTeste)
usuarioTeste = {'first_name': "teste", 'chatid': "123456789", 'ra': "192.123456"}
usuario = {'chatid': "802306258"}

horario = Funções.pegaHorario()
dia = Funções.pegaDia()

if horario == "14:53":

    for aux in banco.Usuarios.find():
        usuario = {'chatid': aux['chatid']}
        print(aux['first_name'] )
        #print("US:" + str(usuario))
        #print(aux)
        if not banco.verifMensagensAutomaticasDesativadas(usuario):
            chatid = aux['chatid']
            ra = aux['ra']

            print(Funções.resposta(ra))
            print("\n")
        else:
            print("mensagem não enviada\n")

#print(banco.listarUsuarios())


