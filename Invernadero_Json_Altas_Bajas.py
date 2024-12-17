import json
import os

class SensorTemperatura:
    def __init__(self, temperatura_actual):
        self.temperatura_actual = temperatura_actual
        self.temperatura_objetivo = 25  # Temperatura objetivo en °C

    def actualizar_temp(self, nueva_temperatura):
        self.temperatura_actual = nueva_temperatura


class SensorHumedad:
    def __init__(self, humedad_actual):
        self.humedad_actual = humedad_actual
        self.humedad_objetivo = 50  # Humedad objetivo en porcentaje

    def actualizar_humedad(self, nueva_humedad):
        self.humedad_actual = nueva_humedad


class SensorNutrientes:
    def __init__(self, nivel_actual):
        self.nivel_actual = nivel_actual
        self.nivel_objetivo = 7  # Nivel objetivo de pH (valor entre 6 y 8)

    def actualizar_nivel(self, nuevo_nivel):
        self.nivel_actual = nuevo_nivel


class ActuadorLuz:
    def __init__(self, estado_luz):
        self.estado_luz = estado_luz  # True: encendida, False: apagada

    def ajustar_luz(self, encender):
        self.estado_luz = encender


class ActuadorNutrientes:
    def __init__(self, nutrientes):
        self.nutrientes = nutrientes  # True: añadiendo nutrientes, False: no

    def ajustar_nutrientes(self, añadir):
        self.nutrientes = añadir


class ControladorInvernadero:
    def __init__(self):
        self.sensor_temperatura = SensorTemperatura(23)  # Temperatura inicial
        self.sensor_humedad = SensorHumedad(45)  # Humedad inicial
        self.sensor_nutrientes = SensorNutrientes(7.5)  # Nutrientes iniciales (pH)
        self.actuador_luz = ActuadorLuz(False)  # Luz apagada al inicio
        self.actuador_nutrientes = ActuadorNutrientes(False)  # Nutrientes no añadidos al inicio

    def controlar(self):
        # Controlar temperatura
        if self.sensor_temperatura.temperatura_actual < self.sensor_temperatura.temperatura_objetivo:
            print("Ajustando calefacción...")
            self.sensor_temperatura.actualizar_temp(self.sensor_temperatura.temperatura_actual + 1)
        elif self.sensor_temperatura.temperatura_actual > self.sensor_temperatura.temperatura_objetivo:
            print("Ajustando refrigeración...")
            self.sensor_temperatura.actualizar_temp(self.sensor_temperatura.temperatura_actual - 1)

        # Controlar humedad
        if self.sensor_humedad.humedad_actual < self.sensor_humedad.humedad_objetivo:
            print("Activando humidificador...")
            self.sensor_humedad.actualizar_humedad(self.sensor_humedad.humedad_actual + 1)
        elif self.sensor_humedad.humedad_actual > self.sensor_humedad.humedad_objetivo:
            print("Activando deshumidificador...")
            self.sensor_humedad.actualizar_humedad(self.sensor_humedad.humedad_actual - 1)

        # Controlar nivel de nutrientes
        if self.sensor_nutrientes.nivel_actual < self.sensor_nutrientes.nivel_objetivo:
            print("Añadiendo nutrientes...")
            self.sensor_nutrientes.actualizar_nivel(self.sensor_nutrientes.nivel_actual + 0.1)
            self.actuador_nutrientes.ajustar_nutrientes(True)
        elif self.sensor_nutrientes.nivel_actual > self.sensor_nutrientes.nivel_objetivo:
            print("Reduciendo nutrientes...")
            self.sensor_nutrientes.actualizar_nivel(self.sensor_nutrientes.nivel_actual - 0.1)
            self.actuador_nutrientes.ajustar_nutrientes(False)

        # Controlar luz 
        if self.sensor_temperatura.temperatura_actual < 22 and not self.actuador_luz.estado_luz:
            print("Encendiendo luz...")
            self.actuador_luz.ajustar_luz(True)
        elif self.sensor_temperatura.temperatura_actual > 22 and self.actuador_luz.estado_luz:
            print("Apagando luz...")
            self.actuador_luz.ajustar_luz(False)


class ManejoArchivos:
    def __init__(self, archivo):
        self.archivo = archivo
        # Crear archivo si no existe
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump([], f)

    def alta(self, datos):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Añadir nuevos datos
        registros.append(datos)
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def baja(self, indice):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Eliminar por índice
        if 0 <= indice < len(registros):
            registros.pop(indice)
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def modificar(self, indice, nuevos_datos):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Modificar el registro por índice
        if 0 <= indice < len(registros):
            registros[indice] = nuevos_datos
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def consultar(self):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        return registros


def mostrar_menu():
    print("\nMenú del Invernadero Automatizado:")
    print("1. Alta (Guardar nueva configuración)")
    print("2. Baja (Eliminar una configuración por índice)")
    print("3. Modificación (Modificar una configuración por índice)")
    print("4. Consultas (Mostrar todas las configuraciones guardadas)")
    print("5. Salir")
    return input("Seleccione una opción: ")


def main():
    invernadero = ControladorInvernadero()
    archivo = ManejoArchivos("Configuraciones.json")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":  # Alta
            try:
                temp = float(input("Temperatura: "))
                hum = float(input("Porcentaje de Humedad: "))
                nut = float(input("Nutrientes: "))
                luz = input("Luz (encender/apagar): ").lower() == 'encender'
                datos = {
                    "temperatura": temp,
                    "humedad": hum,
                    "nutrientes": nut,
                    "luz": luz
                }
                invernadero.controlar()  # Controlar el ambiente según los valores capturados
                archivo.alta(datos)
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        elif opcion == "2":  # Baja
            try:
                indice = int(input("Ingrese el índice de la configuración que desea eliminar: "))
                archivo.baja(indice)
                print("Configuración eliminada exitosamente.")
            except ValueError:
                print("Error: Ingrese un índice válido.")
            except IndexError:
                print("Error: Índice fuera de rango.")

        elif opcion == "3":  # Modificación
            try:
                indice = int(input("Ingrese el índice de la configuración que desea modificar: "))
                temp = float(input("Nueva temperatura: "))
                hum = float(input("Nuevo porcentaje de humedad: "))
                nut = float(input("Nuevo porcentaje de nutrientes: "))
                luz = input("Nuevo estado de luz (encender/apagar): ").lower() == 'encender'
                datos = {
                    "temperatura": temp,
                    "humedad": hum,
                    "nutrientes": nut,
                    "luz": luz
                }
                invernadero.controlar()  # Controlar el ambiente según los valores modificados
                archivo.modificar(indice, datos)
                print("Configuraciones modificadas exitosamente.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            except IndexError:
                print("Error: Índice fuera de rango.")
        
        elif opcion == "4":  # Consultas
            configuraciones = archivo.consultar()
            if configuraciones:
                for i, config in enumerate(configuraciones):
                    print(f"Configuración {i}: Humedad={config['humedad']}, Temperatura={config['temperatura']}, Nutrientes={config['nutrientes']}, Luz={config['luz']}")
            else:
                print("No hay configuraciones guardadas.")
        
        elif opcion == "5":  # Salir
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción del menú.")


if __name__ == "__main__":
    main()


controlador = ControladorInvernadero()

# Simulando el monitoreo y control en un bucle
for i in range(10):
    print(f"Estado actual: Temp: {controlador.sensor_temperatura.temperatura_actual}°C, "
          f"Humedad: {controlador.sensor_humedad.humedad_actual}%, "
          f"Nutrientes: {controlador.sensor_nutrientes.nivel_actual} pH, "
          f"Luz: {'Encendida' if controlador.actuador_luz.estado_luz else 'Apagada'}, "
          f"Nutrientes: {'Añadiendo' if controlador.actuador_nutrientes.nutrientes else 'No añadiendo'}")
    
    # Ejecutar el controlador
    controlador.controlar()
