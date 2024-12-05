from introducirContra import introducir_contra
from comprobar_acceso import comprobar_nfc
from time import sleep
def comprobar_contra(codigo_correcto, intentos, lcd):
    """Verifica el código ingresado con el correcto y gestiona los intentos."""
    while intentos < 3:
        if intentos == 0:
            nfc = comprobar_nfc()
            if nfc:
                print("NFC detectado correctamente.")
                lcd.mostrar_mensaje("Acceso concedido por NFC.")
                return True   
        codigo_ingresado = introducir_contra(lcd)  # Asegúrate de que esta llamada funcione correctamente            
        if codigo_ingresado == codigo_correcto:
            lcd.mostrar_mensaje("Codigo correcto. Alarma desactivada.")
            return True  # Retorna True si el código es correcto
        else:
            # Si el código es incorrecto
            intentos += 1
            lcd.mostrar_mensaje(f"Intentos restantes : {3 - intentos}.")
            print(f"Codigo incorrecto. Te quedan {3 - intentos} intentos.")
            sleep(2)
    lcd.mostrar_mensaje("Has fallado todos los intentos. La alarma sigue activa.")
    return False  # Retorna False si se agotaron los intentos
