from math import exp
import math
import random
import statistics
import csv



def distanciaEntrePuestos(largoPuestos,a,b):
    suma=0
    for x in range(a+1,b):
        suma=suma+largoPuestos[x]
    suma=suma+(largoPuestos[a]/2)+(largoPuestos[b]/2)
    return suma

def fSolucion(largoPuestos,matrizDistanciaClientes):
    suma=0
    nPuestos=len(largoPuestos)
    for x in range(0,nPuestos-1):
        for y in range(x+1,nPuestos):
            suma=suma+(distanciaEntrePuestos(largoPuestos,x,y) * matrizDistanciaClientes[x][y])
    return suma

def nVecino(y):
    x=y[:]
    random.shuffle(x)

    return x

def simulatedAnnealing(largoPuestos,matrizDistanciaClientes):

    #VARIABLES DE LA METAHEURISTICA
    temperaturaInicial=4000
    temperatura=temperaturaInicial
    alpha=0.9

    #INICIACION DE VARIABLES 
    mejorSolucion=largoPuestos[:]
    actualSolucion=largoPuestos[:]
    nuevaSolucion=0
    p=0 #Probabilidad de elegir una peor solucion
    k=1000 #Numero de iteraciones que se ejecutara la metaheuristica


    while k>0:
        nuevaSolucion=nVecino(actualSolucion)
        #print(nuevaSolucion)
        #print(actualSolucion)
        delta=fSolucion(nuevaSolucion,matrizDistanciaClientes)-fSolucion(actualSolucion,matrizDistanciaClientes)
        if delta<0:
            actualSolucion=nuevaSolucion[:]
        else:
            #print(delta)
            p=math.exp(-delta/temperatura)
            r=random.random()
            if r < p:
                actualSolucion=nuevaSolucion[:]
        if fSolucion(actualSolucion,matrizDistanciaClientes) - fSolucion(mejorSolucion,matrizDistanciaClientes) < 0:
            mejorSolucion=actualSolucion[:]
        temperatura=temperatura*alpha
        #print(temperatura)
        k=k-1
    return mejorSolucion[:]







#Variables para iterar
Resultado=0
Resultados=[]
ResultadosFsolucion=[]
media=0
desviacionEstandar=0
#Instancias iniciales
nPuestos=0
solucionInicial=[]
matrizDistanciaClientes=[]

#LEER ARCHIVO Y ASIGNAR LO LEIDO A LAS INSTANCIAS INICIALES
with open('S56.csv',newline='') as f:
    reader=csv.reader(f)
    data=list(reader)
    cont=0
    for x in data:
        x=list(map(int,x))
        if cont==0:
            nPuestos=x[0]
            cont=cont+1
            continue
        if cont==1:
            solucionInicial=x[:]
            cont=cont+1
            continue
        matrizDistanciaClientes.append(x[:])
        cont=cont+1
    f.close()

        

print(fSolucion(solucionInicial,matrizDistanciaClientes))

for iteracion in range(0,10):
    Resultado=simulatedAnnealing(solucionInicial,matrizDistanciaClientes)
    Resultados.append(Resultado)
    ResultadosFsolucion.append(fSolucion(Resultado,matrizDistanciaClientes))


desviacionEstandar=statistics.stdev(ResultadosFsolucion)
media=statistics.mean(ResultadosFsolucion)
print ("Desviacion estandar: " , desviacionEstandar)
print ("Media: " , media)
print ("Soluciones evaluadas en la funcion solucion" , ResultadosFsolucion)


