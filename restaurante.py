class Restaurante:
    def __init__(self, id, nome, endereco, telefone, tipo, horarioAbertura, horarioFechamento, img):
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__tipo = tipo
        self.__horarioAbertura = horarioAbertura
        self.__horarioFechamento = horarioFechamento
        self.__img = img
        self.__avaliacoes = []

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getTelefone(self):
        return self.__telefone

    def getTipo(self):
        return self.__tipo

    def getAvaliacao(self):
        return self.__avaliacao

    def getHorarioAbertura(self):
        return self.__horarioAbertura

    def getHorarioFechamento(self):
        return self.__horarioFechamento

    def getImg(self):
        return self.__img

    def setAvaliacao(self, avaliacao):
        self.__avaliacoes.append(avaliacao)

    def getAvaliacoes(self):
        return self.__avaliacoes

    def getUrlNome(self):
        self.__urlNome = self.__nome.replace(" ", "")
        return self.__urlNome

a = 'Reliquia Restaurante'
b = a.split()
c = ''.join(b)
print(c)
print(a.replace(" ", ""))

