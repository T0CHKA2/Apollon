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
# simple_ev_list = [Idle, Error, Think, PowerOn, Alarm, Request]
DangerList = [FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
danger_level = 0

# Function: Detect any event and start LEDs color change event
def WaitAny():
    for i in range(len(event_list)): # Check all events are they set or not
        if event_list[i].is_set(): # If set, go return what event is set
            return event_list[i]
        else:
            pass

# Function: Will update danger level
def HazardUpdate(score):
    danger_level + score
    # This will limit danger_level only to 4 levels
    # Because of Python interpretator 0 = 1, so 3 will be 4
    if danger_level > 3:
      danger_level = 3
    elif danger_level < 0:
        danger_level = 0
            
    for i in range(len(DangerList)):
        if DangerList[i].is_set():
           DangerList[i].clear() # Clear current danger level
           DangerList[danger_level].set() # Set new by the danger_level score

# Function: Check cause of danger and react to danger change
def CauseCheck(type, score):
    for i in range(len(CauseList)):
        if CauseList[i].is_set() and CauseList[i] is type:
            # If Cause is set and selected Cause from list is type
            pass
        elif CauseList[i] is type:
            type.set()
            HazardUpdate(score)
        else:
            Warning("Unkown Cause type")

# Function: Clear danger cause and lower danger level
def CauseClear(type, score):
    type.clear()
    HazardUpdate(score)

# Function: Check are there any active danger events, are the event type is danger type and set event
def UpdateStatus(name, cause, score):
    for i in range(len(DangerList)): # Check, are there any danger events set
        if DangerList[i].is_set() and score is 0:
            # That will destroy loop of ++score every time
            # And ignore all events that had 0 priority
            pass
        elif DangerList[i].is_set():
            Warning("Danger event is set, unable to change status")
            pass
        else: 
            if str(name.lower()) is "danger" or "hazard": # Check for danger or hazard type event
                if (type(cause) is 'undefined' ):
                    Warning("Cause type is undefined")
                else:
                    if score < 0:
                        CauseClear(cause, score) 
                    else: 
                        CauseCheck(cause, score) # If true, raise danger score and change LED color
            else: # If not danger, just set event type
                name.capitilize().set()

# TODO: Test new event handler