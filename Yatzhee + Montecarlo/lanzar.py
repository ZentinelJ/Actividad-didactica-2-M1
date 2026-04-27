def lanzar(tablero, mantener=None):
    """
    Recibe un arreglo (tablero) de 5 objetos dice.
    Lanza aquellos que no estén en la lista de índices 'mantener'.
    """
    if mantener is None:
        mantener = []
        
    for i, d in enumerate(tablero):
        if i not in mantener:
            d.lanzar()
    return tablero