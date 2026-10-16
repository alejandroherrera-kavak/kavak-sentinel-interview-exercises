def agrupar_por_ventana(tiempos, ventana):
    grupos = []
    actual = []
    for t in sorted(tiempos):
        if actual and t - actual[0] > ventana:
            grupos.append(actual)
            actual = []
        actual.append(t)
    if actual:
        grupos.append(actual)
    return grupos


# Traza estas llamadas a mano. No hace falta ejecutarlas.
# agrupar_por_ventana([1, 3, 10, 11, 25], 5)
# agrupar_por_ventana([1, 3, 10, 11, 25], 3)
