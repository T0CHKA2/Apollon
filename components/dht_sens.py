from machine import Pin
import dht, uasyncio
import event_handler as event

# Coroutine: measure hum & temp every "delay" seconds
async def measure(pin, delay):
    sensor = dht.DHT22(Pin(pin))
    while True:
        sensor.measure() # Measure because without it hum and temp is 0
        temp = sensor.temperature()
        hum = sensor.humidity()
        if temp > 20: # If temp too hot, will warn to drink more water
            event.UpdateStatus("danger", 'temp_over', 1)
        elif temp < 0: # If too cold, will warn to suit up warm
            event.UpdateStatus("danger", "temp_lower", 1)
        elif hum < 20: # If hum too low, will warn to drink more water
            event.UpdateStatus('danger', 'hum_lower', 1)
        else: # In normal temperature and hum will continiue work stabile
            event.CauseClear("temp_over", -1)
            event.CauseClear('temp_lower', -1)
            event.CauseClear('hum_lower', -1)
        await uasyncio.sleep(delay)

# Realize how to check cause that was declared