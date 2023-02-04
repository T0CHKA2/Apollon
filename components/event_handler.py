import uasyncio
from events import Event

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
temp_over = Event()
temp_lower = Event()
hum_lower = Event()

# Lists for check
event_list = [Idle, Error, Think, PowerOn, Alarm, Request, FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
CauseList = [temp_lower, temp_over, hum_lower]
simple_list = [Idle, Error, Think, PowerOn, Alarm, Request]
DangerList = [FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
DangerScore = -1 # Default -1, -1 == Idle state, No danger

def Check(list, output):
    for i in range(len(list)):
        if list[i].is_set():
            if output:
                return list[i]
            else:
                return True
        else:
            return False

# Function: Interaction with 4-point danger level (4PDL in future)
def DangerClass(Score):
    global DangerScore # Using default

    UpdDangerScore = DangerScore + Score
    # Limit set
    if UpdDangerScore < -1:
        UpdDangerScore = -1
    elif UpdDangerScore > 3:
        UpdDangerScore = 3
    elif UpdDangerScore == -1:
        for i in range(len(DangerList)):
            DangerList[i].clear()
    else:
        pass

    with open("temp.txt", "w") as f:
        f.write("%s" % (UpdDangerScore))

    with open("temp.txt", "r") as d:
        d = open("temp.txt", "r")
        d.seek(0)
        DataScore = d.read()

        try:
            if DataScore is "-1":
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    Idle.set()
            elif DataScore is "0":
                print("0")
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    FirstDanger.set()
            elif DataScore is "1":
                print("1")
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    SecondDanger.set()
            elif DataScore is "2":
                print("2")
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    ThirdDanger.set()
            elif DataScore is "3":
                print("3")
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    FourthDanger.set()
        finally:
            d.close()
    

# Function: Set cause type and raise danger level
def CauseSet(Cause, Score):
    CauseCheck = Check(CauseList, True)
    for i in range(len(CauseList)):
        if CauseList[i].is_set():
            pass
        else:
            Cause.set()
            DangerClass(Score)

# Function: Clear cause type and lower danger level
def CauseClear(Cause, Score):
    if Cause.is_set():
        Cause.clear()
        DangerClass(Score)
    else:
        pass

Status = Event()
# Function: Check setted events for change LED color
def LoopCheck():
        # No loop here because of neopixelring.py loop check
    if Status.is_set():
        # This will remove err with overwrite event
        pass
    else:
        if FirstDanger.is_set():
            return "FirstDanger"
        elif SecondDanger.is_set():
            return "SecondDanger"
        elif ThirdDanger.is_set():
            return "ThirdDanger"
        elif FourthDanger.is_set():
            return "FourthDanger"
        elif Idle.is_set():
            return "Idle"
        elif Error.is_set():
            return "Error"
        elif Think.is_set():
            return "Think"
        elif PowerOn.is_set():
            return "PowerOn"
        elif Alarm.is_set():
            return "Alarm"
        elif Request.is_set():
            return "Request"
        else:
            pass


def EventSet(Event):
    DangerCheck = Check(DangerList, False)
    if DangerCheck:
        pass
    else:
        Event.set()
