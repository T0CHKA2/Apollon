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
half_orng = ()
oneNhalfOrng = ()

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
        stat_nm = await event.WaitAny() # check if true
        if (stat_nm is "Idle"): # If Idle LED go orange
            await event.Idle.wait()
            neo.fill(orange)
            neo.write()
            event.CompleteEvent(event.Idle) # Set event close because completed
        elif (stat_nm is "Think"): # If Think LED go blue cycle
            await event.Think.wait()

            for j in range(16):
                neo[j] = (0, 0, 0)
                neo[i % 16] = (blue)
                neo.write()
                time.sleep_ms(50)
            
            event.CompleteEvent(event.Think) # Set event close because completed
        elif (stat_nm is "PowerOn"): # If power on LED go fade from off to orange
            await event.PowerOn.wait()

            for i in range(16):
                c = (i * 15, i * 11, i * 4)
                neo.fill(c)
                neo.write()
                sleep(0.1)
            
            event.CompleteEvent(event.PowerOn) # Set event close because completed
        elif (stat_nm is "Error"): # If Error LED go red
            await event.Error.wait()
            neo.fill(red)
            neo.write()
            event.CompleteEvent(event.Error) # Set event close beacuse completed
        elif (stat_nm is "Request"): # If help request LED go blue
            await event.Request.wait()
            neo.fill(blue)
            neo.write
            event.CompleteEvent(event.Request)
        elif (stat_nm is "Alarm"): # If Alarm Clock working LED go strobo
            await event.Alarm.wait()
            
            for i in range(10):
                neo.fill(black)
                neo.write()
                sleep(0.5)
                neo.fill(orange)
                neo.write()
                sleep(0.5)
            
            event.CompleteEvent(event.Alarm)
        elif (stat_nm is "FirstDanger"): # If First Danger class go yellow
            await event.FirstDanger.wait()
            neo.fill(yellow)
            neo.write()
            event.CompleteEvent(event.FirstDanger)
        elif (stat_nm is "SecondDanger"): # If Second Danger class go half orange
            await event.FirstDanger.wait()
            neo.fill(half_orng)
            neo.write()
            event.CompleteEvent(event.FirstDanger)
        elif (stat_nm is "ThirdDanger"): # If Third Danger class go one and half orange
            await event.FirstDanger.wait()
            neo.fill(oneNhalfOrng)
            neo.write()
            event.CompleteEvent(event.FirstDanger)
        elif (stat_nm is "FourthDanger"): # If Last Danger class go red
            await event.FirstDanger.wait()
            neo.fill(red)
            neo.write()
            event.CompleteEvent(event.FirstDanger)
        else:
            pass
        await uasyncio.sleep_ms(200) # Check every 0.2 sec