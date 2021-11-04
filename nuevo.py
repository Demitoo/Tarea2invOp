from math import exp
import math
import random



def distanciaEntrePuestos(largoPuestos,a,b):
    suma=0
    for x in range(a+1,b):
        suma=suma+largoPuestos[x]
    suma=suma+(largoPuestos[a]/2)+(largoPuestos[b]/2)
    return suma

def fSolucion(nPuestos,largoPuestos,matrizDistanciaClientes):
    suma=0
    for x in range(0,nPuestos-1):
        for y in range(x+1,nPuestos):
            suma=suma+(distanciaEntrePuestos(largoPuestos,x,y) * matrizDistanciaClientes[x][y])
    return suma

def nVecino(y):
    x=y[:]
    random.shuffle(x)

    return x

    
        



nPuestos=8
largoPuestos=[5,6,5,4,5,4,6,5]
matrizDistanciaClientes=[[0,7,5,6,7,5,6,7],[7,0,7,6,5,7,5,6],[5,7,0,6,5,6,5,7],[6,6,6,0,7,6,7,5],[7,5,5,7,0,7,5,6],[5,7,6,6,7,0,6,5],[6,5,5,7,5,6,0,7],[7,6,7,5,6,5,7,0]]
temperaturaInicial=4000
temperatura=temperaturaInicial
alpha=0.9

mejorSolucion=largoPuestos[:]
actualSolucion=largoPuestos[:]
nuevaSolucion=0
p=0
k=10000

print(fSolucion(nPuestos,largoPuestos,matrizDistanciaClientes))

while k>0:
    nuevaSolucion=nVecino(actualSolucion)
    #print(nuevaSolucion)
    #print(actualSolucion)
    delta=fSolucion(nPuestos,nuevaSolucion,matrizDistanciaClientes)-fSolucion(nPuestos,actualSolucion,matrizDistanciaClientes)
    if delta<0:
        actualSolucion=nuevaSolucion[:]
    else:
        #print(delta)
        p=math.exp(-delta/temperatura)
        r=random.random()
        if r < p:
            actualSolucion=nuevaSolucion[:]
    if fSolucion(nPuestos,actualSolucion,matrizDistanciaClientes) - fSolucion(nPuestos,mejorSolucion,matrizDistanciaClientes) < 0:
        mejorSolucion=actualSolucion[:]
    temperatura=temperatura*alpha
    #print(temperatura)
    k=k-1

print(mejorSolucion)
print(fSolucion(nPuestos,mejorSolucion,matrizDistanciaClientes))


