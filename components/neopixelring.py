import machine, neopixel
from time import sleep

orange = (255, 184, 65)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)


def fade(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    for i in range(16):
        c = (i * 15, i * 11, i * 4)
        n.fill(c)
        n.write()
        sleep(0.1)
    
    setorange(neopixel_pin)

def setorange(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    n.fill(orange)
    n.write()

def setred(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    n.fill(red)
    n.write()

def setblue(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    n.fill(blue)
    n.write()

def setyellow(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    n.fill(yellow)
    n.write()