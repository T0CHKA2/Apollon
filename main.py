from components import event_handler, buttons, neopixelring, dht_sens
import uasyncio as asyncio

event_handler.PowerOn.set()
event_handler.DFileInit()

# Coroutine: entry point
async def main():
    asyncio.create_task(neopixelring.LED_st(27))
    asyncio.create_task(dht_sens.measure(15, 1))
    asyncio.create_task(buttons.longpress(32))
#    asyncio.create_task(RTC.alarm(21, 22))
#    Disabled because of not completed 

    while True:
        await asyncio.sleep_ms(50)

# Start
# do NOT delete "asyncio.run()"
asyncio.run(main())