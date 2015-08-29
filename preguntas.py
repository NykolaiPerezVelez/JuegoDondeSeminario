#Sigo probando como sincronizar con kananize  #taskid 19
#Creo clase Pregunta
class Pregunta():


#Constructor para clase Pregunta
    def __init__(self, idPre, pre, res, lon, la):
        self.idPre = idPre
        self.pre = pre
        self.res = res
        self.lon = lon
        self.la = la


#Mostrar Preguntas
    def MostrarPreguntas(self):
        print((self.idPre))
        print((self.pre))
        print((self.res))
        print((self.lon))
        print((self.la))



