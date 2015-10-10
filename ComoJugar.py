# Módulos
from pygame.locals import *
from preguntas import *
from usuarios import *
from funciones import *
from main import *
from menu_mejorado import *



##############################################################################
def MainComoJugar():

###########################################################################
#PONGO FONDO PARA INICIAR JUEGO
    # Constantes
    WIDTH = 942
    HEIGHT = 537

    #Abro la pantalla con las medidas detallas arriba
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #Pongo el fondo con la imagen antes cargada
    background_image = load_image('comojugar.png')
##########################################################################


#######################################################################
#Ubico y pongo la pantalla
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
#######################################################################

    tiempo = 0
    while tiempo <= 1999000:
        tiempo = tiempo + 0.1
    return 0




if __name__ == '__main__':
    pygame.init()
    MainComoJugar()







