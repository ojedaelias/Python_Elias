#-------------------------------Definir librerias-------------------------------------#
import csv

from random import *
#-------------------------------Definicion de funciones-------------------------------#
#-----------Matriz-----------#    
def matrizNula(m,n):                                    # Crea una matriz con valor None de longitud m*n
	matriz = [None] * m                                 # Define una lista matriz con n COLUMNAS
	for i in range(m):                                  # Recorre la lista y en cada columna almacena n FILAS
		matriz[i] = [None] * n
	return matriz

def cargarMatriz(M,D):                         # Llena una matriz "M" con datos "D"
	for i in range(len(M)):                    
		for j in range(len(M[0])):
			M[i][j] = D[i][j]

def mostrarMatriz(M):                              # Muestra la matriz "M" en la terminal
	for i in range(len(M)):
		print("\n")
		for j in range(len(M[0])):
			print(M[i][j], end = "\t")


#Abrir archivo como matriz
def cargarArchivo():                                    
    datosArchivos = []                                                              
    with open("locales-en-venta-2020.csv", 'r', encoding='utf-8') as archivo:          # Abre el archivo y lo llama "archivo", lo lee 
        lector = csv.reader(archivo)                                                   # y guarda lo leido en la variable "lector"
        for fila in lector:                               
            datosArchivos.append(fila)                                                 # Recorre al archivo guardado en lector y
    print(len(datosArchivos)) #VER COMO CALCULAR LAS COLUMNAS Y FILAS                  # lo almacena en la lista "datosArchivos"
    matriz = matrizNula(len(datosArchivos), 11)                                        # Crea una matriz "vacia" de la longitud 
    cargarMatriz(matriz, datosArchivos)                                                # del archivo

    return matriz
#-----------Menu-----------#
def Menu():
    x = int(input('''Seleccione la opcion que desee realizar:
    1. Cargar los datos del archivo "locales-en-venta-2020.csv"
    2. Generar estadísticas. Debe desplegar un submenú únicamente al escoger la opción mostrando las 
    diferentes opciones de resultados a generar.
    3. Agregar registros de nuevos locales.
    4. Actualizar los datos en el archivo locales-en-venta-2020.csv
    5. Salir
    Ingrese el numero de la opcion que quiera seleccionar'''))
    return x
    
#-----------Submenu-----------#
def su subMenu():
    x = int(input('''Seleccione la opcion que desee realizar:
    1. Generar el archivo semestre1.csv que contenga los datos de locales en venta de los trimestres 
    PRIMER y SEGUNDO
    2. Generar el archivo galeriaEstrenar.csv que contenga los datos de locales en venta en galerías, y 
    con antigüedad 0.
    3. Mostrar los locales en venta con mayor precio en cada barrio
    4. Generar un archivo con el promedio de superficies de locales con más de 10 años de 
    antigüedad
    Ingrese el numero de la opcion que quiera seleccionar'''))
    return x




#-----------Agregar datos-----------#
def agregarRegistros(M,C):                                            # Agrega registros a la amtriz "M"
    datos = []
    for i in range(columnas):
        col = matriz[0][i]    
        datos.append(input("Ingrese el dato "+col+": "))
    #print(datos)
    #cargarMatriz(M,datos)
        #print(M)
                        
    for j in range(len(M[0])):
        M[0].append(datos[j])
    #print(M)
    return datos

matriz,columnas = cargarArchivo()
agregarRegistros(matriz,columnas)
#mostrarMatriz(matriz)



#-------------------------------Programa principal-------------------------------#
print('este es el menu')
print('Git hub es una verga una recontra verga')
while Menu() != 5: 
    if Menu() == 1:
        cargarArchivo()
    elif Menu() == 2:
        if datosArchivos == []:
            print('Debes cargar los datos antes de trabajar con ellos')
        else:
            if subMenu() == 1:
            elif subMenu() == 2:
            elif subMenu() == 3:
            elif subMenu() == 4:
    elif Menu() == 3:
    elif Menu() == 4:
       
        

#cargarArchivo()      #cargar archivos punto 1































#----------------------AGREGAR REGISTROS DE NUEVOS LOCALES----------------------#

    

