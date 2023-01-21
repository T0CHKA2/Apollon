from machine import Pin
import dht, neopixelring, uasyncio

# Settings
sensor = dht.DHT22(Pin(15))

# Coroutine: measure hum & temp every 30s
async def measure(delay):
    while True:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        if temp > 20:
            neopixelring.setred(13)
        elif temp < 0:
            neopixelring.setblue(13)
        else:
            neopixelring.setorange(13)
        await uasyncio.sleep(delay)