from machine import Pin  # Importa la clase Pin desde el módulo machine para controlar los pines GPIO.

class Keypad:
    def __init__(self):
        # Definir las filas (R1 a R4) como salidas
        self.filas = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT)]
        # Las filas están conectadas a los pines GPIO 10, 11, 12 y 13 de la Raspberry Pi Pico.
        # Se configuran como salidas (Pin.OUT), ya que se utilizarán para activar cada fila de forma secuencial.

        # Definir las columnas (C1 a C4) como entradas con pull-up
        self.columnas = [Pin(6, Pin.IN, Pin.PULL_UP), Pin(7, Pin.IN, Pin.PULL_UP),
                        Pin(8, Pin.IN, Pin.PULL_UP), Pin(9, Pin.IN, Pin.PULL_UP)]
        # Las columnas están conectadas a los pines GPIO 6, 7, 8 y 9 de la Raspberry Pi Pico.
        # Se configuran como entradas (Pin.IN) con una resistencia pull-up interna (Pin.PULL_UP),
        # lo que significa que estarán en estado HIGH por defecto, y al presionar una tecla, se pondrán en LOW.

        # Mapeo de las teclas del keypad
        self.teclas = [['D', '#', '0', '*'],
                        ['C', '9', '8', '7'],
                        ['B', '6', '5', '4'],
                        ['A', '3', '2', '1']]
        # Esta es la representación de las teclas en el teclado matricial.
        # Cada lista interna representa una fila, y cada elemento dentro de la lista es una tecla en esa fila.
        # Las teclas están mapeadas en un arreglo de 4 filas y 4 columnas.

    def leer_tecla(self):
        # Activar una fila a la vez (hacerla LOW)
        for i in range(4):
            # Poner todas las filas en HIGH para asegurarse de que solo una fila sea activa a la vez
            for fila in self.filas:
                fila.value(1)  # Configura todas las filas a HIGH, es decir, desactiva las filas.

            # Activar la fila actual (LOW)
            self.filas[i].value(0)  # Configura la fila actual a LOW para que se active.

            # Comprobar si alguna columna está activada (LOW)
            for j in range(4):
                if self.columnas[j].value() == 0:
                    # Si alguna columna tiene valor LOW, significa que la tecla en la intersección de esta fila y columna está presionada.
                    # Devolvemos la tecla correspondiente desde el mapeo.
                    return self.teclas[i][j]

        return None  # Si no se presionó ninguna tecla, se retorna None.