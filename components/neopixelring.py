import machine, neopixel, uasyncio, time
import event_handler as event
from time import sleep

orange = (255, 184, 65)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

#while True:
#    await uasyncio.Error()
#    setorange
                
def cycle(neopixel_pin):
    n = 16
    p = machine.Pin(neopixel_pin)
    np = neopixel.NeoPixel(p, n)
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
            np[i % n] = (blue)
            np.write()
            time.sleep_ms(50)

def fadeoff(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    for i in range (16):        
        c = (0, 0, 0)
        n.fill(c)
        n.write()
        sleep(0.1)

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

    for i in range(16):
        n[i] = red
    n.write()

def setblue(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    for i in range(16):
        n[i] = blue
    n.write()

def setyellow(neopixel_pin):
    p = machine.Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    for i in range(16):
        n[i] = yellow
    n.write()

async def LED_st(neopixel_pin):
    while True:
        stat_nm = await event.WaitAny()
        if (stat_nm=="Idle"):
            await event.Idle.wait()
            await setorange(neopixel_pin)
            event.Idle.clear()
            event.Status.clear()
        elif (stat_nm=="Think"):
            await even.Think.wait()
            cycle(neopixel_pin)
            event.Think.clear()
            event.Status.clear()
        elif (stat_nm=="PowerOn"):
            await event.PowerOn.wait()
            fade(neopixel_pin)
            event.PowerOn.clear()
            event.Status.clear()
        else:
            pass
        await uasyncio.sleep_ms(200)