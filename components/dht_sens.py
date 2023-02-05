from machine import Pin
import dht, uasyncio
import event_handler as event

# Coroutine: measure hum & temp every "delay" seconds
async def measure(pin: type[int], delay: type[int]):
    sensor = dht.DHT22(Pin(pin))
    while True:

        sensor.measure() # Measure because without it hum and temp is 0
        temp = sensor.temperature()
        hum = sensor.humidity()

        if int(temp) > 20: 
            event.CauseSet(event.temp_over, 1)
            # Also will warn to drink more water

            if int(hum) < 20:
                event.CauseSet(event.hum_lower, 1)

            else:
                event.CauseClear(event.hum_lower, -1)

        elif int(temp) < 0:
            event.CauseSet(event.temp_lower, 1)
            # Also will warn to suit up warm

            if int(hum) < 20:
                event.CauseSet(event.hum_lower, 1)

            else:
                event.CauseClear(event.hum_lower, -1)
            
        elif int(hum) < 20:
            event.CauseSet(event.hum_lower, 1)
            # Also will warn to drink more water

        else:
            event.CauseClear(event.temp_over, -1)
            event.CauseClear(event.temp_lower, -1)
            event.CauseClear(event.hum_lower, -1)
        
        await uasyncio.sleep(delay)