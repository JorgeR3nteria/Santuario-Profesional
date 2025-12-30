# Ejercicio 1:
# Escribe una función    
#     verificar_sistema(encendido, conectado)
# Debe devolver:
# * "Sistema apagado" si encendido es False
# * "Sin conexión" si está encendido pero no conectado
# * "Sistema operativo" si ambos son True

def verificar_sistema (encendido, conectado):
    if not encendido:
        return "Sistema apagado"
    if not conectado:
        return "Sin conexión"
    return "Sistema operativo"
estado = verificar_sistema(True, True)
print (estado)