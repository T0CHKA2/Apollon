import machine, uasyncio, esp32
import event_handler as event

async def longpress(pin):
    button1 = machine.Pin(pin, machine.Pin.IN)
    while True:
        pressed = button1.value() # Check if presse
        await uasyncio.sleep(1)
        holding = button1.value() # Check if holded
        if pressed and not holding: # If in timing wake up 
            esp32.wake_on_ext0(pin = button1, level = esp32.WAKEUP_ANY_HIGH)
        elif pressed and holding: # If holded go DeepSleep
            await event.DeepSleep.set()
            event.DeepSleep.clear()
            machine.deepsleep() 
        elif holding and not pressed: # If not in timing wake up
            esp32.wake_on_ext0(pin = button1, level = esp32.WAKEUP_ANY_HIGH)
        else: # Else it will ignore
            pass