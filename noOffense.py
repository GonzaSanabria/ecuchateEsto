import cv2
import pygame

# mostrar la imagen + reproducir música
def mostrar_imagen():
    # Inicializar pygame para la música
    pygame.mixer.init()
    pygame.mixer.music.load('cancion.mp3')
    pygame.mixer.music.play()

    # Cargar y redimensionar la imagen
    img = cv2.imread('obesa.jpg')
    img = cv2.resize(img, (1000, 1000))

    # Obtener el centro de la imagen
    center = (img.shape[1] // 2, img.shape[0] // 2)
    angle = 0  # Ángulo de rotación inicial

    # Bucle para rotar la imagen
    while True:
        # Crear la matriz de rotación y aplicar la rotación
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_img = cv2.warpAffine(img, M, img.shape[1::-1])

        # Mostrar la imagen rotada
        cv2.imshow('Imagen', rotated_img)

        # Presiona 'q' para salir
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

        # Incrementar el ángulo
        angle = (angle + 2) % 360

    # Cerrar la ventana de la imagen y detener la música
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

# Pedir al usuario su peso
peso = input("Ingresa tu peso en kg: ")
mostrar_imagen()
