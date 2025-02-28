# MAIKOL RODRIGUEZ
# YORGE ARTEAGA

import numpy as np


# Devuelve EAR dados puntos de referencia oculares.
def eye_aspect_ratio(eye):
    # Calcule las distancias euclidianas entre los dos conjuntos de
    # puntos de referencia verticales del ojo (x, y) -coordenadas.
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # Calcule la distancia euclidiana entre la horizontal
    # Coordenadas (x, y) del punto de referencia del ojo

    C = np.linalg.norm(eye[0] - eye[3])

    # Calcular la relación de aspecto del ojo
    ear = (A + B) / (2.0 * C)

    # Devolver la relación de aspecto del ojo
    return ear


# Devuelve MAR dados puntos de referencia oculares
def mouth_aspect_ratio(mouth):
    # Calcula las distancias euclidianas entre los tres conjuntos.
    # de puntos de referencia verticales de la boca (x, y) -coordenadas
    A = np.linalg.norm(mouth[13] - mouth[19])
    B = np.linalg.norm(mouth[14] - mouth[18])
    C = np.linalg.norm(mouth[15] - mouth[17])

    # Calcule la distancia euclidiana entre la horizontal
    # puntos de referencia de la boca coordenadas (x, y)
    D = np.linalg.norm(mouth[12] - mouth[16])

    # Calcular la relación de aspecto de la boca.
    mar = (A + B + C) / (2 * D)

    # Devolver la relación de aspecto de la boca
    return mar


# Dirección de retorno dada la punta y los puntos de anclaje.
def direction(nose_point, anchor_point, w, h, multiple=1):
    nx, ny = nose_point
    x, y = anchor_point

    if nx > x + multiple * w:
        if ny > y + multiple * h:
            return 'down-right'
        elif ny < y - multiple * h:
            return 'up-right'
        else:
            return 'right'
    elif nx < x - multiple * w:
        if ny > y + multiple * h:
            return 'down-left'
        elif ny < y - multiple * h:
            return 'up-left'
        else:
            return 'left'

    if ny > y + multiple * h:
        return 'down'
    elif ny < y - multiple * h:
        return 'up'

    return 'none'
