import unittest, neopixel
from components import neopixelring as LED
from components import event_handler as event


class TestPowerOn(unittest.TestCase):

    def test_poweron(self):
        event.PowerOn.set() # Set event flag
        LED.LED_st(27) # Start LED
        pixelRGB = neopixel.__getitem__(1) # Getting RGB number of pixel
        self.assertEqual(pixelRGB, (255, 184, 65))
    
    


