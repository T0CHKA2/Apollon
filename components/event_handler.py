import uasyncio
from events import Event

# Event sets
Idle = Event()
Error = Event()
Think = Event()
PowerOn = Event()
Request = Event()
Alarm = Event() # RTC alarm clock

# 4-Point Danger Level (4 PDL In future)
FirstDanger = Event()
SecondDanger = Event()
ThirdDanger = Event()
FourthDanger = Event()

# Cause events
temp_over = Event()
temp_lower = Event()
hum_lower = Event()


# Lists for check
event_list = [Idle, Error, Think, PowerOn, Alarm, Request, FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
CauseList = [temp_lower, temp_over, hum_lower]
simple_list = [Idle, Error, Think, PowerOn, Alarm, Request]
DangerList = [FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
DangerScore = -1 # Default -1, -1 == Idle state, No danger, will be reworked



def Check(list: type[list], output: type[bool]):
    """
    Check selected list for active events, output for return type.
    Example:

    >>> Check(CauseList, True)
    temp_over

    OR

    >>> Check(CauseList, False)
    True
    """
    
    for i in range(len(list)):
        if list[i].is_set():
            if output:
                return list[i]
            else:
                return True
        else:
            return False


def DangerClass(Score: type[int]):
    """
    This function interacting with 4PDL (4-Point Danger Level) by raising or lower Danger Score.
    """

    global DangerScore # Using default

    # This part will be reworked
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
    # This part will be reworked

    with open("temp.txt", "r") as d:
        d = open("temp.txt", "r")
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
def CauseSet(Cause: type[Event], Score: type[int]):
    """
    Set cause type and raise danger level by score number.
    Example: `CauseSet(hum_lower, 1)`
    """

    CauseCheck = Check(CauseList, True)
    for i in range(len(CauseList)):
        if CauseList[i].is_set():
            pass
        else:
            Cause.set()
            DangerClass(Score)

# Function: Clear cause type and lower danger level
def CauseClear(Cause: type[Event], Score: type[int]):
    """
    Clear cause type and lower danger level by score.
    Example: `CauseClear(hum_lower, 1)`
    """

    if Cause.is_set():
        Cause.clear()
        DangerClass(Score)
    else:
        pass


# P.S. Will be reworked
def LoopCheck():
    """
    Check event for set, if set will return name of event.
    It is usually used in the LED color adaptation system according to the situation.

    Always need to be used in loop functions for proper usage
    """

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

# Function: Set event if danger not set
# P.S. Will be reworked in events.py
def EventSet(Event: type[Event]):
    """
    Set event if danger not set

    If danger is set, will pass
    """

    DangerCheck = Check(DangerList, False)
    if DangerCheck:
        pass
    else:
        Event.set()
