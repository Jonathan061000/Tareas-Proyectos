# Combinaciones posibles de monedas
def encontrar_combinaciones(cantidad_restante, monedas_disponibles):  #Funcion para encontrar las combinaciones, con 2 parametros
   
    if cantidad_restante == 0: #Indica que hay una combinacion valida, y que no se necesitan mas monedas 
        return [[]]
    
    if cantidad_restante < 0: #Indica que que la combinacion ha excedido la cantidad deseada y no es valida
        return[]
   
    combinaciones_encontradas = [] #Se crea una lista vacia que almacenara las combinaciones validas que se encuentren

    for indice, moneda in enumerate(monedas_disponibles): #Se usa un for para iterar sobre "monedas_disponibles", usando enumerate para obtener el indice y el valor de cada moneda
        if moneda <= cantidad_restante: #Se comprueba si la moneda actual es menor o igual que que la cantidad restante, puede ser utilizada
            cantidad_nueva = cantidad_restante - moneda #Se calcula una nueva cantidad, que es la que se necesita alcanzar despues de usar la moneda actual
            for combinacion in encontrar_combinaciones(cantidad_nueva, monedas_disponibles[indice:]): #Se llama a la funcion de manera recursiva, para encontrar combinaciones que nos den la nueva cantidad, permitiendo el uso de la misma moneda en la combinacion
                combinaciones_encontradas.append([moneda] + combinacion) # Para cada combinacion valida, se suma la moneda actual a esa combinacion y se agregan a lista "combinaciones encontradas"
    return combinaciones_encontradas #Se devuelven todas las combinaciones encontradas

def total_combinaciones(combinaciones): #Funcion para mostrar las cobinaciones encontradas, con un parametro que es una lista de las combinaciones de monedas que e encontraron
    if not combinaciones: #Se comprueba si la lista esta vacia, y en este caso se indica que no se encontraron combinaciones
        print(" No se encontraron combinaciones posibles")
        return
    for indice, combinacion in enumerate(combinaciones): #Se itera sobre cada combinacion encontrada
        diccionario_combinacion = {} #Se crea un diccionario para contar cuantas monedas de cada tipo se tiene en la combinacion
        for moneda in combinacion: # Para cada moneda en la combinacion, se incrementa sun conteo en el diccionario, usando "get" para obtener el valor actual e incrementarlo
            diccionario_combinacion[moneda] = diccionario_combinacion.get(moneda, 0) + 1
        print(f"Combinacion {indice + 1}:") # Se imprime el indice del numero de combinacion mas 1 
        for moneda, cantidad in diccionario_combinacion.items(): #Se imprimen indicando cuantas monedas de cada tipo se utilizan en la combinacion
            print(f"{cantidad} monedas de {moneda} pesos")
        print()

monedas_disponibles = [50, 20, 10, 5, 1] #Se crea una lista que contiene las denomiaciones o valores de cada moneda que se utilizara en las combinaciones

try:
    cantidad_deseada = int(input("Ingrese la cantidad: ")) #Se solicita al usuario que ingrese la cantidad de la cual requiere las combinaciones
    if cantidad_deseada <= 0: #Si la cantidad es <= 0 se imprime un mesaje que indica que debe ser un numero entero mayor a cero
        print("La cantidad debe ser un numero entero mayor a cero")
    else: # Si la cantidad es valida, se llama a la funcion "encontrar_combinaciones" para obtener las combinaciones posibles
        combinaciones_posibles = encontrar_combinaciones(cantidad_deseada, monedas_disponibles)
        print(f"Se encontraron {len(combinaciones_posibles)} combinaciones posibles") #Se muestra en numero de combinaciones  que se encontraron
        total_combinaciones(combinaciones_posibles) #Se muestran todas las combinaciones encontradas
except ValueError: #Si la cantidad ingresada no es valida se muestra un mensaje de error, solicitanco una cantidad valida
    print("Por favor, ingrese un numero entero valido")


