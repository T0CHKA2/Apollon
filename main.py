import neopixel
from machine import Pin

# To change color create new var with new RGB settings
# Example:
# blue = (0, 0, 255) where Red 0 Green 0 Blue 255
orange = (255, 160, 64)

# Custom settings here, without <>
pin = Pin(<Your pin here>)
led_pixels(<Your pixels length here>)

neo = neopixel.NeoPixel(pin, led_pixels)

# For another color create new var
neo.fill(orange) # Type here your new var
neo.write() # This will change color when triggered