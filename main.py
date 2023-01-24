import machine, buttons, dht_sens, event_handler
import uasyncio as asyncio
import neopixelring

# If woke up from deep sleep turn async back on
if machine.reset_cause() is machine.DEEPSLEEP_RESET:
    event_handler.PowerOn.set()
    main()

event_handler.PowerOn.set()
# Coroutine: entry point
async def main():
    asyncio.create_task(dht_sens.measure(15, 1)) # Starting async by giving tasks
    asyncio.create_task(buttons.longpress(32))
    asyncio.create_task(neopixelring.LED_st(27))

    while True:
        await asyncio.sleep_ms(50)

# Start async and ESP32 scripts
# do NOT delete "asyncio.run()"
asyncio.run(main())