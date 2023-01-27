from uasyncio import Event

# Event sets
Idle = Event() # If not doing anything 
Error = Event() # On error do smth
Think = Event() # If doing something too long
PowerOn = Event() # On power on
Request = Event() # On voice assistant help request
Alarm = Event() # RTC alarm
FirstDanger = Event() # On first danger class
SecondDanger = Event() # On second danger class
ThirdDanger = Event() # On third danger class
FourthDanger = Event() # On last danger class

# Status event only for WaitAny()
Status = Event()

# This is very bad move, i know...
# But uasyncio.primitives.WaitAny() doesn't work
# So i'm improvize

# Coroutine: Detect any event and start LEDs color change event
async def WaitAny():
    # No loop here because of neopixelring.py loop check
    if Status.is_set():
        # This will remove err with overwrite event
        pass
    elif Status.is_set() is False:
        if Idle.is_set():
            Status.set()
            return "Idle"
        elif Error.is_set():
            Status.set()
            return "Error"
        elif Think.is_set():
            Status.set()
            return "Think"
        elif PowerOn.is_set():
            Status.set()
            return "PowerOn"
        elif Alarm.is_set():
            Status.set()
            return "Alarm"
        elif Request.is_set():
            Status.set()
            return "Request"
        elif FirstDanger.is_set():
            Status.set()
            return "FirstDanger"
        elif SecondDanger.is_set():
            Status.set()
            return "SecondDanger"
        elif ThirdDanger.is_set():
            Status.set()
            return "ThirdDanger"
        elif FourthDanger.is_set():
            Status.set()
            return "FourthDanger"
        else:
            Warning("Unknown event, please check if you added it in WaitAny()")
            pass # If unknown event throw warn and pass
    else:
        raise Exception("Unknown status of 'Status' event") # throw err if status of "Status" event is unknown

# Function: Will close all events that using LEDs
def CompleteEvent(event):
    try:
        Status.clear()
        event.clear() # Close all events
    except Exception:
        print(Exception) # Error handling
    