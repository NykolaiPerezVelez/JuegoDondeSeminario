import pygame,time
pantalla = pygame.display.set_mode((600,400)) # Crea la pantalla con esas dimensiones
imagen = pygame.image.load('images.jpg') # Carga la imagen
fondo = pygame.Surface((600,400)) # Crea una imagen (Surface)
fondo.fill([255,255,255]) # La rellena de color blanco (255,255,255esla representacion de rojo,amarillo y azul de la imagen)
while 1:
 for i in range(400):
  pantalla.blit(fondo,(0,0)) # Carga el fondo en la pantalla, tapando todo lo que hubiera antes
  pantalla.blit(imagen,(i,i)) # Pone la imagen en las coordenadas que diga la variable i tapando esa parte del fondo
  pygame.display.flip()
  time.sleep(0.01)
 for i in range(400):
  pantalla.blit(fondo,(0,0))
  pantalla.blit(imagen,(400-i,400-i))
  pygame.display.flip()
  time.sleep(0.01)
