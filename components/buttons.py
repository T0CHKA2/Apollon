import machine, uasyncio, esp32
import event_handler as event

async def longpress(pin):
    button1 = machine.Pin(pin, machine.Pin.IN)
    while True:
        pressed = button1.value()
        await uasyncio.sleep(1)
        holding = button1.value()
        if pressed and not holding:
            esp32.wake_on_ext0(pin = button1, level = esp32.WAKEUP_ANY_HIGH)
        elif pressed and holding:
            await event.DeepSleep.set()
            machine.deepsleep()
        elif holding and not pressed:
            esp32.wake_on_ext0(pin = button1, level = esp32.WAKEUP_ANY_HIGH)
        else:
            pass