"""
Cálculo de Espectro de Respuesta Sísmica
Basado en la Norma Chilena NCh433.Of2008

Autor: Alonso Figueroa Bustos
Ingeniero Civil Estructural

Script en proceso de desarrollo
"""

import numpy as np
import matplotlib.pyplot as plt

def espectro_respuesta(T, tipo_suelo='Tipo C'):
    """
    Calcula la aceleración espectral de respuesta para un periodo T dado,
    considerando el tipo de suelo según norma chilena.
    
    Parámetros:
        T (float o np.array): Periodo(s) de vibración [s]
        tipo_suelo (str): Tipo de suelo ('Tipo A', 'Tipo B', 'Tipo C', 'Tipo D', 'Tipo E')
    
    Retorna:
        Sa (float o np.array): Aceleración espectral [g]
    """
    
    # Parámetros característicos de espectro para cada tipo de suelo (ejemplo)
    if tipo_suelo == 'Tipo C':
        # Valores típicos para suelo tipo C
        Tc = 0.5
        T1 = 1.0
        Sa_max = 1.2  # Valor ejemplo
        
    # Implementar más condiciones para otros tipos de suelo
    else:
        raise ValueError('Tipo de suelo no soportado')
    
    Sa = np.zeros_like(T, dtype=float)
    
    # Cálculo simplificado del espectro por tramos
    for i, t in enumerate(T):
        if t <= Tc:
            Sa[i] = Sa_max * (1 + t / Tc)
        elif Tc < t <= T1:
            Sa[i] = Sa_max
        else:
            Sa[i] = Sa_max * (T1 / t)
    
    return Sa

if __name__ == "__main__":
    # Periodos desde 0 a 4 s
    T = np.linspace(0, 4, 400)
    Sa = espectro_respuesta(T)
    
    plt.plot(T, Sa, label='Tipo C')
    plt.title('Espectro de Respuesta Sísmica - Norma Chilena NCh433.Of2008')
    plt.xlabel('Periodo (s)')
    plt.ylabel('Aceleración espectral (g)')
    plt.grid(True)
    plt.legend()
    plt.show()
