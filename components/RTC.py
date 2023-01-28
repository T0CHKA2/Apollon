import ds1307, machine, uasyncio
import event_handler as event

ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)

# Coroutine: Alarm
async def alarm(SDA, SCL):
    
    # Settings
    hrs = ds1307._read_hours()
    min = ds1307._read_minutes()
    date = ds1307._read_date()
    date_now = null # Do not forget todo this

    while True:
        if alarm_data is date_now or alarm_data > date_now: # Check if alarm time has come
            event.Alarm.set()
            print("Alarm! Alarm!")
        else:
            pass
        uasyncio.sleep_ms(50)

# Coroutine: set Alarm data
async def alarm_set():

    # Settings
    hrs = ds1307._read_hours()
    min = ds1307._read_minutes()
    date = ds1307._read_date()
    date_now = null # Do not forget todo this

    # SoonTM
    pass