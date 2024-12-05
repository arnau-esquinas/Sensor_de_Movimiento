from time import sleep, localtime
import os

DIFERENCIA_HORARIA = 1 
# Función para detectar movimiento  
def escribir_log(mensaje):
    try:
        # Verificar si el archivo existe
        fecha_hora = localtime()
        hora_ajustada = (fecha_hora[3] + DIFERENCIA_HORARIA) % 24
        
        if not "dec_movimiento.log" in os.listdir():
            print("El archivo de log no existe. Creándolo...")

        # Obtener la fecha y hora actual
        fecha_hora_str = "{:02d}/{:02d}/{:04d} {:02d}:{:02d}:{:02d}".format(
            fecha_hora[2], fecha_hora[1], fecha_hora[0],  # Día, Mes, Año
            hora_ajustada, fecha_hora[4], fecha_hora[5]   # Hora ajustada, Minuto, Segundo
        )
        # Crear el mensaje con la fecha y hora
        log_mensaje = f"{fecha_hora_str} - {mensaje}"

        # Escribir el mensaje en el archivo de log
        with open("dec_movimiento.log", "a") as log:
            log.write(log_mensaje + "\n")
    except Exception as e:
        print("Error al escribir en el log:", e)
