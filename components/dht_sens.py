from machine import Pin
import dht, neopixelring, uasyncio

# Coroutine: measure hum & temp every "delay" seconds
async def measure(pin, delay):
    sensor = dht.DHT22(Pin(pin))
    while True:
        sensor.measure() # Measure because in without it hum and temp = 0
        temp = sensor.temperature()
        hum = sensor.humidity()
        if temp > 20: # If temp too hot, will warn to drink more water
            neopixelring.setred(27)
        elif temp < 0:
            neopixelring.setblue(27) # If too cold, will warn to suit up warm
        else: # In normal temperature will continiue work stabile
            neopixelring.setorange(27)
        await uasyncio.sleep(delay)