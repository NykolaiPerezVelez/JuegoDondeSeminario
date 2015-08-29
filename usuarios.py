#Creo clase Usuario
class Usuario():


#Constructor para clase Usuario
    def __init__(self, idUsuario, nombreUsuario, mejorPuntaje, neuronasUsadas):
        self.idUsuario = idUsuario
        self.nombreUsuario = nombreUsuario
        self.mejorPuntaje = mejorPuntaje
        self.neuronasUsadas = neuronasUsadas


#Mostrar Usuario
    def MostrarUsuarios(self):
        print((self.idUsuario))
        print((self.nombreUsuario))
        print((self.mejorPuntaje))
        print((self.neuronasUsadas))






