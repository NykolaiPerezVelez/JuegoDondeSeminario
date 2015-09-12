#Creo clase Usuario
class Usuario():


#Constructor para clase Usuario
    def __init__(self, idUsuario, nombreUsuario, neuronasUsadas, mejorPuntaje):
        self.idUsuario = idUsuario
        self.nombreUsuario = nombreUsuario
        self.neuronasUsadas = neuronasUsadas
        self.mejorPuntaje = mejorPuntaje


#Mostrar Usuario
    def MostrarUsuarios(self):
        print((self.idUsuario))
        print((self.nombreUsuario))
        print((self.neuronasUsadas))
        print((self.mejorPuntaje))






