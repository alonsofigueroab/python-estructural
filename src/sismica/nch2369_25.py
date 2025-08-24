
def coef_importancia(categoria:str):
    """
    Devuelve el coeficiente de importancia de una categoría de ocupación.
    """
    
    importancia={
        "I": 0.8,
        "II": 1.0,
        "III": 1.2,
        "IV": 1.2,
    }
    
    return importancia[categoria]

def acel_efectiva(zona:int):
    """
    Devuelve la aceleración efectiva de una zona.
    """
    if x not in [1,2,3]:
        raise ValueError("Zona sísmica debe ser 1, 2 o 3")

    aceleracion={
        1: 0.2,
        2: 0.3,
        3: 0.4
    }
    
    return aceleracion[zona],1.4*aceleracion[zona]

