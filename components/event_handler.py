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
temp_over = Event()
temp_lower = Event()
hum_lower = Event()

# Lists for check
event_list = [Idle, Error, Think, PowerOn, Alarm, Request, FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
CauseList = [temp_lower, temp_over, hum_lower]
simple_list = [Idle, Error, Think, PowerOn, Alarm, Request]
DangerList = [FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
DangerScore = -1

def Check(list, output):
    for i in range(len(list)):
        if list[i].is_set():
            if output:
                return list[i]
            else:
                return True
        else:
            return False

def DangerClass(Score):
    global DangerScore

    UpdDangerScore = DangerScore + Score

    if UpdDangerScore < -1:
        UpdDangerScore = -1
    elif UpdDangerScore > 3:
        UpdDangerScore = 3
    elif UpdDangerScore == -1:
        for i in range(len(DangerList)):
            DangerList[i].clear()
        
        EventSet(Idle)
    else:
        pass

    if UpdDangerScore is -1:
        for i in range(len(DangerList)):
            DangerList[i].clear()
            Idle.set()
    elif UpdDangerScore is 0:
        for i in range(len(DangerList)):
            if DangerList[i].is_set():
                DangerList[i].clear()
                DangerList[UpdDangerScore].set()
            else:
                DangerList[UpdDangerScore].set()
            
    elif UpdDangerScore is 1:
        for i in range(len(DangerList)):
            DangerList[i].clear()
            DangerList[UpdDangerScore].set()
    elif UpdDangerScore is 2:
        for i in range(len(DangerList)):
            DangerList[i].clear()
            DangerList[UpdDangerScore].set()
    elif UpdDangerScore is 3:
        for i in range(len(DangerList)):
            DangerList[i].clear()
            DangerList[UpdDangerScore].set()

def CauseSet(Cause, Score):
    CauseCheck = Check(CauseList, True)
    for i in range(len(CauseList)):
        if CauseList[i].is_set():
            pass
        else:
            Cause.set()
            DangerClass(Score)

def CauseClear(Cause, Score):
    if Cause.is_set():
        Cause.clear()
        DangerClass(Score)
    else:
        pass

def LoopCheck():
    for i in range(len(event_list)): # Check all events are they set or not
        if event_list[i].is_set(): # If set, go return what event is set
            return event_list[i]
        else:
            pass


def EventSet(Event):
    DangerCheck = Check(DangerList, False)
    if DangerCheck:
        pass
    else:
        Event.set()


# TODO: Configure LED work
# Now it's all working
# But somehow there is delay
# and i dunno how this delay work
# i think i starting to lose motivation to this work