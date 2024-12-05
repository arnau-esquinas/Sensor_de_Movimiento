from keypad import Keypad
from time import sleep

keypad = Keypad()

def introducir_contra(lcd):
    #Lee los dígitos del keypad y devuelve el código ingresado.
    codigo_ingresado = ""
    print("Alarma activa. Introduce el codigo para desactivarla.")
    lcd.mostrar_mensaje("Introduce el codigo:")

    # Leer 4 dígitos desde el keypad
    while True:
        tecla = keypad.leer_tecla()
        if tecla:
            lcd.mostrar_mensaje(f"Tecla: {tecla}")
            if tecla == 'C':
                # Finalizar la introducción y devolver el código ingresado
                return codigo_ingresado
            elif tecla == 'D':
                # Borrar el último dígito si existe
                if len(codigo_ingresado) > 0:
                    codigo_ingresado = codigo_ingresado[:-1]  # Eliminar el último carácter
                    lcd.mostrar_mensaje(f"Codigo: {'*' * len(codigo_ingresado)}")
                else:
                    lcd.mostrar_mensaje("No hay nada que borrar.")
            else:
                # Añadir el dígito a la contraseña
                codigo_ingresado += str(tecla)
                lcd.mostrar_mensaje(f"Codigo: {'*' * len(codigo_ingresado)}")  # Mostrar asteriscos para ocultar el código
            sleep(0.2)  # Espera para evitar lecturas dobles
