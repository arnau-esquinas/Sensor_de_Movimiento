from time import sleep
from machine import Pin, I2C
from activarAlarma import activar_alarma
from desactivarAlarma import desactivar_alarma
from pir import detectar_movimiento
from lcd import LCD
from boton import funcion_boton
import os


# Declaración de los elementos
buzzer = Pin(27, Pin.OUT)  
led_rojo = Pin(19, Pin.OUT)  
led_verde = Pin(20, Pin.OUT)  
button = Pin(26, Pin.IN, Pin.PULL_UP)  
sensor_pir = Pin(28, Pin.IN)  
i2c = I2C(0, scl=Pin(17), sda=Pin(16))  
lcd = LCD(16, 17)  
codigo_correcto = "4444"
 
# Estado inicial de la alarma (global)
estado_alarma = 1  # 1 = desactivada, 0 = activada
led_verde.off()
led_rojo.off()
buzzer.value(0)
lcd.mostrar_mensaje(" ")

# Inicializa el botón en un hilo asincrónico
funcion_boton(button, led_verde, led_rojo, buzzer, sensor_pir, codigo_correcto, lcd, estado_alarma)
