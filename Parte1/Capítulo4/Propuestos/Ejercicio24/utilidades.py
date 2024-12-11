def determinar_mayor(esferas):
    esfera_mayor = max(esferas, key=lambda esfera: esfera.peso)
    return esfera_mayor
