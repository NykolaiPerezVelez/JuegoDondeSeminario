from pygame.locals import *
from preguntas import *
from usuarios import *
from funciones import *
from menuUsuario import *




#########################################################################
#Vamos a cargar los usuarios
matrizUsuarios = RecuperarUsuarios()

#Vamos a cargar las preguntas
matrizPreguntas = RecuperarPreguntas()

#Veamos cuantas preguntas tenemos- Lo usaremos en modulo Random
cantPreguntas = CantidadPreguntas()
##########################################################################


#Notar que entro al main con el usuario activo, que puede existir
#O ser anonimo
def main(usuarioJugando):


###########################################################################
#PONGO FONDO PARA INICIAR JUEGO
    # Constantes
    WIDTH = 942
    HEIGHT = 537

    #Abro la pantalla con las medidas detallas arriba
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    #Le pongo el titulo al juego
    pygame.display.set_caption("¡¿¿¿Donde......")



    #Pongo el fondo con la imagen antes cargada
    background_image = load_image('mapamundi.gif')
##########################################################################




#########################################################################
    #Cargo y reproduzco la cancion
    PonerMusica()
########################################################################

##########################################################################
#Defino Fuentes
    pygame.font.init()
    fuente = pygame.font.Font(None, 50)
    fuente1 = pygame.font.Font('kristen ITC.ttf', 30)
    fuente2 = pygame.font.Font('kristen ITC.ttf', 18)


    def MostrarPuntos(punTotales, neu):
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
        texto = fuente.render("Puntos: " + str(punTotales), 1, (0, 0, 255))
        texto1 = fuente.render("Neuronas vivas:" + str(neu), 1, (0, 0, 255))
        screen.blit(texto1, (0, 0))
        screen.blit(texto, (0, 30))
        pygame.display.flip()

    def MostrarPregunta(pregu):
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
        texto2 = fuente1.render(str(pregu), 1, (0, 0, 15))
        screen.blit(texto2, (10, 0))
        pygame.display.flip()


    def MostrarResultado(p, t, resultado):
        texto3 = fuente2.render(str(resultado), 1, (0, 0, 15))
        texto4 = fuente2.render("Puntos: " + str(p), 1, (0, 0, 15))
        texto5 = fuente2.render("Neuronas: " + str(t), 1, (0, 0, 15))
        texto6 = fuente2.render("Ultimo resultado: " , 1, (0, 0, 15))
        screen.blit(texto3, (350, 420))
        screen.blit(texto4, (350, 450))
        screen.blit(texto5, (350, 480))
        screen.blit(texto6, (350, 390))
        pygame.display.flip()
#########################################################################


    def MostrarPuntosYNeuronasRestantes(t,p):
        texto6 = fuente2.render("Neuronas Vivas: " + str(t), 1, (0, 0, 15))
        texto7 = fuente2.render("Puntos Acumulados: " + str(p), 1, (0, 0, 15))
        screen.blit(texto6, (10, 400))
        screen.blit(texto7, (10, 430))
        pygame.display.flip()


#######################################################################
#Ubico y pongo la pantalla
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
#######################################################################


##########################################################################
#Asigno al azar la primer pregunta
    pregRandom = AsignarPreguntaRandom(cantPreguntas, matrizPreguntas)
    MostrarPregunta(pregRandom[0])
##########################################################################



##########################################################################
    ##Defino neuronas, por defecto 10- Este parametro se cambiara con la
    #dificultad del juego
    neuronas = usuarioJugando[2]
    #Defino puntos acuulados = 0, sera el contador de puntuacion
    puntosAcumulados = 0

    #Muestro ambos parametros por pantalla
    MostrarPuntosYNeuronasRestantes(neuronas,puntosAcumulados)
#########################################################################




#########################################################################
    ##Bucle hasta que quedas sin neuronas
    while neuronas>0:
#######################################################################
#vector boobleano false false false en condiciones normales
        boolean = HizoClick()
#######################################################################



        #Si no hice click....
        if boolean.vectorBooleano[0] == 0:
            x, y = EsperarClick()
            xx = pregRandom[1]
            yy = pregRandom[2]
            p = 0
            t = 0
            d = CalcularDistancia(x, y, xx, yy)
            p, t, resultado = SegunDistancia(d, p, t)
            #En el renglon anterior "sumo", puntos, neuronas y pongo
            #comentario IMPRE..
            #OTRA PREGUNTA
            pregRandom = AsignarPreguntaRandom(cantPreguntas, matrizPreguntas)
            MostrarPregunta(pregRandom[0])
            MostrarResultado(p, t, resultado)
            neuronas = neuronas + t
            puntosAcumulados = puntosAcumulados + p
            MostrarPuntosYNeuronasRestantes(neuronas,puntosAcumulados)

    #Con este puntaje termino el juego
    puntajeFinalJuego = puntosAcumulados



    #Entro a la pantalla con el puntaje final, para mostrarlo
    mostrarPantallaGameOver(puntajeFinalJuego)


    GuardousuarioEnTXT (usuarioJugando, puntajeFinalJuego)









if __name__ == '__main__':
    pygame.init()
    main(usuarioJugando)

