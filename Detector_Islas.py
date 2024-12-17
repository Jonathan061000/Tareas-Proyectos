import numpy as np
matriz=np.matrix([[1,0,0,0,0,1],
                  [0,1,0,1,1,1],
                  [0,0,0,1,1,1],
                  [0,1,0,0,0,0],
                  [1,0,1,0,1,0],
                  [1,0,1,0,1,0]])

Islas = 0 #Variable para contar el numero de islas
F,C = np.shape(matriz) #Dimensiones de la matriz, (F= Filas, C= Columnas)
CO= [] #Lista para guardar coordenadas de las celdas que forman parte de la isla
visitas = np.zeros((F,C),dtype=bool) #Matriz booleana de dimensiones iguales a "matriz", con todas las celdas en false(no visitada)
posicion=[(-1,0),(1,0),(0,-1),(0,1)] #Lista con las 4 direcciones posibles, para explorar desde cualquier celda

def numIslas(i,j):  #Funcion para buscar en las celdas
    visitas[i,j] = True #Se marca la posición como visitada, poniendo "true" en esa posicion en la matriz "visitas"
    CO.append([i,j]) #Se añade la coordenada a la lista "CO"
    for dir in posicion: #Se recorre cada direccion en la lista posicion
        ni,nj = i + dir[0], j + dir[1] #Se calcula las nuevas coordenadas "ni" y "nj"
        if 0 <= ni < F and 0 <= nj < C and matriz[ni,nj] == 1 and not visitas[ni,nj]: #Verifica limites, que el valor sea 1 y que no halla sido visitada la coordenada
            numIslas(ni,nj) #Llama a "numIslas" recursivamente para explorar la celda adyacente

for i in range (F): #Para recorrer todas las filas de "matriz"
    for j in range (C): #Para recorrer todas las columnas de "matriz"
        if matriz[i,j] == 1 and not visitas[i,j]: # Para verificar que la celda contiene un 1 y que no se halla visitado ya
            Islas +=1 #Aumenta el contador de la variable "numIslas" en 1
            numIslas(i,j) #Se llama a la funcion "numIslas" para explorar las celdas conentadas a la celda actual


print(matriz) #Se imprime la matriz
print(f"Dimensiones de la matriz: Filas:{F} y columnas: {C}\n") #Se imprimen las dimenciones de la matriz: Filas y columnas
print(f"Numero total de islas: {Islas}") #Se imprime el numero total de islas que se encuentran en la matriz



