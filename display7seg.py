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
        

#Codigo agregado by: Eulises Brazonm

                   #char,'C', 'A',
        self.dictionary = [['0', int('3f',16),int('40',16)],
                    ['1', int('06',16),int('79',16)],
                    ['2', int('5b',16),int('24',16)],
                    ['3', int('4f',16),int('30',16)],
                    ['4', int('66',16),int('19',16)],
                    ['5', int('6D',16),int('12',16)],
                    ['6', int('7D',16),int('02',16)],
                    ['7', int('07',16),int('78',16)],
                    ['8', int('7f',16),int('00',16)],
                    ['9', int('67',16),int('18',16)],
                    ['A', int('77',16),int('08',16)],
                    ['b', int('7c',16),int('03',16)],
                    ['C', int('39',16),int('46',16)],
                    ['c', int('58',16),int('27',16)],
                    ['d', int('5e',16),int('21',16)],
                    ['E', int('79',16),int('06',16)],
                    ['F', int('71',16),int('0e',16)],
                    ['f', int('71',16),int('0e',16)],
                    ['G', int('3d',16),int('42',16)],
                    ['H', int('76',16),int('09',16)],
                    ['h', int('74',16),int('0b',16)],
                    ['i', int('30',16),int('4f',16)],
                    ['J', int('1e',16),int('61',16)],
                    ['j', int('1e',16),int('61',16)],
                    ['L', int('38',16),int('47',16)],
                    ['l', int('38',16),int('47',16)],
                    ['P', int('73',16),int('0c',16)],
                    ['p', int('73',16),int('0c',16)],
                    ['q', int('67',16),int('18',16)],
                    ['r', int('31',16),int('4e',16)],
                    ['S', int('6f',16),int('12',16)],
                    ['U', int('3e',16),int('41',16)],
                    ['u', int('1c',16),int('63',16)],
                    ['Y', int('6e',16),int('11',16)]]
        
    def show_char(self, char, location):
        
        #evaluo el valor que estoy recibiedo
  
        for word in self.dictionary:
            if char == word[0]:
                if self.kind.upper() == 'C':
                    symbol= word[1]
                if self.kind.upper() == 'A':
                    symbol= word[2]
                else:
                    return
        #en caso de no encontrarse el valor arrojara un error
        try:
            bit = 1;
            for i in range(7):
                if (symbol  & bit) == 0: #evaluo si en la posicion del bit se encuentra un 0
                    self.display[i].off()
                else:
                    self.display[i].on()
                bit = bit << 1 #desplazo el bit de comparazion hacia la izquierda
            
            #enciendo el digito durante un breve instante de tiempo
            self.transistors[location].on()
            utime.sleep_ms(1)
            self.transistors[location].off()
            
        except Exception as e:
            print("Error:", e)
        

