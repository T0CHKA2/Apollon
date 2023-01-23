import uasyncio as asyncio
from uasyncio import Event

# Event sets
Idle = Event()
Error = Event()
Think = Event()
PowerOn = Event()
Status = Event()
FadeReadyFlag = Event()

# This is very bad move, i know... But uasyncio.primitives.WaitAny() doesn't work
async def WaitAny():
    if Status.is_set():
        pass
    else:
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
        else:
            pass
