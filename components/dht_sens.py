from machine import Pin
import dht, uasyncio
import event_handler as event

# Coroutine: measure hum & temp every "delay" seconds
async def measure(pin, delay):
    sensor = dht.DHT22(Pin(pin))
    while True:
        sensor.measure() # Measure because in without it hum and temp = 0
        temp = sensor.temperature()
        hum = sensor.humidity()
        if temp > 20 or temp < 0: # If temp too hot, will warn to drink more water
            event.FirstDanger.set() # If too cold, will warn to suit up warm
        else: # In normal temperature will continiue work stabile
            event.Idle.set()
        await uasyncio.sleep(delay)