import machine
from machine import Timer
from machine import UART

uart = UART(0, baudrate = 9600, tx = machine.Pin(0), rx = machine.Pin (1))

uart.write("helo word")

data = uart.read(10)
while (data == None):
        data = uart.read(10)

print(data)