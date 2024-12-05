from time import sleep
from lcd import LCD

def activar_alarma(led_verde, led_rojo, buzzer, sensor_pir,lcd):
    print("Activando alarma...")
    lcd.mostrar_mensaje("Activando alarma...")
    led_verde.off()
    led_rojo.on()
    buzzer.value(0)

    # Reiniciar el estado del sensor PIR y esperar para estabilizar
    sleep(2)  # Espera para estabilización del PIR
    print("Esperando estabilización del sensor PIR...")
    if sensor_pir.value() == 1:
        print("Sensor PIR aún activo. Esperando...")
        sleep(0.5)
    
    print("Alarma activada.")
    lcd.mostrar_mensaje("Alarma activada.")
    return 0