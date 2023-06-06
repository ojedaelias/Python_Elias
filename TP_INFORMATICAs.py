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
    datosMatriz = []
    try:
        #with open("locales-en-venta-2020.csv", 'r',encoding = 'utf-8') as archivo:
        with open("locales-en-venta-2020.csv", 'r',encoding = 'utf-8') as archivo:      
            lector = csv.reader(archivo)                    
            for fila in lector:                               
                datosMatriz.append(fila)
    except EOFError:
        print("No se pudo abrir el archivo correctamente")
    
    columnas = None
    for i in range(len(datosMatriz[0])+1):
        columnas = i
    
    matriz = matrizNula(len(datosMatriz),columnas)  
    cargarMatriz(matriz, datosMatriz)
    return matriz,columnas                                              # del archivo

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
def subMenu():
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


#--------------Validacion que este cargada la matriz antes de trabajarla----------------#
def validacion(x):
    while x == []:
            print('Debes cargar los datos antes de trabajar con ellos')
            Menu = Menu()
            if Menu == 1:
                x = cargarArchivo()
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
#agregarRegistros(matriz,columnas)
mostrarMatriz(matriz)



#-------------------------------Programa principal-------------------------------#
Menu = Menu()
while Menu != 1 and Menu != 2 and Menu != 3 and Menu != 4 and Menu != 5:
    print('El numero ingresado no corresponde a ninguna de las opciones')
    Menu = Menu()
while Menu != 5: 
    if Menu == 1:
        cargarArchivo()
    elif Menu == 2:
        while datosArchivos == []:
            datosArchivos = validacion(datosArchivos)
        subMenu = subMenu()
        while subMenu != 1 and subMenu != 2 and subMenu != 3 and subMenu != 4:
            print('El numero ingresado no corresponde a ninguna de las opciones')
            subMenu =subMenu()
        if subMenu == 1:
        elif subMenu == 2:
        elif subMenu == 3:            
        elif su Menu == 4:
    elif Menu == 3:
        if datosArchivos == []
            datosArchivos = validacion(datosArchivos)
    elif Menu == 4:

       
        

#cargarArchivo()      #cargar archivos punto 1































#----------------------AGREGAR REGISTROS DE NUEVOS LOCALES----------------------#

    

