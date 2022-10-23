from turtle import position
from primeraparte import crear_tabla,añadir,encontrar
tabla=crear_tabla(9)
nombre=input()
while(nombre!=""):
    añadir(tabla,nombre)
    nombre=input()
print("Nombre a buscar")
buscado=input()
posicion=encontrar(tabla,buscado)
if posicion is not None:
    print("elemento encontrado ", posicion.info)
else:
    print("No se ha encontrado na")