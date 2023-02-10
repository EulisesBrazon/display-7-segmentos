"""
Clase de Display 7 Segmentos usando MicroPython
by: Sergio Andres Castaño Giraldo
Referencia: https://controlautomaticoeducacion.com/
"""

from machine import Pin
import utime

class Display:
    
    
    def __init__(self, Pins, kind = 'A', transistor_pins = 1):
        self.kind = kind
        self.number_digit = len(transistor_pins)
        
        #Configura los pines del display como salida
        display = list()
        for i in range(7):
            display.append( Pin(Pins[i], Pin.OUT) )
        
        #Configura los pines de los transistores como salida
        transistors = list()
        for i in range(self.number_digit):
            transistors.append( Pin(transistor_pins[i], Pin.OUT) )
        
        #Tupla con las posiciones del display
        self.display = display
        
        #Tupla con las posiciones de los transistores
        self.transistors = transistors
        
    def show(self, digits):
        #Realiza la multiplexación
        for i in range( self.number_digit ):
            number = int((digits % 10 ** (i+1)) / 10 ** i)
            self._show_one_display(number)
            self.transistors[i].on()
            utime.sleep_ms(1)
            self.transistors[i].off()
            
    
    #Metodo provado para mostrar número en un solo display
    def _show_one_display(self, digit):
        bit = 1;
        
        #Display Cátodo Común
        if self.kind.upper() == 'C':
            numbers = (int('3f',16),int('06',16),int('5b',16),int('4f',16),int('66',16),int('6d',16),int('7d',16),int('07',16),int('7f',16),int('67',16))
        #Display Ánodo Común
        elif self.kind.upper() == 'A':
            numbers = (int('40',16),int('79',16),int('24',16),int('30',16),int('19',16),int('12',16),int('02',16),int('78',16),int('00',16),int('18',16))
        else:
            return
        
        for i in range(7):
            if (numbers[digit]  & bit) == 0:
                self.display[i].off()
            else:
                self.display[i].on()
            bit = bit << 1
        
"""
Metodo agregado
"""
        
    def show_char(self, digit, location):
        
        #evaluo el valor qeu estoy recibiedo
        if digit == '0':
            #una vez que reconosco el caracter,asigno su valor correspondiente
            if self.kind.upper() == 'C':
                numbers = (int('3f',16))
            elif self.kind.upper() == 'A':
                numbers = (int('40',16))
            else:
                return
        elif digit == '1':
            if self.kind.upper() == 'C':
                numbers = (int('06',16))
            elif self.kind.upper() == 'A':
                numbers = (int('79',16))
            else:
                return
        elif digit =='2':
            if self.kind.upper() == 'C':
                numbers = (int('5b',16))
            elif self.kind.upper() == 'A':
                numbers = (int('24',16))
            else:
                return
        elif digit == '3':
            if self.kind.upper() == 'C':
                numbers = (int('4f',16))
            elif self.kind.upper() == 'A':
                numbers = (int('30',16))
            else:
                return
        elif digit == '4':
            if self.kind.upper() == 'C':
                numbers = (int('66',16))
            elif self.kind.upper() == 'A':
                numbers = (int('19',16))
            else:
                return
        elif digit == '5':
            if self.kind.upper() == 'C':
                numbers = (int('6D',16))
            elif self.kind.upper() == 'A':
                numbers = (int('12',16))
            else:
                return
        elif digit == '6':
            if self.kind.upper() == 'C':
                numbers = (int('7D',16))
            elif self.kind.upper() == 'A':
                numbers = (int('02',16))
            else:
                return
        elif digit == '7':
            if self.kind.upper() == 'C':
                numbers = (int('07',16))
            elif self.kind.upper() == 'A':
                numbers = (int('78',16))
            else:
                return
        elif digit == '8':
            if self.kind.upper() == 'C':
                numbers = (int('7f',16))
            elif self.kind.upper() == 'A':
                numbers = (int('00',16))
            else:
                return
        elif digit == '9':
            if self.kind.upper() == 'C':
                numbers = (int('67',16))
            elif self.kind.upper() == 'A':
                numbers = (int('18',16))
            else:
                return
        elif digit =='A':
            if self.kind.upper() == 'C':
                numbers = (int('77',16))
            elif self.kind.upper() == 'A':
                numbers = (int('08',16))
            else:
                return
        elif digit == 'b':
            if self.kind.upper() == 'C':
                numbers = (int('7c',16))
            elif self.kind.upper() == 'A':
                numbers = (int('03',16))
            else:
                return
        elif digit == 'C':
            if self.kind.upper() == 'C':
                numbers = (int('39',16))
            elif self.kind.upper() == 'A':
                numbers = (int('46',16))
            else:
                return
        elif digit =='c':
            if self.kind.upper() == 'C':
                numbers = (int('58',16))
            elif self.kind.upper() == 'A':
                numbers = (int('27',16))
            else:
                return
        elif digit == 'd':
            if self.kind.upper() == 'C':
                numbers = (int('5e',16))
            elif self.kind.upper() == 'A':
                numbers = (int('21',16))
            else:
                return
        elif digit == 'E':
            if self.kind.upper() == 'C':
                numbers = (int('79',16))
            elif self.kind.upper() == 'A':
                numbers = (int('06',16))
            else:
                return
        elif digit == 'F' or 'f':
            if self.kind.upper() == 'C':
                numbers = (int('71',16))
            elif self.kind.upper() == 'A':
                numbers = (int('0e',16))
            else:
                return
        elif digit == 'G':
            if self.kind.upper() == 'C':
                numbers = (int('3d',16))
            elif self.kind.upper() == 'A':
                numbers = (int('42',16))
            else:
                return
        elif digit == 'H':
            if self.kind.upper() == 'C':
                numbers = (int('76',16))
            elif self.kind.upper() == 'A':
                numbers = (int('09',16))
            else:
                Return
        elif digit == 'h':
            if self.kind.upper() == 'C':
                numbers = (int('74',16))
            elif self.kind.upper() == 'A':
                numbers = (int('0b',16))
            else:
                    eturn
        elif digit == 'i':
            if self.kind.upper() == 'C':
                numbers = (int('30',16))
            elif self.kind.upper() == 'A':
                numbers = (int('4f',16))
            else:
                return
        elif digit == 'J' or 'j':
            if self.kind.upper() == 'C':
                numbers = (int('1e',16))
            elif self.kind.upper() == 'A':
                numbers = (int('61',16))
            else:
                return
        elif digit == 'L'or 'l':
            if self.kind.upper() == 'C':
                numbers = (int('38',16))
            elif self.kind.upper() == 'A':
                numbers = (int('47',16))
            else:
                return
        elif digit == 'P'or 'p':
            if self.kind.upper() == 'C':
                numbers = (int('73',16))
            elif self.kind.upper() == 'A':
                numbers = (int('0c',16))
            else:
                return
        elif digit == 'q':
            if self.kind.upper() == 'C':
                numbers = (int('67',16))
            elif self.kind.upper() == 'A':
                numbers = (int('18',16))
            else:
                return
        elif digit == 'r':
            if self.kind.upper() == 'C':
                numbers = (int('31',16))
            elif self.kind.upper() == 'A':
                numbers = (int('4e',16))
            else:
                return
        elif digit == 'S':
            if self.kind.upper() == 'C':
                numbers = (int('6f',16))
            elif self.kind.upper() == 'A':
                numbers = (int('12',16))
            else:
                return
        elif digit == 'U':
            if self.kind.upper() == 'C':
                numbers = (int('3e',16))
            elif self.kind.upper() == 'A':
                numbers = (int('41',16))
            else:
                return
        elif digit == 'u':
            if self.kind.upper() == 'C':
                numbers = (int('1c',16))
            elif self.kind.upper() == 'A':
                numbers = (int('63',16))
            else:
                    return
        elif digit == 'Y':
            if self.kind.upper() == 'C':
                numbers = (int('6e',16))
            elif self.kind.upper() == 'A':
                numbers = (int('11',16))
            else:
                return    
        else:
            #si no corresponde con ninguno termino la ejecucion
            return
        
        
        #realizo el recorrido bit a bit
        bit = 1;
        
        for i in range(7):
            if (numbers  & bit) == 0: #evaluo si en la posicion del bit se encuentra un 0
                self.display[i].off()
            else:
                self.display[i].on()
            bit = bit << 1 #desplazo el bit de comparazion hacia la izquierda
            
        self.transistors[location].on()
        utime.sleep_ms(1)
        self.transistors[location].off()

