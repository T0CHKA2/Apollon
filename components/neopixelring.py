import neopixel, uasyncio, time
from machine import Pin
import event_handler as event
from time import sleep

# Settings
orange = (255, 184, 65)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
half_orng = (165, 255, 15)
oneNhalfOrng = (255, 165, 15)

def fadeoff(neopixel_pin):
    p = Pin(neopixel_pin)
    n = neopixel.NeoPixel(p, 16)

    for i in range (16):        
        if i is 0:
            sleep(0.1)
            pass
        elif i is 16:
            n.fill(black)
            n.write()
            sleep(0.1)
        else:
            c = (i/255, i/184, i/65)
            n.fill(c)
            n.write()
            sleep(0.1)


# Coroutine: On LED Event change LED color
async def LED_st(pin):
    while True:
        neo = neopixel.NeoPixel(Pin(pin), 16)
        stat_nm = event.LoopCheck() # check if true
        print(stat_nm)
        if (stat_nm is "Idle"): # If Idle LED go orange
            neo.fill(orange)
            neo.write()
        elif (stat_nm is "Think"): # If Think LED go blue cycle

            for j in range(16):
                np[j] = (0, 0, 0)
                np[i % 16] = (blue)
                np.write()
                neo[j] = (0, 0, 0)
                neo[i % 16] = (blue)
                neo.write()
                time.sleep_ms(50)

        elif (stat_nm is "PowerOn"): # If power on LED go fade from off to orange

            for i in range(16):
                c = (i * 15, i * 11, i * 4)
                neo.fill(c)
                neo.write()
                sleep(0.1)
            event.PowerOn.clear() # Because it used once, clear
            event.Idle.set()
        elif (stat_nm is "Error"): # If Error LED go red
            neo.fill(red)
            neo.write()
        elif (stat_nm is "Request"): # If help request LED go blue
            neo.fill(blue)
            neo.write
        elif (stat_nm is "Alarm"): # If Alarm Clock working LED go strobo
            
            for i in range(10):
                neo.fill(black)
                neo.write()
                sleep(0.5)
                neo.fill(orange)
                neo.write()
                sleep(0.5)
            
        elif (stat_nm is "FirstDanger"): # If First Danger class go yellow
            neo.fill(yellow)
            neo.write()
        elif (stat_nm is "SecondDanger"): # If Second Danger class go half orange
            neo.fill(half_orng)
            neo.write()
        elif (stat_nm is "ThirdDanger"): # If Third Danger class go one and half orange
            neo.fill(oneNhalfOrng)
            neo.write()
        elif (stat_nm is "FourthDanger"): # If Last Danger class go red
            neo.fill(red)
            neo.write()
        else:
            pass
        await uasyncio.sleep_ms(200) # Check every 0.2 sec