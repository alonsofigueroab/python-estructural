# Verificación a flexión simple de un perfil W según AISC
import math

def verificar_flexion(Mu, Zx, Fy):
    phi = 0.9
    Mn = Fy * Zx
    if phi * Mn >= Mu:
        return "Perfil cumple a flexión"
    else:
        return "Perfil NO cumple a flexión"

