import pygame
import random
import matplotlib.pyplot as plt

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
w, h = 800, 400
pantalla = pygame.display.set_mode((w, h))
pygame.display.set_caption("Juego: Disparo de Bala, Salto, Nave y Menú")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Variables del jugador, bala, nave, etc.
jugador = None
bala = None
bala2 = None
fondo = None
nave = None

# Variables de salto
salto = False
salto_altura = 15  # Velocidad inicial de salto
gravedad = 1
en_suelo = True

# Variables de caminar
camina = False
camina_distancia = 20
friccion = 1

# Variables de pausa y menú
pausa = False
fuente = pygame.font.SysFont('Arial', 24)
menu_activo = True
modo_auto = False  # Indica si el modo de juego es automático

# Lista para guardar los datos de velocidad, distancia y salto (target)
datos_modelo = []

# Cargar las imágenes
jugador_frames = [
    pygame.image.load('assets/sprites/mono_frame_1.png'),
    pygame.image.load('assets/sprites/mono_frame_2.png'),
    pygame.image.load('assets/sprites/mono_frame_3.png'),
    pygame.image.load('assets/sprites/mono_frame_4.png')
]
bala_img = pygame.image.load('assets/sprites/purple_ball.png')
bala_img2 = pygame.image.load('assets/sprites/purple_ball.png')
fondo_img = pygame.image.load('assets/game/fondo2.png')
nave_img = pygame.image.load('assets/game/ufo.png')

# Escalar la imagen de fondo para que coincida con el tamaño de la pantalla
fondo_img = pygame.transform.scale(fondo_img, (w, h))

# Crear el rectángulo del jugador y balas
jugador = pygame.Rect(50, h - 100, 32, 48)
bala = pygame.Rect(w - 50, h - 90, 16, 16)
bala2 = pygame.Rect(w - 745, h - 390, 16, 16)
nave = pygame.Rect(w - 100, h - 100, 64, 64)

# Variables para la animación del jugador
current_frame = 0
frame_speed = 10
frame_count = 0

# Variables de las balas
velocidad_bala = -3
bala_disparada = False
velocidad_bala2 = 3
bala_disparada2 = False

# Variables para el fondo en movimiento
fondo_x1 = 0
fondo_x2 = w


# FFunción para disparar la bala
def disparar_bala():
    global bala_disparada, velocidad_bala
    if not bala_disparada:
        velocidad_bala = random.randint(-8, -3)
        bala_disparada = True

def disparar_bala2():
    global bala_disparada2, velocidad_bala2
    if not bala_disparada2:
        velocidad_bala2 = random.randint(3, 8)
        bala_disparada2 = True


# Función para reiniciar la posición de la bala
def reset_bala():
    global bala, bala_disparada
    bala.x = w - 50
    bala_disparada = False

def reset_bala2():
    global bala2, bala_disparada2
    bala2.y = h - 390
    bala_disparada2 = False

# Función para manejar el salto
def manejar_salto():
    global jugador, salto, salto_altura, en_suelo
    if salto:
        jugador.y -= salto_altura
        salto_altura -= gravedad
        if jugador.y >= h - 100:
            jugador.y = h - 100
            salto = False
            salto_altura = 15
            en_suelo = True

# Función para manejar el avance del jugador
def manejar_caminata():
    global jugador, camina, camina_distancia, friccion
    if camina:
        jugador.x += camina_distancia
        camina_distancia -= friccion
        if jugador.x <= 60:
            jugador.x = 60
            camina = False
            camina_distancia = 20

# Función para guardar datos
def guardar_datos():
    global jugador, bala, velocidad_bala, salto, bala2, camina
    distancia = abs(jugador.x - bala.x)
    salto_hecho = 1 if salto else 0
    caminata_hecha = 1 if camina else 0
    datos_modelo.append((velocidad_bala, distancia, salto_hecho, caminata_hecha))

# Función para graficar datos
def graficar_datos():
    if not datos_modelo:
        print("No hay datos para graficar.")
        return
    velocidades, distancias, saltos, caminatas = zip(*datos_modelo)
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    axs[0, 0].plot(velocidades, label='Velocidad de la Bala', color='gold')
    axs[0, 0].set_title('Velocidad de la Bala')
    axs[0, 1].plot(distancias, label='Distancia', color='purple')
    axs[0, 1].set_title('Distancia al Jugador')
    axs[1, 0].plot(saltos, label='Saltó (1 = Sí, 0 = No)', color='brown')
    axs[1, 0].set_title('Saltó')
    axs[1, 1].plot(caminatas, label='Caminó (1 = Sí, 0 = No)', color='silver')
    axs[1, 1].set_title('Caminó')
    plt.tight_layout()
    plt.show()


def mostrar_menu():
    global menu_activo, modo_auto
    pantalla.fill(NEGRO)
    texto = fuente.render("Presiona 'A' para Auto, 'M' para Manual, 'G' para Ver Gráficas, 'Q' para Salir", True, BLANCO)
    pantalla.blit(texto, (w // 8, h // 2))
    pygame.display.flip()

    while menu_activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    modo_auto = True
                    menu_activo = False
                elif evento.key == pygame.K_m:
                    modo_auto = False
                    menu_activo = False
                elif evento.key == pygame.K_g:
                    graficar_datos()
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    exit()


def reiniciar_juego():
    global menu_activo, jugador, bala, bala2, bala_disparada, salto, camina, en_suelo
    menu_activo = True
    jugador.x, jugador.y = 50, h - 100
    reset_bala()
    reset_bala2()
    salto = False
    camina = False
    en_suelo = True  # Aseguramos que el jugador esté en el suelo al reiniciar
    mostrar_menu()


def update():
    global bala, velocidad_bala, current_frame, frame_count, fondo_x1, fondo_x2, bala2
    fondo_x1 -= 1
    fondo_x2 -= 1
    if fondo_x1 <= -w:
        fondo_x1 = w
    if fondo_x2 <= -w:
        fondo_x2 = w

    pantalla.blit(fondo_img, (fondo_x1, 0))
    pantalla.blit(fondo_img, (fondo_x2, 0))
    pantalla.blit(jugador_frames[current_frame], (jugador.x, jugador.y))
    pantalla.blit(nave_img, (nave.x, nave.y))

    if bala_disparada:
        bala.x += velocidad_bala
    if bala_disparada2:
        bala2.y += velocidad_bala2

    pantalla.blit(bala_img, (bala.x, bala.y))
    pantalla.blit(bala_img2, (bala2.x, bala2.y))

    if jugador.colliderect(bala) or jugador.colliderect(bala2):
        reiniciar_juego()

    if bala.x < 0:  # Reiniciar la bala cuando se sale de la pantalla
        reset_bala()

    if bala2.y > h:  # Reiniciar la segunda bala cuando se sale de la pantalla
        reset_bala2()


def main():
    global salto, en_suelo, camina, pausa
    reloj = pygame.time.Clock()
    mostrar_menu()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and en_suelo:
                    salto = True
                    en_suelo = False
                if evento.key == pygame.K_d:
                    camina = True
                if evento.key == pygame.K_p:  # Pausar el juego
                    pausa = not pausa
                if evento.key == pygame.K_q:  # Salir del juego
                    pygame.quit()
                    exit()

        if not pausa:
            if salto:
                manejar_salto()
            if camina:
                manejar_caminata()
            guardar_datos()
            if not bala_disparada:
                disparar_bala()
            if not bala_disparada2:
                disparar_bala2()
            update()
        else:
            pantalla.fill(NEGRO)
            texto = fuente.render("Juego Pausado. Presiona 'P' para reanudar.", True, BLANCO)
            pantalla.blit(texto, (w // 4, h // 2))
            pygame.display.flip()

        pygame.display.flip()
        reloj.tick(30)


if __name__ == "__main__":
    main()
