import esp32, machine
from machine import Pin
import uasyncio as asyncio
from dht_sens import measure
import neopixelring

# Settings
wake1 = Pin(13, Pin.IN)

# Turning on indicator
neopixelring.fade(13)

# Coroutine: Entry point
async def main():
    asyncio.create_task(measure(5))

    # Async goes here
    while True:
        # External button wake from deep sleep
        # esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)
        await asyncio.sleep_ms(1000)

# Start
asyncio.run(main())
