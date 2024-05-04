import pygame
import random
import math
from pygame import mixer

# Paquete pygame
pygame.init()  # Inicializar el paquete

# Pantalla
pantalla = pygame.display.set_mode((800, 600))  # Crear la pantalla
pygame.display.set_caption('Invasión Espacial')  # Cambiar el título
# Cargar icono
icono = pygame.image.load('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\img\\ovni.png')
pygame.display.set_icon(icono)  # Cambiar el icono
# Cambiar el fondo de la pantalla
fondo = pygame.image.load('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\img\\Fondo.jpg')

# Música
# Poner música de fondo
mixer.music.load('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\sonidos\\MusicaFondo.mp3')
mixer.music.set_volume(.3)  # Fijar el volumen
mixer.music.play(-1)  # -1: se repite cada vez que termine

# Jugador
# Cargar icono del jugador
img_jugador = pygame.image.load('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\img\\cohete.png')
jugador_x = 368  # Posición del jugador en x
jugador_y = 500  # Posición del jugador en y
jugador_x_cambio = 0  # La variable empieza en 0 para que el jugador no se esté moviendo

# Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):  # Por enemigo de la cantidad de enemigos que debe haber en pantalla (8)
    # Cargar icono del enemigo
    img_enemigo.append(pygame.image.load('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\img\\'
                                         'enemigo.png'))
    enemigo_x.append(random.randint(0, 736))  # Generar de forma aleatoria con un rango la posición x
    enemigo_y.append(random.randint(50, 200))  # Generar de forma aleatoria con un rango la posición y
    enemigo_x_cambio.append(.5)  # Puede empezar en cualquier número mayor a 0 para que regrese en sentido horizontal
    enemigo_y_cambio.append(50)  # Empieza en 50 para que no esté tan arriba el enemigo

# Bala
balas = []  # Se genera una lista vacía porque son dos balas las que dispara la nave
# Cargar icono de la bala
img_bala = pygame.image.load('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\img\\bala.png')
bala_x = 0  # Empieza en 0 porque realmente va a obtener la posición del jugador en x
bala_y = 500  # Empieza en 500 como la del jugador porque de ahí sale
bala_x_cambio = 0  # Empieza en 0 porque ya no se va a mover a partir de donde fue disparada
bala_y_cambio = 2  # Empieza en 2 para la velocidad, es decir, un contador de +2
bala_visible = False  # Empieza en falso porque al principio la bala no puede ser visible

# Puntaje
puntaje = 0  # Empieza en 0
fuente = pygame.font.Font('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\fuentes'
                          '\\FreeSansBold.ttf', 32)  # Fuente para el puntaje y su tamaño
texto_x = 10  # Posición en x del texto
texto_y = 10  # Posición en y del texto

# Game Over
fuente_final = pygame.font.Font('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\fuentes'
                                '\\Retronoid.ttf', 50)  # Fuente para el texto de game over y su tamaño


# Función del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))  # blit: colocar elementos en pantalla


# Función del enemigo
def enemigo(x, y, ene):  # ene: es el índice correspondiente a cada enemigo que se declaro en el for e in cantidad_enem
    pantalla.blit(img_enemigo[ene], (x, y))


# Función disparar bala
def disparar_bala(x, y):
    global bala_visible  # Se modificó con global la variable inicializada fuera de la función
    bala_visible = True  # La bala será visible cuando sea disparada
    pantalla.blit(img_bala, (x + 16, y + 10))  # Se agrega 16 y 10 para que sea desde el centro de la nave


# Función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))  # Fórmula de la distancia
    if distancia < 27:  # Si la distancia es menor a 27
        return True  # Hay una colisión
    else:
        return False  # No hay colisión


# Función puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))  # True: para que no esté tan pixelado
    pantalla.blit(texto, (x, y))


# Función juego terminado
def game_over():
    game_over_fuente = fuente_final.render('GAME OVER', True, (255, 255, 255))
    pantalla.blit(game_over_fuente, (60, 200))


# Loop de ejecución
se_ejecuta = True  # Generar un loop de ejecución
while se_ejecuta:  # Mientras se ejecuta el loop

    # Fondo de pantalla
    pantalla.blit(fondo, (0, 0))  # Cambiar el fondo de la pantalla

    # Eventos en el programa
    for evento in pygame.event.get():  # Por cada evento dentro de los eventos del juego

        # Evento de cerrar la pantalla
        if evento.type == pygame.QUIT:  # Si el evento es de tipo QUIT (cerrar)
            se_ejecuta = False  # El loop de ejecución se va a dejar de ejecutar

        # Evento de presionar teclas
        if evento.type == pygame.KEYDOWN:  # Si el evento es de tipo presionar la tecla
            if evento.key == pygame.K_LEFT:  # Si la tecla presionada es la izquierda
                jugador_x_cambio = -.5  # El jugador se va a mover a la izquierda
            if evento.key == pygame.K_RIGHT:  # Si la tecla presionada es la derecha
                jugador_x_cambio = .5  # El jugador se va a mover a la derecha
            if evento.key == pygame.K_SPACE:  # Si la tecla presionada es la barra espaciadora
                sonido_bala = mixer.Sound('C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial\\sonidos'
                                          '\\disparo.mp3')  # Colocar un sonido de disparo para las balas
                sonido_bala.set_volume(.5)  # Fijar el volumen del sonido
                sonido_bala.play()  # Reproducir el sonido
                nueva_bala = {  # Se genera un diccionario para disparar 2 balas al mismo tiempo
                    "x": jugador_x,  # Va a ser la posición original del jugador en x
                    "y": jugador_y,  # Va a ser la posición original del jugador en y
                    "velocidad": -5  # La velocidad de la bala va a ser de 5 hacia arriba
                }
                balas.append(nueva_bala)  # Se agrega a la lista de balas para llevar un registro
                if not bala_visible:  # Si la bala no está visible
                    bala_x = jugador_x  # La posición horizontal de la bala va a ser igual a la del jugador
                    disparar_bala(bala_x, bala_y)  # Llamar a la función de disparar bala con posiciones x y y

        # Evento de soltar teclas
        if evento.type == pygame.KEYUP:  # Si el evento es de tipo soltar la tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:  # Si la tecla es la izquierda o derecha
                jugador_x_cambio = 0  # El jugador va a detenerse

    # Modificar la posición del jugador
    jugador_x += jugador_x_cambio  # A la posición x del jugador se le agrega el cambio en x que se genere en el loop

    # Mantener jugador dentro de los bordes de la pantalla.
    if jugador_x <= 0:  # Si la posición es menor o igual a 0
        jugador_x = 0  # El jugador se va a colocar en 0
    elif jugador_x >= 736:  # A 800 se le resta el tamaño del icono del personaje que es de 64
        jugador_x = 736  # El jugador se va a colocar en 736

    # Modificar la posición del enemigo
    for e in range(cantidad_enemigos):  # e va a ser el indicador del enemigo, para saber cuál es

        # Fin del juego
        if enemigo_y[e] >= 500:  # Si la posición de y (hacia abajo) es mayor o igual a 500
            for k in range(cantidad_enemigos):  # Por un enemigo (muerto) en cantidad de enemigos que son 8
                enemigo_y[k] = 1000  # El enemigo se coloca en 1000 para que desaparezca de pantalla
            game_over()  # Se manda a llamar a la función game_over para terminar el juego
            break  # Salir del loop

        enemigo_x[e] += enemigo_x_cambio[e]  # Se agrega el cambio en x que se genere en el loop para cada enemigo

        # Mantener enemigo dentro de los bordes de la pantalla
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = .5  # Cuando toque el borde se regresa a la derecha
            enemigo_y[e] += enemigo_y_cambio[e]  # Cuando toque el borde comienza a bajar
        elif enemigo_x[e] >= 736:  # A 800 se le resta el tamaño del icono del enemigo que es de 64
            enemigo_x_cambio[e] = -.5  # Cuando toque el borde se regresa a la izquierda
            enemigo_y[e] += enemigo_y_cambio[e]  # Cuando toque el borde comienza a bajar

        # Colisión
        for bala in balas:  # Por cada bala en la lista de balas
            # Comprobar si hay colisión entre la bala y el enemigo actual
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])

            if colision_bala_enemigo:  # Si hay colisión entre la bala y el enemigo
                sonido_colision = mixer.Sound("C:\\Users\\Aiko Marín\\Desktop\\Proyectos Python\\InvasionEspacial"
                                              "\\sonidos\\Golpe.mp3")  # Seleccionar sonido de colisión
                sonido_colision.set_volume(.5)  # Fijar el volumen del sonido
                sonido_colision.play()  # Reproducir el sonido
                balas.remove(bala)  # Eliminar la bala de la lista de balas
                puntaje += 1  # Aumentar el puntaje

                # Reposicionar el enemigo aleatoriamente en la parte superior de la pantalla
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)

                break  # Salir del bucle, ya que se encontró una colisión y se procesó

        # Código para lanzar una bala
        # colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y) # Llamar a la función hay colision
        # if colision:
        #     sonido_colision = mixer.Sound('Golpe.mp3')
        #     sonido_colision.set_volume(.5)
        #     sonido_colision.play()
        #     bala_y = 500  # Restablecer la bala a su posición original
        #     bala_visible = False  # La bala no se va a ver
        #     puntaje += 1  # Ir aumentando el puntaje
        #     enemigo_x[e] = random.randint(0, 736)  # Desaparecer y aparecer otro enemigo en x
        #     enemigo_y[e] = random.randint(50, 200)  # Desaparecer y aparecer otro enemigo en y

        # Función de enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)  # Mandar a llamar a la función con las posiciones x y y, y el índice

    # Disparar varias balas
    if bala_y <= -64:  # Cuando la bala desaparezca, no cuando toque el borde, por eso es menor o igual a 64 (su tamaño)
        bala_y = 500  # Se restablece la posición de la bala
        bala_visible = False  # No va a ser visible

    # Movimiento de la bala
    for bala in balas:  # Por cada bala en la lista de balas
        bala["y"] += bala["velocidad"]  # Incrementar la posición vertical de la bala según su velocidad

        # Dibujar la imagen de la bala en la pantalla en su nueva posición
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))

        # Si la posición vertical de la bala es menor que 0 (está fuera de la pantalla hacia arriba)
        if bala["y"] < 0:
            balas.remove(bala)  # Eliminar la bala de la lista, ya que está fuera de la pantalla y no es visible

    if bala_visible:  # Si la bala está visible
        disparar_bala(bala_x, bala_y)  # Llamar a la función disparar bala con las variables de posición x y y
        bala_y -= bala_y_cambio  # La posición vertical va a ir subiendo en 2

    # Funciones
    jugador(jugador_x, jugador_y)  # Mandar a llamar a la función con las posiciones x y y
    mostrar_puntaje(texto_x, texto_y)  # Mandar a llamar a la función con las posiciones x y y

    # Actualización
    pygame.display.update()  # Necesita actualizarse la pantalla
