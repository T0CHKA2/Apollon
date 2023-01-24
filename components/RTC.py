import ds1307, machine
import event_handler as event

ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)

hrs = ds1307._read_hours()
min = ds1307._read_minutes()
date = ds1307._read_date()

# Coroutine: Alarm
async def alarm():
    while True:
        if alarm_data is data_now or alarm_data > data.now: # Check if alarm time has come
            event.Alarm.set()
            print("Alarm! Alarm!")
        else:
            pass
        uasyncio.sleep_ms(50)

# Coroutine: set Alarm data
async def alarm_set():
    # SoonTM
    pass