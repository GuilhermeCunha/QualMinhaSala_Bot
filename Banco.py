from pymongo import MongoClient

class Banco():
    def __init__(self):
        self.MONGO_HOST = "10a.mongo.evennode.com:27017"
        self.MONGO_HOST = "10a.mongo.evennode.com:27017"
        self.MONGO_PORT = 27017
        self.MONGO_DB = "02d80ae80ce3255cd96fd877831d6649"
        self.MONGO_USER = "02d80ae80ce3255cd96fd877831d6649"
        self.MONGO_PASS = "00280900"
        self.connection = MongoClient(self.MONGO_HOST, self.MONGO_PORT)
        self.db = self.connection[self.MONGO_DB]
        self.db.authenticate(self.MONGO_USER, self.MONGO_PASS)
        self.Usuarios = self.db.get_collection("Usuarios")
        self.MensagensDesativadas = self.db.get_collection("MensagensDesativadas")

    def desativarMensagensAutomaticas(self, usuario):
        usuarioCompleto = 0
        for us in self.Usuarios.find(usuario):
            usuarioCompleto = us
        if usuarioCompleto != 0:
            self.MensagensDesativadas.insert_one(usuarioCompleto)
            return True
        return False
    def ativarMensagensAutomaticas(self, usuario):
        usuarioCompleto = 0
        for us in self.Usuarios.find(usuario):
            usuarioCompleto = us
        if usuarioCompleto != 0:
            self.MensagensDesativadas.delete_one(usuarioCompleto)
            return True
        return False

    def removerUsuario(self, usuario):
        try:
            for aux in self.Usuarios.find(usuario):
                print(aux)
                id = aux['_id']
                self.Usuarios.remove({'_id': id})
                return True
            else:
                return False
        except:
            return "Error"

    def inserirUsuario(self, novoUsuario):
        try:
            for us in self.Usuarios.find(novoUsuario):
                return False
            self.Usuarios.insert_one(novoUsuario)
            return True
        except:
            return "Error"
    def verifMensagensAutomaticasDesativadas(self, usuario):
        try:
            for us in self.MensagensDesativadas.find(usuario):
                return True
            return False
        except:
            print("Error")
            return

    def acharUsuario(self, usuario):
        for us in self.Usuarios.find(usuario):
            return us
        return False

    def acharRAporID(self, id):
        id = str(id)
        chatid= {'chatid': id}
        for us in self.Usuarios.find(chatid):
            return us['ra']

        return False
    def apagarCollection(self):
        self.db.drop_collection("Usuarios")

    def numeroUsuarios(self):
        return self.Usuarios.estimated_document_count()
    def listarUsuarios(self):
        lista = []
        i=0
        while i < self.numeroUsuarios():
            Usuario = self.Usuarios.find()[i]
            nome = str(Usuario['first_name'])
            chatID = str(Usuario['chatid'])
            ra = str(Usuario['ra'])
            if not self.verifMensagensAutomaticasDesativadas(Usuario):
                mensagensAutomaticas = "Ativado"
            else:
                mensagensAutomaticas = "Desativado"
            info = "Nome: " + nome + "\n" + "ChatID: " + chatID + "\n" + "RA: " + ra + "\n" + "Mensagens Automáticas: "+ mensagensAutomaticas + "\n\n"
            lista.append(info)
            i += 1
        i=0
        texto = ""
        while i<len(lista):
            texto += lista[i]
            i += 1
        return texto



    #resultado = Usuarios.insert_one(usuario)
    #for us in Usuarios.find():
     #   print(usuario.get('first_name'))
    '''
    nomeUsuario = str(usuario2['first_name'])
    print(Usuarios.estimated_document_count())
    
    for us in Usuarios.find(usuario2):
        achei = us.get('first_name')
    print(achei)
    #print(resultado)
    '''
