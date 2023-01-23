from machine import Pin
import dht, neopixelring, uasyncio, event_handler

# Settings
sensor = dht.DHT22(Pin(15))

# Coroutine: measure hum & temp every 30s
async def measure(delay):
    while True:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        if temp > 20:
            neopixelring.setred(27)
        elif temp < 0:
            neopixelring.setblue(27)
        else:
            neopixelring.setorange(27)
        await uasyncio.sleep(delay)