from Banco import Banco
import ChatBot
import Funções
banco = Banco()
#usuario = {'first_name': "Gabriel", 'chatid': "123456789", 'ra': "192.123456"}
#banco.inserirUsuario(usuario)
#print(banco.numeroUsuarios())
#print(banco.listarUsuarios())
#print(banco.listarUsuarios())
lista = []
for aux in banco.Usuarios.find():
    print(aux['first_name'])
    lista.append(aux)
    print(aux)
print("\n")
print(lista[0]['ra'])

