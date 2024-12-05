from machine import Pin
from librerias.mfrc522 import MFRC522
import time 

# Configuración del lector RFID MFRC522
lector = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
tarjeta = 2909068339
llavero = 2788074931
nfc = False

# Función para comprobar el acceso con NFC
def comprobar_nfc():
    print("Lector activo...\n")
    contador = 0
    for contador in range(10):
        lector.init()
        (stat, tag_type) = lector.request(lector.REQIDL)
        if stat == lector.OK:
            (stat, uid) = lector.SelectTagSN()
            if stat == lector.OK:
                identificador = int.from_bytes(bytes(uid),"little",False)
                
                if identificador == tarjeta or identificador == llavero:
                    print("UID: "+ str(identificador)+" Identificado")
                    return True
                    
                else:
                    print("UID: "+ str(identificador)+" desconocido: Acceso denegado")
                    return False
        contador += 1
        if contador >= 10:  # Si se alcanza el límite de intentos, salir del bucle
            print("Se alcanzaron 10 intentos sin detectar una tarjeta válida.")
            return False
        time.sleep(0.1)
