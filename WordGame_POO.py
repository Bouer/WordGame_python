# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:57:09 2023

@author: MDC
"""

import random
import math


ARCHIVO_PALABRAS = "palabras.txt"

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
    
    for i in range(5):
        print(" ")
   

def mostrar_reglas_del_juego():
    print("                         Reglas del juego:")
    print("               --------------------------------------")
    print(" * El juego consiste en formar palabras utilizando las letras disponibles.")
    print(" * Cada jugador tiene una mano de letras que puede utilizar para formar palabras.")
    print(" * Las palabras deben estar compuestas por letras válidas según el idioma del juego.")
    print("* El objetivo es obtener la mayor puntuación posible formando palabras.")
    print(" * Cada letra tiene asignado un valor numérico que determina la puntuación de la palabra.")
    print("* El juego continúa hasta que se agoten las letras en la bolsa o no sea posible formar más palabras.")
    print("\n")
    print("    ¡Buena suerte!")
    print("   -----------------")
    print("     * * * * *     ")
    print("    *          *    ")
    print("   *  A JUGAR!  *  ")
    print("    *          *     ")
    print("     * * * * *    ")
    print(" ")
    input("Presione Enter para continuar...")
    
    for i in range(15):
        print(" ")
    
class JuegoDePalabras:
    
    
    def __init__(self, archivo_palabras):
        self.lista_palabras = self.cargar_palabras(archivo_palabras)
        self.TAMANIO_MANO = 7
        self.VOCALES = 'aeiou'
        self.CONSONANTES = 'bcdfghjklmnpqrstvwxyz'
        self.VALORES_LETRAS = {
            'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
            'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'ñ': 4, 'o': 1, 'p': 3, 'q': 10,
            'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10 }

    def cargar_palabras(self, archivo_palabras):
       
       inFile = open(ARCHIVO_PALABRAS, 'r')
       
       palabras = []
       for palabra in inFile:
           palabras.append(palabra.strip().lower())
           
       return palabras

    def obtener_diccionario_frecuencias(self, secuencia):
         
        # frecuencias: diccionario
        frec = {}
        for x in secuencia:
            frec[x] = frec.get(x,0) + 1
        
        return frec

    def obtener_puntaje_palabra(self, palabra, n):
        
          longitud_palabra = sum(1 for letra in palabra if letra.isalpha())  # Contar letras válidas en la palabra
          
          primer_componente = sum(self.VALORES_LETRAS.get(letra.lower(), 0) for letra in palabra.lower())
                    
          if "*" in palabra:
              longitud_palabra += 1
          
          segundo_componente = max(7 * longitud_palabra - 3 * (n - longitud_palabra), 1)
         
          
          puntaje = primer_componente * segundo_componente
          print()
          
          
          return puntaje

    def mostrar_mano(self, mano):
         
        #keys() método  que devuelve una vista de las claves (keys) presentes en el diccionario.
        for letra in mano.keys():
            for j in range(mano[letra]):
                 print(letra, end=' ')      # Muestra todas las letras en la misma linea
        print()                             # Linea vacía

    def repartir_mano(self, n):
        mano={}
        #math.ceil() redondeado hacia arriba 
        cantidad_vocales = int(math.ceil(n / 3)) # 7/3 = 2,33 [3]
        
        
        vocales = self.obtener_diccionario_frecuencias(random.choices(self.VOCALES, k=cantidad_vocales))
        mano.update(vocales)
        #print(mano)
        
               
        mano["*"] = 1 # Agregamos el comodin
        
        consonantes = self.obtener_diccionario_frecuencias(random.choices(self.CONSONANTES,k=n-1-cantidad_vocales))
        mano.update(consonantes)
        #print(mano)
     
        return mano

    def actualizar_mano(self, mano, palabra):
       
        nueva_mano = mano.copy()  # Crear una copia de la mano original
        palabra = palabra.lower() # Convierte a minuscula la palabra   
        # Iterar sobre cada letra de la palabra
        for letra in palabra:
            if letra in nueva_mano:
                nueva_mano[letra] = max(0, nueva_mano[letra] - 1)
                #print(nueva_mano[letra])
        return nueva_mano

    def es_palabra_valida(self, palabra, mano):
      
           lista_mano = [letra  for letra, cantidad in mano.items() for _ in range(cantidad)]
           lista_mano_copy = lista_mano.copy()  # Crear una copia de la lista mano
               
           palabra_min = palabra.lower()
           palabra_sin_asterisco = ""
           
           
           if "*" in palabra_min:
               palabras_reemplazadas = [palabra_min.replace("*", vocal) for vocal in "aeiou"]
               
               
               for palabra_asterisco in palabras_reemplazadas:
                   if palabra_asterisco in self.lista_palabras:
                       
                       palabra_sin_asterisco = palabra_asterisco
                       
                       break
           else:
               
               palabra_sin_asterisco = palabra_min  
             
           
           puede_formar_palabra = True
           
                 
           if palabra_sin_asterisco in self.lista_palabras:
               
               
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

    def calcular_longitud_mano(self, mano):
        
        return sum(mano.values())-1
        

    def jugar_mano(self, mano):
        palabra = ""
        letras_en_mano = self.calcular_longitud_mano(mano)
        n = self.TAMANIO_MANO
        puntaje_total = 0
        
        
        while letras_en_mano >= 0 or palabra != "!!":
            
            print(" ")
            print("+","+",sep="------------------------")
            print("Mano actual:", end=" ")
            nueva_mano = self.actualizar_mano(mano, palabra)
            self.mostrar_mano(nueva_mano)
            print("+","+",sep="----------------------------")
            
            
            print(" ")
            palabra_anterior = palabra
            
            palabra = input("Ingrese una palabra o ""!!"" para indicar que desea terminar: ")
            
            if (self.es_palabra_valida(palabra, mano)):
                
                puntaje = self.obtener_puntaje_palabra(palabra, n)
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
                print(" La palabra no es valida")
                print("+","+",sep="------------------------", end="\n")
                
                palabra = palabra_anterior  # Restaurar la palabra anterior
                
            letras_en_mano = self.calcular_longitud_mano(mano)
            if not letras_en_mano:  # Verifica si quedan letras en la mano
                break
            
        
        
        if letras_en_mano == 0:
            
            print("+","+",sep="------------------------")
            print(" Se quedo sin letras")
            print(" Puntaje Final: {} puntos".format(puntaje_total))
            print("+","+",sep="------------------------", end="\n\n")
        elif palabra == "!!" :
            print(" ")
            print("+","+",sep="------------------------")
            print(" Puntaje Final: {} puntos".format(puntaje_total))
            print("+","+",sep="------------------------", end="\n\n")
            print("")

    def intercambiar_mano(self, mano, letra):
        mano_copia = mano.copy()
        #print(mano_copia)
        letras = self.VOCALES + self.CONSONANTES
        
        if letra in mano_copia:
            cantidad_letra = mano_copia.pop(letra)
            #print("Cantidad de la letra a eliminar:", cantidad_letra)
            
            nueva_letra = random.choice(letras)
            while nueva_letra in mano_copia:  # Si existe nueva_letra , crea otra
                nueva_letra = random.choice(letras)
                
            mano_copia[nueva_letra] = cantidad_letra
        
       # print(" ")
        #self.mostrar_mano(mano_copia)
        #print(mano_copia)
        return mano_copia

    def jugar_partida(self):
        
        Bienvenida ()
        
        mostrar_reglas_del_juego()
        
        print("+++++++++++++++++++++++++++++++++++++++")
        print(" ")
        
        cantidad_manos = None
        mano = self.repartir_mano(self.TAMANIO_MANO)
        
        comodin_intercambiarletra = 1 #Comodin cambiar letra
        comodin_repetirmano = 1 #Comodin de repetir mano
        
        while cantidad_manos is None:
            
            input_cantidad_manos = input("Ingrese la cantidad de manos a jugar: ")
             
            try:
                 cantidad_manos = int(input_cantidad_manos)
                 
                 if cantidad_manos <= 0:
                     print("La cantidad de manos debe ser un número positivo.")
                     cantidad_manos = None
            except ValueError:
                 print("Ingrese un número válido para la cantidad de manos.")
        
        print(" ")
        print("+","+",sep="----------------------------")
        print(" Mano actual: ",end=" " )
        self.mostrar_mano(mano)
        print("+","+",sep="----------------------------")

        for i in range(cantidad_manos):
            print(" ")
            print("Jugando mano número", i+1) 
            print(" ")
            
            
            mano_anterior = mano
            
            if(comodin_repetirmano != 0):
                if (i >= 1):
                    self.repetir_mano = input("¿Desea repetir la mano de la partida anterior?? ")
                    print(" ")
                    if (self.repetir_mano.lower() == "si" ):
                        print("+","+",sep="----------------------------")
                        print(" Mano actual: ",end=" " )
                        self.mostrar_mano(mano_anterior)
                        print("+","+",sep="----------------------------")
                        print(" ")
                        comodin_repetirmano = 0
                    else:
                        mano = self.repartir_mano(self.TAMANIO_MANO)
                        print("+","+",sep="----------------------------")
                        print(" Mano actual: ",end=" " )
                        self.mostrar_mano(mano)
                        print("+","+",sep="----------------------------")
                        print(" ")
                        comodin_repetirmano = 1
                                
            else:
                print("+","+",sep="-------------------------------------------------")
                print(" El comodin de repetir mano, ya fue utilizado!!")
                print("+","+",sep="-------------------------------------------------")
                print(" ")
                
                mano = self.repartir_mano(self.TAMANIO_MANO)
              
                
            intercambio_deseado = " "
            if (comodin_intercambiarletra != 0):
                while intercambio_deseado.lower() != "si" and intercambio_deseado.lower() != "no":
                    
                    intercambio_deseado = input("---- ¿Desea intercambiar una letra? (si/no): ")
                 
                    if intercambio_deseado.lower() == "si":
                        letra_para_reemplazar = input("---- ¿Qué letra desea intercambiar?: ")
                        mano_intercam = self.intercambiar_mano(mano, letra_para_reemplazar)
                        comodin_intercambiarletra = 0;
                        
                    elif intercambio_deseado.lower() == "no":
                        print(" ")
                        print("+","+",sep="-----------------------------------------")
                        print(" No se realizará ningún intercambio.")
                        print("")
                        print(" Continua teniendo el comodin para cambiar letra!!")
                        print("+","+",sep="-----------------------------------------")
                        mano_intercam = mano
                        comodin_intercambiarletra = 1;
                    else:
                        print("Opción no válida. Por favor, ingrese 'si' o 'no'.")
            else:
                print("+","+",sep="-------------------------------------------------")
                print(" El comodin para intercambiar letra, ya fue utilizado!!")
                print("+","+",sep="-------------------------------------------------")
                print(" ")
                mano_intercam = mano
            
            self.jugar_mano(mano_intercam)

   

if __name__ == '__main__':
    
    juego = JuegoDePalabras("archivo_palabras.txt")

    juego.jugar_partida()
    
    
   
    print("+++++++++++++++++++++")
    print("","   FIN DEL JUEGO   ","",sep="|")
    print("+++++++++++++++++++++")
  
