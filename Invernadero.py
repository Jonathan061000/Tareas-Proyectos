class SensorTemperatura:
    def __init__(self, temperatura_actual):
        self.temperatura_actual = temperatura_actual
        self.temperatura_objetivo = 25 #Temperatura en °C
    def actualizar_temperatura(self, nueva_temperatura):
        self.temperatura_actual = nueva_temperatura
class SensorHumedad:
    def __init__(self, humedad_actual):
        self.humedad_actual = humedad_actual
        self.humedad_objetivo = 50 #Humedad objetivo en porcentaje
    def actualizar_humedad(self, nueva_humedad):
        self.humedad_actual = nueva_humedad
class ActuadorLuz:
    def __init__(self, estado_luz):
        self.estado_luz = estado_luz #True: encencido, False: apagado
    def ajustar_luz(self, encender):
        self.estado_luz = encender
    
class ControladorInvernadero:
    def __init__(self):
        self.sensor_temperatura = SensorTemperatura(20) #Temperatura inicial
        self.sensor_humedad = SensorHumedad(40) #Humedad inicial
        self.actuador_luz = ActuadorLuz(False) #Luz apagada al inicio
    def controlar(self):
        #Controlar temperatura
        if self.sensor_temperatura.temperatura_actual < self.sensor_temperatura.temperatura_objetivo:
            print("Ajustando calefaccion...")
            self.sensor_temperatura.actualizar_temperatura(self.sensor_temperatura.temperatura_actual + 1)
        elif self.sensor_temperatura.temperatura_actual > self.sensor_temperatura.temperatura_objetivo:
            print("Ajustando refrijeracion...")
            self.sensor_temperatura.actualizar_temperatura(self.sensor_temperatura.temperatura_actual - 1)
        #Controlar humedad
        if self.sensor_humedad.humedad_actual < self.sensor_humedad.humedad_objetivo:
            print("Activando humidificador...")
            self.sensor_humedad.actualizar_humedad(self.sensor_humedad.humedad_actual +1)
        elif self.sensor_humedad.humedad_actual > self.sensor_humedad.humedad_objetivo:
            print("Activando deshumidificador...")
            self.sensor_humedad.actualizar_humedad(self.sensor_humedad.humedad_actual - 1)
        #Contolar luz (por ejemplo encencer si la temperatura es baja)
        if self.sensor_temperatura.temperatura_actual < 22 and not self.actuador_luz.estado_luz:
            print("Encenciendo luz..")
            self.actuador_luz.ajustar_luz(True)
        elif self.sensor_temperatura.temperatura_actual > 22 and self.actuador_luz.estado_luz:
            print("Apagando luz...")
            self.actuador_luz.ajustar_luz(False) 
# Ejemplo de uso
controlador = ControladorInvernadero()
# Simulando el monitoreo y control en un bucle
for i in range(10):
    print(f"Estado actual: Temp: {controlador.sensor_temperatura.temperatura_actual}°C, "
          f"Humedad: {controlador.sensor_humedad.humedad_actual}%, "
          f"Luz: {'Encendida' if controlador.actuador_luz.estado_luz else 'Apagada'}")
    controlador.controlar()  # Ejecutar el controlador