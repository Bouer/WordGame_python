# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:32:49 2020

@author: Federico
"""

import math
import random
import os



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
	
#
# (fin Codigo de ayuda)
# -----------------------------------

#
# Problema #2: Puntuar una palabra
#
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
    
    for i in range(cantidad_vocales-1):
        #random.choice() - vocal aleatoria de la lista VOCALES
        x = random.choice(VOCALES)
#Se utiliza el método get() del diccionario para obtener el valor actual de la clave x.
#Si la clave x no existe en el diccionario, se devuelve 0 como valor predeterminado.
#Se agrega 1 al valor obtenido (o 0 si la clave no existía) 
#y se actualiza el diccionario mano con el nuevo valor.
#Esto garantiza que se mantenga un registro de cuántas veces se ha agregado
#cada vocal al diccionario mano.
        mano[x] = mano.get(x, 0) + 1
        
    mano["*"] = 1 # Agregamos el comodin
    
    for i in range(cantidad_vocales, n):    
        x = random.choice(CONSONANTES)
        mano[x] = mano.get(x, 0) + 1
       
    return mano

#
# Problema #3: Actualizar la mano eliminando letras.
#
def actualizar_mano(mano, palabra):
   
    nueva_mano = mano.copy()  # Crear una copia de la mano original
    palabra = palabra.lower() # Convierte a minuscula la palabra   
    # Iterar sobre cada letra de la palabra
    for letra in palabra:
        if letra in nueva_mano:
            nueva_mano[letra] = max(0, nueva_mano[letra] - 1)
            #print(nueva_mano[letra])
    return nueva_mano


#
# Problema #4: Verificar si la palabra es válida.
#
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
              
    
    
    """
    Devuelve True si la palabra está en lista_palabras y está compuesta
    completamente por letras en la mano. Sino, devuelve False.
    No se debe modificar ni mano ni lista_palabras.
   
    palabra: string
    mano: diccionario (string -> int)
    lista_palabras: lista de cadenas en minúsculas
    Retorna: boolean
    """
    

#
# Problema #5: Jugar una mano
#
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
        
        
     
        
  
  

    """
    Permite que un usuario juegue una mano, con las siguientes consideraciones:

    * Se le muestra la mano actual.
    
    * El usuario puede ingresar una palabra.

    * Cuando una palabra es ingresada (válida o inválida), utiliza letras de la mano.

    * Una palabra inválida se rechaza, mediante un mensaje que le pide al usuario
      que ingrese otra palabra.

    * Después de cada palabra válida: se muestra el puntaje de la palabra, 
      las letras restantes de la mano y se le pide al usuario que ingrese 
      otra palabra.

    * La suma de los puntajes de las palabras se presenta una vez que la mano termina.

    * La mano termina cuando no hay más letras sin usar.
      El usuario también puede terminar la mano ingresando dos signos de exclamación
      ('!!') en vez de una palabra.

      mano: diccionario (string -> int)
      lista_palabras: lista de cadenas en minúsculas.
      retorna: el puntaje total de la mano
      
    """
    
    """
    # PSEUDO-CODIGO
    # Llevar registro del puntaje total
    
    # Mientras haya letras en la mano o el usuario no ingrese '!!':
    
        # Mostrar la mano
        
        # Pedirle al usuario que ingrese una palabra
        
        # Si la entrada son dos signos de exclamación, se termina el juego
                    
        # Sino (la entrada no son dos signos de exclamación):

            # Si la palabra es válida:

                # Mostrarle al usuario los puntos que ganó,
                # y el puntaje total de la mano hasta ese momento.

            # Sino (la palabra no es válida):
                # Rechazar palabra inválida (mostrar un mensaje)
                
            # actualizar la mano del usuario eliminando las letras 
            # que usó en la palabra (aún si la palabra era inválida)
            

    # Se terminó el juego (el usuario se quedó sin letras o ingresó '!!'),
    # se le muestra el puntaje final de la mano.

    # Retorna el puntaje final como resultado de la función.
    """


#
# Problema #6: Jugar una partida completa
# 


#
# procedimiento para reemplazar una letra en la mano
#

def intercambiar_mano(mano, letra):
    
    mano_copia = mano.copy()
    print(mano_copia)
    letras = VOCALES + CONSONANTES
    
    if letra in mano_copia:
        cantidad_letra = mano_copia.pop(letra)
        print("Cantidad de la letra a eliminar:", cantidad_letra)
        
        nueva_letra = random.choice(letras)
        while nueva_letra in mano_copia:  # Si existe nueva_letra , crea otra
            nueva_letra = random.choice(letras)
            
        mano_copia[nueva_letra] = cantidad_letra
    
    print(" ")
    mostrar_mano(mano_copia)
    print(mano_copia)
    return mano_copia
    
    """
    Permite al usuario reemplazar todas las copias de una letra en la mano 
    (elegida por el usuario) por una nueva letra elegida, al azar, de VOCALES 
    y CONSONANTES. La nueva letra debe ser diferente a la elegida para intercambiar, 
    y no puede ser ninguna de las letras que ya tiene en la mano.
    
    Si el usuario ingresa una letra que no está en la mano, la mano debe quedar igual.
    
    No se debe modificar la mano original.
    Por ejemplo:
        intercambiar_mano({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    puede resultar en:
        {'h':1, 'e':1, 'o':1, 'x':2} -> si la nueva letra es 'x'
    La nueva letra no debe ser 'h', 'e', 'l', u 'o' ya que esas letras ya están en 
    la mano.
    
    mano: diccionario (string -> int)
    letra: string
    retorna: diccionario (string -> int)
    """
    
    
#
# Problema #1: Armar esqueleto del ciclo de juego
#       
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
    
    pass

def jugar_partida(lista_palabras):
   
   Bienvenida ()
   print("+++++++++++++++++++++++++++++++++++++++")
   print(" ")
   cantidad_manos = None

   while cantidad_manos is None:
        input_cantidad_manos = input("Ingrese la cantidad de manos a jugar: ")
        
        try:
            cantidad_manos = int(input_cantidad_manos)
            
            if cantidad_manos <= 0:
                print("La cantidad de manos debe ser un número positivo.")
                cantidad_manos = None
        except ValueError:
            print("Ingrese un número válido para la cantidad de manos.")

    
   mano = repartir_mano(TAMANIO_MANO)
    

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
   
   
   
   
   
   
     # if palabra.lower() in lista_palabras:
     #    print('La palabra {} se encuentra en la lista.')
     # else:
     #    print('La palabra {} NO se encuentra en la lista.')
        
    # while (total_manos>0):
    #         print("Jugando Mano")
            
    #         mano = repartir_mano(TAMANIO_MANO)
    #         mostrar_mano(mano)
            
    #         if (intercambiar_letra != 0):
                
    #             intercambio = bool(input ("Desea intercambiar mano?? si/no"))
    #             if intercambio == ("si"):
    #                 print("True")
                        
    #                 letra = input("Ingresar letra a intercambiar: ")
                    
    #                 cambio_letra = intercambiar_mano(mano, letra)
    #                 print (mostrar_mano(cambio_letra))
                    
    #                 intercambiar_letra -= 1               
                
    #             if intercambio == ("no"):
                
    #                 print("False")
                    
    #                 intercambiar_letra = 0
                
    #         else:
                
    #             print("Jugando mano actual")
                
    #             intercambiar_letra = 0
                
    #             if (repitio_mano):
    #               #  obtener_puntaje_palabra(palabra, )
    #             else:
    #                 bool(input("Desea repetir la mano actual??: "))
                    
                    
    #         total_manos -= 1
            
        
    
   """
    Permitir al usuario jugar una serie de manos (partida)

    * Pedir al usuario que ingrese un número total de manos.

    * Acumular el puntaje de cada mano en un puntaje total para la partida.
 
    * Por cada mano, antes de empezar a jugar, preguntar al usuario si quiere
      intercambiar una letra por otra. Esto se puede hacer sólo una vez durante 
      el juego. Una vez que se usa esta opción, no se le debe preguntar nuevamente 
      al usuario si quiere intercambiar una letra durante el juego.
    
    * Por cada mano, preguntar al usuario si desea volver a jugar la mano.
      Si el usuario ingresa 'si', se repetirá la mano y se mantendrá el mayor
      de los dos puntajes obtenidos para esa mano. Esto se puede hacer una única vez
      durante la partida. Una vez que se utiliza la opción de volver a jugar una mano,
      no se debe volver a preguntar si desea volver a jugar futuras manos. Volver a
      jugar una mano no afecta el número de manos totales que el usuario eligió jugar.
      
            * Nota: si se vuelve a jugar una mano, no se podrá elegir reemplazar una
              letra (se debe jugar con la mano original)
      
    * Devuelve el puntaje total de la partida.

    lista_palabras: lista de cadenas en minúsculas
    """
    
    #print("jugar_partida no implementado.") # TO DO... Eliminar esta linea cuando se implemente la función.
    


#
# Construye las estructuras de datos necesarias para jugar la partida.
# No eliminar la condición "if __name__ == '__main__':" Este código se ejecuta
# cuando el programa se ejecuta directamente, sin usar la sentencia import.
#
if __name__ == '__main__':
    lista_palabras = cargar_palabras()
    jugar_partida(lista_palabras)
    
    
    print("+++++++++++++++++++++")
    print("","   FIN DEL JUEGO   ","",sep="|")
    print("+++++++++++++++++++++")
  
   