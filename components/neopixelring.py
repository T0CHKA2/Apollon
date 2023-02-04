import neopixel, uasyncio, time
from machine import Pin
import event_handler as event

# Settings
orange = (255, 184, 65)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
half_orng = (165, 255, 15)
oneNhalfOrng = (255, 165, 15)

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
        stat_name = event.LoopCheck() # Check for bool
        if (stat_name is "FirstDanger"):
            neo.fill(yellow)
            neo.write()
        elif (stat_name is "SecondDanger"):
            neo.fill(half_orng)
            neo.write()
        elif (stat_name is "ThirdDanger"):
            neo.fill(oneNhalfOrng)
            neo.write()
        elif (stat_name is "FourthDanger"):
            neo.fill(red)
            neo.write()
        elif (stat_name is "Idle"):
            neo.fill(orange)
            neo.write()
        elif (stat_name is "Think"):

            for j in range(16):# Led color change cycle
                neo[j] = (0, 0, 0)
                neo[i % 16] = (blue)
                neo.write()
                neo[j] = (0, 0, 0)
                neo[i % 16] = (blue)
                neo.write()
                time.sleep_ms(50)

        elif (stat_name is "PowerOn"):

            for i in range(16): # Same here
                c = (i * 15, i * 11, i * 4)
                neo.fill(c)
                neo.write()
                time.sleep(0.1)
            
            event.PowerOn.clear() # Because it used once, clear
            event.Idle.set() # For stable event check is set
        elif (stat_name is "Error"):
            neo.fill(red)
            neo.write()
        elif (stat_name is "Request"):
            neo.fill(blue)
            neo.write
        elif (stat_name is "Alarm"):
            
            for i in range(10): # Same as Think event
                neo.fill(black)
                neo.write()
                time.sleep(0.5)
                neo.fill(orange)
                neo.write()
                time.sleep(0.5)

            event.Alarm.clear() # Clear after 10 sec
        else:
            pass
        await uasyncio.sleep_ms(200) # Check every 0.2 sec