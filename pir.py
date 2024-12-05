from machine import Pin, PWM
from time import sleep
from log import escribir_log

def detectar_movimiento(estado_alarma, buzzer, sensor_pir, lcd):

    # Detectar movimiento
    if sensor_pir.value() == 1:  # Movimiento detectado (cambio de 0 a 1)
        print("¡Movimiento detectado!")  # Mensaje de depuración
        lcd.mostrar_mensaje("¡Movimiento Detectado!")  # Mostrar mensaje en LCD
        buzzer.value(1)  # Encender el buzzer
        escribir_log("Buzzer Activado")
    if sensor_pir.value() == 0:
        print("NO")
    sleep(0.2)