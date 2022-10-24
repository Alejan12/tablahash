import numpy as np
def franja(stop):
    i=(stop+1)%10
    while i!=stop:
        yield 1
        i=(i+1)%10
def hash(datos):
    poscion=datos%10
    if a[poscion]==0:
        a[poscion]=datos
    else:
        for i in franja(poscion):
            if a[i]==0:
                a[i]=datos
                break
def busqueda(respuesta):
    if (respuesta=="Si" or respuesta=="si"):
        print("q valor quieres buscar")
        z=int(input())
        buscar(z)
        y=input("Desea buscar otro elemento?")
        busqueda(y)
    elif ( respuesta=="No" or respuesta=="no"):
        print("Fin")
    else:
        print("Esa respuesta no vale") 
def buscar(datos):
    posicion=datos%10
    if a[posicion]==datos:
        print("El elemento esta en la posicion: "+ posicion+1)
    else:
        for i in franja(posicion):
            if a[i]==datos:
                print("El elemento se encuentra en la posicion: "+ i+1)
                break
            if i==posicion:
                print("elemento no encontrado")
                break

a=np.array[0,0,0,0,0,0,0,0,0,0]
print("Introduzca los datos")
for i in range(0,10,1):
    x=int(input("Valor:"))
    hash(x)
print(a)
y=input("Desea saber otro valor?")
busqueda(y)



