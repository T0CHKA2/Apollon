import unittest, neopixel
from components import neopixelring as LED
from components import event_handler as event


class TestPowerOn(unittest.TestCase):

    def setUp(self) -> None:
        uasyncio.create_task(neopixelring.LED_st(27))
        return super().setUp()

    def test_poweron(self):
        event.PowerOn.set() # Set event flag
        LED.LED_st(27) # Start LED
        pixelRGB = neopixel.__getitem__(1) # Getting RGB number of pixel
        self.assertEqual(pixelRGB, (255, 184, 65))
        event.PowerOn.clear()
    
    def test_Error(self):
        # event.Error.set()
        # ...
        # event.Error.clear()
        pass

    def test_Idle(self):
        # event.Idle.set()
        # ...
        # event.Idle.clear()
        pass

    def test_Request(self):
        # event.Request.set()
        # ...
        # event.Request.clear()
        pass

    def test_Alarm(self):
        # event.Alarm.set()
        # ...
        # event.Alarm.clear()
        pass

    def test_Think(self):
        # event.Think.set()
        # ...
        # event.Think.clear()
        pass

    def test_FirHaz(self):
        # event.FirstDanger.set()
        # ...
        # event.FirstDanger.clear()
        pass

    def test_SecHaz(self):
        # event.SecondDanger.set()
        # ...
        # event.SecondDanger.clear()
        pass
    
    def test_ThrdHaz(self):
        # event.ThirdDanger.set()
        # ...
        # event.ThirdDanger.clear()
        pass

    def test_FourHaz(self):
        # event.FourthDanger.set()
        # ...
        # event.FourthDanger.clear()
        pass

