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


def StatusCheck():
    """
    Wait any event flag to change LED color.
    """
    
    for i in range(len(event_list)):
        if event_list[i].is_set():
            return event_list[i]
        else:
            pass

def DFileInit():
    """
    Initializing danger score file.
    """

    with open("temp.txt", "w") as f:
        f.write("-1")
        f.close()

def DangerClass(Score: type[int]):
    """
    This function interacting with 4PDL (4-Point Danger Level) by raising or lower Danger Score.
    """

    with open("temp.txt", "r") as f:

        DangerScore = f.read()
        NewDScore = int(DangerScore) + int(Score)

        # Limit set
        if NewDScore < -1:
            NewDScore = -1

        elif NewDScore > 3:
            NewDScore = 3
        
        with open("temp.txt", "w") as d:
            d.write("%s" % (NewDScore))

        try:
            if NewDScore is -1:
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    Idle.set()

            elif NewDScore is 0:
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    Idle.clear()
                    FirstDanger.set()

            elif NewDScore is 1:
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    Idle.clear()
                    SecondDanger.set()

            elif NewDScore is 2:
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    Idle.clear()
                    ThirdDanger.set()

            elif NewDScore is 3:
                for i in range(len(DangerList)):
                    DangerList[i].clear()
                    Idle.clear()
                    FourthDanger.set()
        finally:
            f.close()

def CauseSet(Cause: type[Event], Score: type[int]):
    """
    Set cause type and raise danger level by score number.
    Example: `CauseSet(hum_lower, 1)`
    """

    if Cause.is_set():
        pass

    else:
        Cause.set()
        DangerClass(Score)

# Function: Clear cause type and lower danger level
def CauseClear(Cause: type[Event], Score: type[int]):
    """
    Clear cause type and lower danger level by score.
    Example: `CauseClear(hum_lower, -1)`
    """

    if Cause.is_set():
        Cause.clear()
        DangerClass(Score)

    else:
        pass


# P.S. Will be reworked in events.py
def EventSet(Event: type[Event]):
    """
    Set event if danger not set

    If danger is set, will pass
    """

    for i in range(len(DangerList)):
        if DangerList[i].is_set():
            pass
        
        else:
            Event.set()
