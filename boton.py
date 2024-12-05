from activarAlarma import activar_alarma
from desactivarAlarma import desactivar_alarma
from pir import detectar_movimiento
from time import sleep
from machine import Pin

# Función asincrónica para el manejo del botón
def funcion_boton(button, led_verde, led_rojo, buzzer, sensor_pir, codigo_correcto, lcd, estado_alarma):
    ultimo_estado_boton = True

    while True:
        estado_boton = button.value()
        
        if estado_boton == 0 and ultimo_estado_boton == 1:
            if estado_alarma == 1:  
                estado_alarma = activar_alarma(led_verde, led_rojo, buzzer, sensor_pir, lcd)
            else:
                estado_alarma = desactivar_alarma(led_rojo, led_verde, buzzer, codigo_correcto, lcd)
                
            ultimo_estado_boton = estado_boton
            sleep(0.1)
        
        elif estado_boton == 1:
            ultimo_estado_boton = estado_boton 
        
        if estado_alarma == 0:
            detectar_movimiento(estado_alarma, buzzer, sensor_pir, lcd)
            
        if buzzer.value() == 1:
            led_rojo.toggle()
        sleep(0.1)