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

    def inserirUsuario(self, novoUsuario):
        try:
            for us in self.Usuarios.find(novoUsuario):
                return False
            self.Usuarios.insert_one(novoUsuario)
            return True
        except:
            return "Error"
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
            nome = str(self.Usuarios.find()[i]['first_name'])
            chatID = str(self.Usuarios.find()[i]['chatid'])
            ra = str(self.Usuarios.find()[i]['ra'])
            info = "Nome: " + nome + "\n" + "ChatID: " + chatID + "\n" + "RA: " + ra + "\n\n"
            lista.append(info)
            i += 1
        i=0
        texto = ""
        while i<len(lista):
            texto += lista[i]
            i += 1
        return texto
        return True



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
