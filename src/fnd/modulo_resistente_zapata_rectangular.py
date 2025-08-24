def modulo_resistente_zapata_rectangular(b_x, b_y, h):
    """
    Calcula el módulo resistente de una zapata rectangular.

    Parámetros:
    b_x (float): Ancho de la zapata en la dirección x (en metros).
    b_y (float): Ancho de la zapata en la dirección y (en metros).
    h (float): Altura de la zapata (en metros).

    Retorna:
    tuple: Módulo resistente en la dirección x y en la dirección y (en m^3).
    """
    W_x = (b_x * b_y**2) / 6
    W_y = (b_y * b_x**2) / 6
    return W_x, W_y