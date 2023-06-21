# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:32:49 2020

@author: Federico
"""

import math
import random


VOCALES = 'aeiou'
CONSONANTES = 'bcdfghjklmnpqrstvwxyz'
TAMANIO_MANO = 7

VALORES_LETRAS = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'ñ': 4, 'o': 1, 'p': 3, 'q': 10,
    'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10 }

# -----------------------------------
# Codigo de ayuda
#

ARCHIVO_PALABRAS = "palabras.txt"

def cargar_palabras():
   
    #print("Cargando lista de palabras desde el archivo...")
    # inFile: Archivo
    #abriendo el archivo especificado por la variable ARCHIVO_PALABRAS 
    inFile = open(ARCHIVO_PALABRAS, 'r')
    # palabras: lista de cadenas
    #La función itera sobre cada línea del archivo inFile, donde cada línea representa una palabra.
    #Luego, para cada palabra, se realiza lo siguiente:
    # método strip() para eliminar los espacios en blanco al inicio y final de la palabra.
    # método lower() para convertir la palabra a minúsculas y así asegurarse de que todas las palabras en la lista estén en minúsculas.   
    palabras = []
    for palabra in inFile:
        palabras.append(palabra.strip().lower())
#se imprime la cantidad de palabras cargadas en la lista 
#y se retorna la lista completa de palabras.
    #print("  ", len(palabras), "palabras cargadas.")
    
    return palabras

def obtener_diccionario_frecuencias(secuencia):
    
    # frecuencias: diccionario
    frec = {}
    for x in secuencia:
        frec[x] = frec.get(x,0) + 1
    
    return frec

def obtener_puntaje_palabra(palabra, n):
    
     
      #Se calcula la longitud de la palabra contando la cantidad de letras válidas en ella
      #isalpha() método de cadena en Python que verifica si todos los caracteres de una cadena son letras.
      longitud_palabra = sum(1 for letra in palabra if letra.isalpha())  # Contar letras válidas en la palabra
      #El primer componente del puntaje se calcula sumando los valores numéricos de cada letra de la palabra
      #puntos_letras.get(letra.lower(), 0). Si la letra no está en el diccionario puntos_letras, se le asigna un valor de 0.
      #La función lower() se utiliza para considerar tanto letras mayúsculas como minúsculas.
      primer_componente = sum(VALORES_LETRAS.get(letra.lower(), 0) for letra in palabra.lower())
      
      
      if "*" in palabra:
          longitud_palabra += 1
      
      #El segundo componente del puntaje se calcula utilizando la fórmula: 7 * longitud_palabra - 3 * (n - longitud_palabra), donde n es la cantidad total de letras disponibles en la mano.
      #Este componente asegura que las palabras más largas y las palabras que utilizan la mayoría de las letras de la mano tengan un mayor puntaje.
      segundo_componente = max(7 * longitud_palabra - 3 * (n - longitud_palabra), 1)
     
      #se calcula el puntaje total multiplicando el primer componente por el segundo componente.
      puntaje = primer_componente * segundo_componente
      print()
      
      #La función devuelve el puntaje calculado para la palabra.
      return puntaje
    

def mostrar_mano(mano):
    
    #keys() método  que devuelve una vista de las claves (keys) presentes en el diccionario.
    for letra in mano.keys():
        for j in range(mano[letra]):
             print(letra, end=' ')      # Muestra todas las letras en la misma linea
    print()                             # Linea vacía


def repartir_mano(n):
     
    mano={}
    #math.ceil() redondeado hacia arriba 
    cantidad_vocales = int(math.ceil(n / 3)) # 7/3 = 2,33 [3]
    
    
    vocales = obtener_diccionario_frecuencias(random.choices(VOCALES, k=cantidad_vocales))
    mano.update(vocales)
    print(mano)
    
           
    mano["*"] = 1 # Agregamos el comodin
    
    consonantes = obtener_diccionario_frecuencias(random.choices(CONSONANTES,k=n-1-cantidad_vocales))
    mano.update(consonantes)
    print(mano)
 
    return mano


def actualizar_mano(mano, palabra):
   
    nueva_mano = mano.copy()  # Crear una copia de la mano original
    palabra = palabra.lower() # Convierte a minuscula la palabra   
    # Iterar sobre cada letra de la palabra
    for letra in palabra:
        if letra in nueva_mano:
            nueva_mano[letra] = max(0, nueva_mano[letra] - 1)
            #print(nueva_mano[letra])
    return nueva_mano

def es_palabra_valida(palabra, mano, lista_palabras):
#En Python, cuando no se necesita utilizar el valor de una variable en un bucle,
#es común usar el guion bajo (_) como nombre de variable. 
#En este caso, el guion bajo se utiliza porque no necesitamos utilizar
#el valor de la variable en cada iteración.
    lista_mano = [letra  for letra, cantidad in mano.items() for _ in range(cantidad)]
    lista_mano_copy = lista_mano.copy()  # Crear una copia de la lista mano
        
    palabra_min = palabra.lower()
    palabra_sin_asterisco = ""
    
    
    if "*" in palabra_min:
        palabras_reemplazadas = [palabra_min.replace("*", vocal) for vocal in "aeiou"]
        
        
        for palabra_asterisco in palabras_reemplazadas:
            if palabra_asterisco in lista_palabras:
                
                palabra_sin_asterisco = palabra_asterisco
                
                break
    else:
        
        palabra_sin_asterisco = palabra_min  
      
    
    
    
    
    puede_formar_palabra = True
    
          
    if palabra_sin_asterisco in lista_palabras:
        
        
        for letra in palabra_min:
            if letra in lista_mano_copy:
                
                lista_mano_copy.remove(letra)  # Eliminar la letra de la lista mano
                
            else:
                puede_formar_palabra = False
                
                break
        if puede_formar_palabra:
            
            return True
        else:
            
            return False
    else:
        return False
              

def calcular_longitud_mano(mano):
    
    return sum(mano.values())
    
    
def jugar_mano(mano, lista_palabras):
    
    palabra = ""
    letras_en_mano = calcular_longitud_mano(mano)
    n = TAMANIO_MANO
    puntaje_total = 0
    
    while letras_en_mano > 0 or palabra != "!!":
        
        print(" ")
        print("Mano actual:", end=" ")
        nueva_mano = actualizar_mano(mano, palabra)
        mostrar_mano(nueva_mano)
        
        
        print(" ")
        palabra_anterior = palabra
        
        palabra = input("Ingrese una palabra o ""!!"" para indicar que desea terminar: ")
        
        if (es_palabra_valida(palabra, mano, lista_palabras)):
            
            puntaje = obtener_puntaje_palabra(palabra, n)
            puntaje_total += puntaje
            print("+","+",sep="------------------------")
            print('"{}"'.format(palabra)," + resulta en {} puntos".format(puntaje),end="\n\n")
            
            print("Total: {} puntos".format(puntaje_total))
            print("+","+",sep="------------------------", end="\n\n")
            
            mano = nueva_mano
            
        elif (palabra == "!!"):
            
            break
        
        else:
            print(" ")
            print("+","+",sep="------------------------")
            print("La palabra no es valida")
            print("+","+",sep="------------------------", end="\n")
            
            palabra = palabra_anterior  # Restaurar la palabra anterior
            
    
        
    letras_en_mano = calcular_longitud_mano(mano)
         
    
    if letras_en_mano == 0:
        
        print("+","+",sep="------------------------")
        print("Se quedo sin letras")
        print(" Puntaje Final: {} puntos".format(puntaje_total))
        print("+","+",sep="------------------------", end="\n\n")
    elif palabra == "!!" :
        print(" ")
        print("+","+",sep="------------------------")
        print(" Puntaje Final: {} puntos".format(puntaje_total))
        print("+","+",sep="------------------------", end="\n\n")
        print("")
        


def intercambiar_mano(mano, letra):
    
    mano_copia = mano.copy()
    print(mano_copia)
    letras = VOCALES + CONSONANTES
    
    if letra in mano_copia:
        cantidad_letra = mano_copia.pop(letra)
        #print("Cantidad de la letra a eliminar:", cantidad_letra)
        
        nueva_letra = random.choice(letras)
        while nueva_letra in mano_copia:  # Si existe nueva_letra , crea otra
            nueva_letra = random.choice(letras)
            
        mano_copia[nueva_letra] = cantidad_letra
    
   # print(" ")
    mostrar_mano(mano_copia)
    #print(mano_copia)
    return mano_copia

    
def Bienvenida ():

    print(" ")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("","   BIENVENIDO AL JUEGO DE PALABRAS   ","",sep="|")
    print(""," REALIZADO PARA EL TALLER DE PYTHON  ","",sep="|")
    print("","EN EL MARCO DE ARGENTINA PROGRAMA 4.0","",sep="|")
    print("","          By Matias Cabrera          ","",sep="|")
    print("","                                     ","",sep="|")
    print("","  Visita mi repositorio en GitHub:   ","",sep="|")
    print("","    https://github.com/Bouer         ","",sep="|")
    print("+++++++++++++++++++++++++++++++++++++++")
    print(" ")
    input("Presione Enter para continuar...")
    
    for i in range(15):
        print(" ")
    
def jugar_partida(lista_palabras):
   
   Bienvenida ()
   print("+++++++++++++++++++++++++++++++++++++++")
   print(" ")
   cantidad_manos = None
   mano = repartir_mano(TAMANIO_MANO)

   while cantidad_manos is None:
       
       input_cantidad_manos = input("Ingrese la cantidad de manos a jugar: ")
        
       try:
            cantidad_manos = int(input_cantidad_manos)
            
            if cantidad_manos <= 0:
                print("La cantidad de manos debe ser un número positivo.")
                cantidad_manos = None
       except ValueError:
            print("Ingrese un número válido para la cantidad de manos.")
 

   for i in range(cantidad_manos):
       print(" ")
       print("Jugando mano número", i+1) 
       print(" ")
       
       mano_anterior = mano
              
       if (i >= 1):
           repetir_mano = input("¿Desea repetir la mano actual?? ")
           print(" ")
           if (repetir_mano.lower() == "si" ):
               print("+","+",sep="----------------------------")
               print(" Mano actual: ",end=" " )
               mostrar_mano(mano_anterior)
               print("+","+",sep="----------------------------")
               print(" ")
           else:
               mano = repartir_mano(TAMANIO_MANO)
               print("+","+",sep="----------------------------")
               print(" Mano actual: ",end=" " )
               mostrar_mano(mano)
               print("+","+",sep="----------------------------")
               print(" ")
       else:
              mano = repartir_mano(TAMANIO_MANO)
              print("+","+",sep="----------------------------")
              print(" Mano actual: ",end=" " )
              mostrar_mano(mano)
              print("+","+",sep="----------------------------")
              print(" ")
       
        
       intercambio_deseado = " "
       
       while intercambio_deseado.lower() != "si" and intercambio_deseado.lower() != "no":
           
           intercambio_deseado = input("---- ¿Desea intercambiar una letra? (si/no): ")
        
           if intercambio_deseado.lower() == "si":
               letra_para_reemplazar = input("---- ¿Qué letra desea intercambiar?: ")
               mano_intercam = intercambiar_mano(mano, letra_para_reemplazar)
           elif intercambio_deseado.lower() == "no":
               print("No se realizará ningún intercambio.")
               mano_intercam = mano
           else:
               print("Opción no válida. Por favor, ingrese 'si' o 'no'.")

       jugar_mano(mano_intercam, lista_palabras)
   
   
if __name__ == '__main__':
    lista_palabras = cargar_palabras()
    jugar_partida(lista_palabras)
   
    print("+++++++++++++++++++++")
    print("","   FIN DEL JUEGO   ","",sep="|")
    print("+++++++++++++++++++++")
  
   