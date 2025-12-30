def estado_temperatura(temp, sensor_funciona):
    if not sensor_funciona:
        return "Sensor dañado"
    if temp >= 80:
        return "Temperatura Peligrosa"
    return "Temperatura normal"
temperatura = int(input("Ingrese la temperatura: "))
sensor = True
estado = estado_temperatura(temperatura, sensor)
print(estado)