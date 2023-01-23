import machine, buttons, dht_sens, event_handler
import uasyncio as asyncio
from uasyncio import Event
import neopixelring

# If woke up from deep sleep turn back on
if machine.reset_cause() is machine.DEEPSLEEP_RESET:
    event_handler.PowerOn.set()
    main()

event_handler.PowerOn.set()

# Coroutine: entry point
async def main():
    # Async goes down here
    asyncio.create_task(dht_sens.measure(1))
    asyncio.create_task(buttons.longpress(32))
    asyncio.create_task(neopixelring.LED_st(27))

    while True:
        await asyncio.sleep_ms(50)

# Start async and ESP32 scripts
# do NOT delete "asyncio.run()"
asyncio.run(main())