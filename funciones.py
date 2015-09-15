# Módulos
import pygame
from pygame.locals import *
from math import sqrt
from preguntas import *
from usuarios import *




###########################################################################
#Pre: Debe exitir un archivo llamado preguntas.txt en el directorio
#con el formato id,pregunta,longRespuesta, latrespuesta

#POST: Devuelve la cantidad de preguntas que hay en el archivo


#Cantidad de lineas de preguntas
def CantidadPreguntas():
        archi = open('preguntas.txt')
        cantidadPreguntasCargados = len(archi.readlines())
        cantPreguntas = cantidadPreguntasCargados
        archi.close()
        return cantPreguntas
###########################################################################




###########################################################################
#Pre:Debe exitir un archivo llamado preguntas.txt en el directorio
#con el formato id,pregunta,longRespuesta, latrespuesta

#POST: Carga las preguntas en una matri, preguntas[i][j]
# i es la pregunta, y j el atributo

#Recuperar usuarios desde archivo

def RecuperarPreguntas():
    import csv
    preguntas = []
    archivo = open("preguntas.txt", "r")
    archivo_csv = csv.reader(archivo)
    for idP, pre, lo, la in archivo_csv:
        preguntas.append((int(idP), pre, int(lo), int(la)))
    archivo.close()
    return preguntas
##########################################################################




###########################################################################
#Pre: conocer cantidad de preguntas, y tener cargadas las preguntas

#POST: devuelve una pregunta al azar

#OBS:entro con: CantidadPreguntas(),RecuperarPreguntas()
def AsignarPreguntaRandom(x,y):
        import random
        (idpre,pre,xres,yres)=(y[random.randrange(x)])
        return pre,xres,yres

#preAzar es la pregunta y long y lat
preAzar=AsignarPreguntaRandom(CantidadPreguntas(),RecuperarPreguntas())
##########################################################################




###########################################################################
#Pre: debe existir un archivo de usuarios con el nombre usuarios.txt...
# de la forma id, nombre, tiempo, puntos

#POST: devuelve la cantidad de usuarios cargados

def CantidadUsuarios():
        archi=open('usuarios.txt')
        cantidadUsuariosCargados = len(archi.readlines())
        cantUsuarios=cantidadUsuariosCargados
        archi.close()
        return cantUsuarios
##########################################################################




###########################################################################
#Pre: debe existir un archivo de usuarios con el nombre usuarios.txt...
# de la forma id, nombre, tiempo, puntos

#POST:  Carga los usuarios que ya han jugado en una matriz[]i[j]

def RecuperarUsuarios():
     import csv
     usuarios = []
     archivo = open("usuarios.txt", "r")
     archivo_csv = csv.reader(archivo)
     for idU,nombre,tiempo,puntos in archivo_csv:
         usuarios.append((int(idU),nombre,int(tiempo),int(puntos)))
     archivo.close()
     return usuarios
##########################################################################





###########################################################################
#Pre:  tenes creado el usuario activo en forma de vector...

#POST: Muestra sus variables

def MostrarDatosUsuarioActivo(self, a):
        print(("idUsuario",+a[0]))
        print(("Nombre",a[1]))
        print(("Mejor puntaje",+a[2]))
        print(("Tiempo jugado",+ a[3]))
##########################################################################




###########################################################################
#Pre: ESTAS USAN PY GAME
########################################################################
# Clases que referencian al estado del click
#PRE: Necesitan tener pygame importado

#POST1: Devuelve la posicion del mouse al hacer click
#POST2: Devuelve el estado de los botones del mouse
# (false,false,false) inactivo

#Gerero la clase Click
class ClickRealizadoEn():
    def __init__(self):
        pygame.mouse.get_pos.__init__(self)
        self.vectorPosicion = pygame.mouse.get_pos()



#Gerero la clase Click
class HizoClick():
    def __init__(self):
        pygame.event.get.__init__(self)
        pygame.mouse.get_pressed.__init__(self)
        pygame.event.get()
        self.vectorBooleano = pygame.mouse.get_pressed()
##########################################################################


#########################################################################
#GENERO FUNCIONES QUE USARE

########################################################################
#Cargo la imagen
def load_image(filename, transparent=False):

        try: image = pygame.image.load(filename)
        except pygame.error as message:
                raise SystemExit(message)
        image = image.convert()
        if transparent:
                color = image.get_at((0, 0))
                image.set_colorkey(color, RLEACCEL)
        return image
########################################################################

########################################################################
#Espero el click
def EsperarClick():
        sinClick = True
        while sinClick==True:
            boolean = HizoClick()
            xy = ClickRealizadoEn()
            boolean.vectorBooleano[0]
            xy.vectorPosicion
            if boolean.vectorBooleano[0] == 1:
                sinClick = False
                print((xy.vectorPosicion))
                return xy.vectorPosicion
########################################################################

########################################################################
#Calculo la distancia

#PRE: ingreso con x e y del click, y con x e y de respuesta correcta
#POST: devuelve la distancia

def CalcularDistancia(clickX, clickY, correctaX, correctaY):
    d = sqrt((clickX - correctaX) ** 2 + (clickY - correctaY) ** 2)
    return d
########################################################################


########################################################################
#Respuesta del juego

#PRE: ingreso con la distancia
#POST: devuelve los puntos y las neuronas

def SegunDistancia(d, p, t):  #Distancia, puntos y neuronas
    if d <= 20:
        resultado = "IMPRESIONANTE"
       #Cargo y reproduzco la cancion
        pygame.mixer.init
        pygame.mixer.music.load("ovacion.mp3")
        pygame.mixer.music.play()
        p = p + 73
        t = t + 2
    if d > 20 and d <= 40:
        resultado = "Muy bien"
        pygame.mixer.music.load("grito.mp3")
        pygame.mixer.music.play()
        p = p + 57
        t = t + 1
    if d > 40 and d <= 60:
        resultado = "Bien"
<<<<<<< HEAD
        pygame.mixer.music.load("woo.mp3")
        pygame.mixer.music.play()
=======
>>>>>>> master
        p = p + 38
        t = t
    if d > 60 and d <= 80:
        resultado = "Regular"
        p = p + 23
        t = t - 1
    if d > 80 and d <= 100:
        resultado = "Mal"
<<<<<<< HEAD
        pygame.mixer.music.load("nelson.mp3")
        pygame.mixer.music.play()
=======
>>>>>>> master
        p = p + 10
        t = t - 5
    if d > 100 and d <= 150:
        resultado = "Horrible"
        pygame.mixer.music.load("abucheo.mp3")
        pygame.mixer.music.play()
        p = p
        t = t - 7
    if d > 150 and d <= 300:
        resultado = "Matate!!!"
<<<<<<< HEAD
        pygame.mixer.music.load("homero.mp3")
        pygame.mixer.music.play()
=======
>>>>>>> master
        p = p - 13
        t = t - 13
    if d > 300:
        resultado = "Deja jugar a otro"
        t = -200
        p = p - 20
    return p, t, resultado
#########################################################################



#########################################################################
def PonerMusicaRandom():
    import random
    pygame.mixer.init()
    a = []
    a.append("parajuego0.mp3")
    a.append("parajuego1.mp3")
    a.append("parajuego2.mp3")
    a.append("parajuego3.mp3")
    a.append("parajuego4.mp3")
    a.append("parajuego5.mp3")
    a.append("parajuego6.mp3")
    a.append("parajuego7.mp3")
    a.append("parajuego8.mp3")
    pygame.mixer.music.load(a[random.randrange(9)])
    pygame.mixer.music.play(-1)
########################################################################

##############################################################################
def CargarUsuarios():
    #Vamos a cargar los usuarios
    matrizUsuarios = RecuperarUsuarios()
    return matrizUsuarios
##############################################################################



###########################################################################
#Pre: Debe existir la matriz de usuarios ya creados.... se debe conocer el
# dni del usuario que se busca, y la cantidad de usuarios cargados

#POST:  se cargan los valores del usuario encontrado: dni, nombre,neuronas
#,puntos
#Y si no existe se pide que los ingrese...

def buscarUsuarioEnTXT(n, dni, matriz):
    existe = False
#Veo si existe el usuario, si no lo creo
    for i in range(0, int(n)):
        if (int(matriz[i][0])== int(dni)):
            dniUsuarioActivo = dni
            nombreUsuarioActivo = matriz[i][1]
            t = matriz[i][2]
            mejorPuntajeUsuarioActivo = matriz[i][3]
            existe = True
    if existe == False:
        dniUsuarioActivo = dni
        print ("Ingrese nuevo usuario")
        nombreUsuarioActivo = input()
        t = 15
        mejorPuntajeUsuarioActivo = 0
    return dniUsuarioActivo, nombreUsuarioActivo, t, mejorPuntajeUsuarioActivo

##########################################################################



##########################################################################
def MostrarPuntosFinales(p):
        #Defino Fuentes
        pygame.font.init()
        fuente = pygame.font.Font(None, 50)
        texto7 = fuente.render("Puntos Finales: " + str(p), 1, (33, 33, 15))
        screen.blit(texto7, (100, 40))
        pygame.display.flip()
###########################################################################



###########################################################################
def mostrarPantallaGameOver(p):



        #Cargo y reproduzco la cancion
        pygame.mixer.init
        pygame.mixer.music.load("abucheo.mp3")
        pygame.mixer.music.play()


        #PONGO FONDO PARA INICIAR JUEGO
        # Constantes
        WIDTH = 942
        HEIGHT = 537

        #Abro la pantalla con las medidas detallas arriba
        screen = pygame.display.set_mode((WIDTH, HEIGHT))


        #Le pongo el titulo al juego
        pygame.display.set_caption("¡¿¿¿Donde...GAME OVEEER.")



        #Pongo el fondo con la imagen antes cargada
        background_image = load_image('game-over.png')


        #Funcion interna para mostrar la puntuacion final
        def MostrarPuntosFinales(p):
            #Defino Fuentes
            pygame.font.init()
            fuente = pygame.font.Font(None, 100)
            texto7 = fuente.render("Puntos Finales: " + str(p), 1, (99, 33, 15))
            screen.blit(texto7, (170, 300))
            pygame.display.flip()




        #Ubico y pongo la pantalla
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

        #Muestro puntaje final
        MostrarPuntosFinales(p)


        tiempo = 0
        while tiempo <= 1999990:
            tiempo = tiempo + 0.3
        return 0






if __name__ == '__main__':
    pygame.init()
    mostrarPantallaGameOver()



#######################################################################


#######################################################################
def instanciaUsuario (usuarioJugando, puntajeFinalJuego):
    if (puntajeFinalJuego>= usuarioJugando[3]):
        usuarioGameOver = Usuario (int(usuarioJugando[0]),
        str(usuarioJugando[1]), int(usuarioJugando[2]),int(puntajeFinalJuego))
    else:
        usuarioGameOver = Usuario (int (usuarioJugando[0]),
        str(usuarioJugando[1]),int (usuarioJugando[2]),int (usuarioJugando[3]))
    usuarioGameOver.MostrarUsuarios()
