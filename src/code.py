# Programmable owl tealight 
# Copyright (C) 2020 Ayan Pahwa

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import board
import neopixel
import touchio
import time

# Pin for capacitive touch sensor 
touch_pad = board.A1  
touch = touchio.TouchIn(touch_pad)
count = 0

# Pin for NeoPixel
pixel_pin = board.D0
num_pixels = 4
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

# Initialise LEDs to off 

pixels.fill((0, 0, 0))
pixels.show()
time.sleep(0.1)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


# Main code sarts here 
while True:
    if touch.value:
        count = count + 1
        time.sleep(0.1)

        if count == 0:
            pixels.fill((0, 0, 0))
            pixels.show()
            time.sleep(0.1)

        elif count == 1:
            pixels.fill((255, 0, 0))
            pixels.show()
            time.sleep(0.1)

        elif count == 2:
            pixels.fill((0, 255, 0))
            pixels.show()
            time.sleep(0.1)

        elif count == 3:
            pixels.fill((0, 0, 255))
            pixels.show()
            time.sleep(0.1)

        elif count == 4:
            pixels.fill((255, 255, 255))
            pixels.show()
            time.sleep(0.1)

        elif count == 5:
            rainbow_cycle(0.01)
            count = -1

