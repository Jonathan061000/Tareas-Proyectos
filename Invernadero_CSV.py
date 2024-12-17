import csv

class SensorTemperatura:
    def __init__(self, temperatura_actual):
        self.temperatura_actual = temperatura_actual
        self.temperatura_objetivo = 25  # Temperatura objetivo en °C

    def actualizar_temperatura(self, nueva_temperatura):
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
        self.sensor_temperatura = SensorTemperatura(20)  # Temperatura inicial
        self.sensor_humedad = SensorHumedad(40)  # Humedad inicial
        self.sensor_nutrientes = SensorNutrientes(6.5)  # Nutrientes iniciales (pH)
        self.actuador_luz = ActuadorLuz(False)  # Luz apagada al inicio
        self.actuador_nutrientes = ActuadorNutrientes(False)  # Nutrientes no añadidos al inicio

    def controlar(self):
        # Controlar temperatura
        if self.sensor_temperatura.temperatura_actual < self.sensor_temperatura.temperatura_objetivo:
            print("Ajustando calefacción...")
            self.sensor_temperatura.actualizar_temperatura(self.sensor_temperatura.temperatura_actual + 1)
        elif self.sensor_temperatura.temperatura_actual > self.sensor_temperatura.temperatura_objetivo:
            print("Ajustando refrigeración...")
            self.sensor_temperatura.actualizar_temperatura(self.sensor_temperatura.temperatura_actual - 1)

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
        # Controlar luz (por ejemplo, encender si la temperatura es baja)
        if self.sensor_temperatura.temperatura_actual < 22 and not self.actuador_luz.estado_luz:
            print("Encendiendo luz...")
            self.actuador_luz.ajustar_luz(True)
        elif self.sensor_temperatura.temperatura_actual > 22 and self.actuador_luz.estado_luz:
            print("Apagando luz...")
            self.actuador_luz.ajustar_luz(False)

    # Metodo para guardar datos en un archivo CSV
    def guardar_datos_csv(self, archivo):
        with open(archivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                self.sensor_temperatura.temperatura_actual,
                self.sensor_humedad.humedad_actual,
                self.sensor_nutrientes.nivel_actual,
                'Encendida' if self.actuador_luz.estado_luz else 'Apagada',
                'Añadiendo' if self.actuador_nutrientes.nutrientes else 'No añadiendo'
            ])

controlador = ControladorInvernadero()

# Crear el archivo CSV con los encabezados
archivo_csv = 'Datos_invernadero.csv'
with open(archivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Temperatura (°C)', 'Humedad (%)', 'Nutrientes (pH)', 'Luz', 'Nutrientes (Estado)'])
    
# Simulando el monitoreo y control en un bucle
for i in range(10):
    print(f"Estado actual: Temp: {controlador.sensor_temperatura.temperatura_actual}°C, "
          f"Humedad: {controlador.sensor_humedad.humedad_actual}%, "
          f"Nutrientes: {controlador.sensor_nutrientes.nivel_actual} pH, "
          f"Luz: {'Encendida' if controlador.actuador_luz.estado_luz else 'Apagada'}, "
          f"Nutrientes: {'Añadiendo' if controlador.actuador_nutrientes.nutrientes else 'No añadiendo'}")
    
    # Ejecutar el controlador
    controlador.controlar()
    # Guardar los datos en el archivo CSV
    controlador.guardar_datos_csv(archivo_csv)