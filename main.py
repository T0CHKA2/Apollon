import machine, sys
import uasyncio as asyncio

# Importing files from another folder
sys.path.insert(1, '/path/to/application/app/folder')
import buttons, dht_sens, event_handler, RTC, neopixelring

# If woke up from deep sleep turn async back on
if machine.reset_cause() is machine.DEEPSLEEP_RESET:
    event_handler.PowerOn.set()
    main()

# Coroutine: entry point
async def main():
    event_handler.PowerOn.set()
    asyncio.create_task(dht_sens.measure(15, 1)) # Starting async by giving tasks
    asyncio.create_task(buttons.longpress(32))
    asyncio.create_task(neopixelring.LED_st(27))
    asyncio.create_task(RTC.alarm(21, 22))

    while True:
        await asyncio.sleep_ms(50)

# Start async and ESP32 other Coroutines
# do NOT delete "asyncio.run()"
asyncio.run(main())