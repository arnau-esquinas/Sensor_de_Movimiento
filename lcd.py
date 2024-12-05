from machine import I2C, Pin
from librerias.lcd_api import LcdApi
from librerias.pico_i2c_lcd import I2cLcd

class LCD:
    def __init__(self, Pin_SDA, Pin_SCL):
        self.I2C_ADDR = 0x3F  # Dirección confirmada
        self.I2C_NUM_ROWS = 2
        self.I2C_NUM_COLS = 16

        # Inicializar I2C con frecuencia reducida
        self.i2c = I2C(0, sda=Pin(Pin_SDA), scl=Pin(Pin_SCL), freq=40000)

        try:
            # Intentar inicializar la pantalla LCD
            self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, self.I2C_NUM_ROWS, self.I2C_NUM_COLS)
            print("LCD inicializado correctamente.")
        except OSError as e:
            print("Error al inicializar LCD:", e)
            self.lcd = None  # Asegurarnos de que self.lcd no existe si la inicialización falla
        
    def mostrar_mensaje(self, msg):  # Añadir 'self' como primer parámetro
        """Muestra un mensaje en la pantalla LCD."""
        if self.lcd:
            self.lcd.clear()  # Limpiar la pantalla LCD antes de mostrar el mensaje
            self.lcd.putstr(msg)  # Mostrar el mensaje en el LCD
        else:
            print("No se pudo mostrar el mensaje en la LCD.")
