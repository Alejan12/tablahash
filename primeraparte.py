def crear_tabla(tamaño):
    tabla=[None]*tamaño
    return tabla
def numero_elementos(tabla):
    return len(tabla)- tabla.count(None)
def funcion_hash(dato, tamaño):
    return len(str(dato).strip())%tamaño
def añadir (tabla, dato):
    lugar= funcion_hash(dato, len(tabla))
    if tabla[lugar] is None:
        tabla[lugar]=dato
    else:
        print("Algo va mal")
def encontrar(tabla, buscar):
    pos=None
    lugar= funcion_hash(buscar, len(tabla))
    if tabla[lugar] is not None:
        if buscar== tabla[lugar]:
            pos-lugar
        else:
            print("aplica funcion de sondeo")
    return pos
def eliminar(tabla, dato):
    pos=None
    lugar= funcion_hash(dato, len(tabla))
    if tabla[lugar] is not None:
        if dato== tabla[lugar]:
            dato= tabla[lugar]
            tabla[lugar]=None
        else:
            print("aplica funcion de sondeo")
    return dato
       
   