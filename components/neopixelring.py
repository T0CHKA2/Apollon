import neopixel, uasyncio, time
from machine import Pin
import event_handler as events

# Settings
orange = (255, 184, 65)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
half_orng = (165, 255, 15) # Of course it's not half orng
oneNhalfOrng = (255, 165, 15) # And of course it's not 1.5 orng

# Will be reworked
"""
def fadeoff(neopixel_pin):
    p = Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    for i in range (16):        
        if i is 0:
            time.sleep(0.1)
            pass
        elif i is 16:
            n.fill(black)
            n.write()
            time.sleep(0.1)
        else:
            c = (i/255, i/184, i/65)
            n.fill(c)
            n.write()
            time.sleep(0.1)
"""
# Will be reworked

# Coroutine: On LED Event change LED color
async def LED_start(pin: type[int]):
    while True:

        neo = neopixel.NeoPixel(Pin(pin), 16)
        event = events.StatusCheck()

        if (event is events.FirstDanger):
            neo.fill(yellow)
            neo.write()

        elif (event is events.SecondDanger):
            neo.fill(half_orng)
            neo.write()

        elif (event is events.ThirdDanger):
            neo.fill(oneNhalfOrng)
            neo.write()

        elif (event is events.FourthDanger):
            neo.fill(red)
            neo.write()
        elif (event is events.Idle):
            neo.fill(orange)
            neo.write()

        elif (event is events.Think):
            for i in range(4): # LED Color change cycle
                for j in range(16): # Color change: cycle
                    neo[j] = (0, 0, 0)
                    neo[i % 16] = (blue)
                    neo.write()
                    time.sleep_ms(50)

        elif (event is events.PowerOn):
            for i in range(16): # Color change: fade off/orange
                c = (i * 15, i * 11, i * 4)
                neo.fill(c)
                neo.write()
                time.sleep(0.1)
            
            events.PowerOn.clear() # Because it used once, clear
            events.EventSet(events.Idle) # For stable event check is set

        elif (event is events.Error):
            neo.fill(red)
            neo.write()

        elif (event is events.Request):
            neo.fill(blue)
            neo.write

        elif (event is events.Alarm):
            for i in range(10): # Color change: strobo
                neo.fill(black)
                neo.write()
                time.sleep(0.5)
                neo.fill(orange)
                neo.write()
                time.sleep(0.5)

            events.Alarm.clear() # Clear after 10 sec
        else:
            pass
        await uasyncio.sleep_ms(200) # Check every 0.2 sec