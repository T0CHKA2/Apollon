import machine, neopixel

orange = (255, 184, 65)
red = (255, 0, 0)

# Simple functions for changing neopixel color and brightness
def setorange(neopixel_pin, neopixel_leds):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, neopixel_leds)

    # Setting all pixels to one color
    for i in range(16):
        n[i] = orange
    
    # Sending to LEDs their color
    n.write()

def setred(neopixel_pin, neopixel_leds):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, neopixel_leds)

    for i in range(16):
        n[i] = red
    n.write()