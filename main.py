from machine import Pin
import utime
import display7seg

def temporizacion(display7, contador, delay):
    
   while (delay>0): 				#Mientras que la variable CONTRET sea mayor que cero
      display7.show(contador)       #Llamar la rutina MOSTRAR
      delay -= 1      				#Decremente la variable CONTRET
      
def saludar(display, contret):
    while (contret>0): #Mientras que la variable CONTRET sea mayor que cero
        display.show_char('H',3)
        display.show_char('0',2)
        display.show_char('L',1)
        display.show_char('A',0)
        contret -= 1      #Decremente la variable CONTRET
        
def helloAndCont():
    
    #Raspberry Pi PICO (4 digitos)
    display_pins = (16, 18, 13, 14, 15, 17, 12) #(a, b, c, d, e, f, g)
    transistor_pins = (22, 21, 20, 19)

    
    display7 = display7seg.Display(display_pins,transistor_pins = transistor_pins )
    
    #Inicia las variables
    contador = 0
    sentido = True
    saludar(display7,1000)
    
    while True:
        #Muestra el valor del contador en el display
        temporizacion(display7, contador, 20)
        

#Verifica si incrementa o decrementa el contador
        if sentido:
            contador += 1
        else:
            contador -= 1
        
        #Si contador es nueve coloque el sentido del contador a decrementar
        if contador == 9999:
            saludar(display7,1000)
            sentido = False
        
        #Si contador es cero coloque el sentido del contador a incrementar
        if contador == 0:
            saludar(display7,1000)
            sentido = True
    #Raspberry Pi PICO (4 digitos)
    
def main():
    while True :
        try:
            helloAndCont()
        except Exception as e:
            print("Error:", e)
        utime.sleep(2)
        
if __name__ == '__main__':
    main()

