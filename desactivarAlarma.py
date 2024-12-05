from comprobarContra import comprobar_contra
from time import sleep
from lcd import LCD
from pir import detectar_movimiento
from log import escribir_log

def desactivar_alarma(led_rojo, led_verde, buzzer, codigo_correcto, lcd):
    
    # Llamar a la función para introducir y verificar el código
    if comprobar_contra(codigo_correcto, 0, lcd):
        led_rojo.off()
        led_verde.on()
        buzzer.value(0)
        print("Alarma desactivada.")
        lcd.mostrar_mensaje("Alarma desactivada.")
        detectar_movimiento
        return 1

    # Código incorrecto
    buzzer.value(1)
    escribir_log("Buzzer Activado")
    sleep(0.5)
    print("Codigo incorrecto. La alarma sigue activada.")
    lcd.mostrar_mensaje("Codigo incorrecto")
    return 0