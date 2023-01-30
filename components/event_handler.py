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

# Lists for check
event_list = [Idle, Error, Think, PowerOn, Alarm, Request, FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
DangerList = [FirstDanger, SecondDanger, ThirdDanger, FourthDanger]
danger_level = 0

# Function: Detect any event and start LEDs color change event
def WaitAny():
    for i in range(len(event_list)): # Check all events are they set or not
        if event_list[i].is_set(): # If set, go return what event is set
            return event_list[i]
        else:
            pass

# Function: Will raise danger level
def HazardUp(score):
    danger_level + score # Add score to danger level
    if danger_level is 1:
        SecondDanger.clear() # Clearing other danger classes
        ThirdDanger.clear()
        FourthDanger.clear()

        FirstDanger.set()
    elif danger_level is 2:
        FirstDanger.clear() # Clearing other danger classes
        ThirdDanger.clear()
        FourthDanger.clear()

        SecondDanger.set()
    elif danger_level is 3:
        SecondDanger.clear() # Clearing other danger classes
        FirstDanger.clear()
        FourthDanger.clear()

        ThirdDanger.set()
    elif danger_level is 4:
        SecondDanger.clear() # Clearing other danger classes
        FirstDanger.clear()
        ThirdDanger.clear()

        FourthDanger.set()
    else:
        danger_level - score # Do not add score to danger level
        Warning("There are limit for danger level, its already 4")

        # TODO: Use "for i in range()"


# Function: If no danger go idle state
# This is TEST FUNC it may be not used in future commits
def IdleState():
    for i in range(len(DangerList)):
        if DangerList[i].is_set():
            pass
        else:
            Idle.set()

# idk what is that so just let it be constructor
# Class: Forming an a event cause and type to send it into this file
class event(object):
    def __init__(self, type, cause, score):
        self.type = type # Example: Danger
        self.score = score # Example: 1 TODO: Default: 0
        self.cause = cause # Example: Temperature_over_limit

def check(class_event): # Check are this danger(or hazard) type event
        if class_event.type.lower() is "danger" or "hazard":
            HazardUp(class_event.score) # If true, raise danger score and change LED color
        else: # If not danger, just set event type
            class_event.type.capitilize().set()


# TODO: create new WaitAny() check, or think more about how to reconstruct WaitAny()
# lmao this will be 3-rd reconstruction of WaitAny()

# Function: Will lower danger level
def HazardDown():
    # Here will be multiple events that will work as trigger
    # That will trigger event_handler and do LED change
    
    pass