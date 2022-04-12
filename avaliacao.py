class Avaliacao:
    def __init__(self, id, nome, nota, comentario, restaurante):
        self.__id = id
        self.__nome = nome
        self.__nota = nota
        self.__comentario = comentario
        self.__restaurante = restaurante

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getNota(self):
        return self.__nota

    def getComentario(self):
        return self.__comentario

    def getRestaurante(self):
        return self.__restaurante