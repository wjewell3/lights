import board
import neopixel
import time
from rainbowio import colorwheel

num_pixels = 39
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness = 0.3)

NONE = (0,0,0)
GREEN = (255, 0, 0)
YELLOW = (255, 150, 0)
RED = (0, 255, 0)
PURPLE = (0, 255, 255)
BLUE = (0, 0, 255)
CYAN = (180, 0, 255)
BROWN = (64,92,51)

# l = [x*0.05 for x in range(1,21)] 
# l2 = l.copy()
# l2.reverse()
# l3 = l + l2 # list of values from 0.05 -> 1 -> 0.05, len(40)
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=1.0)
increment = 5
num = 0
while True:
    print(num)
    num += increment
    if num >=255:
        increment = -5
    elif num <=0:
        increment = 5
    # for i in range(len(l3)):
        # pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness = l3[i])
        # pixels.fill(RED) # red
        # pixels = neopixel.NeoPixel(board.D18, 50, brightness = brightness)
    for i in range(0,6): # green
        pixels[i] = (num, 0, 0)
    for i in range(6,36): #red
        pixels[i] = (0, num, 0)
    for i in range(36,39): # blue
        pixels[i] = (0, 0, num)
    pixels.show()
    # time.sleep(0.0001)

# def color_chase(color, wait):
#     for i in range(num_pixels):
#         pixels[i] = color
#         if i>=5:
#              pixels[i-5] = NONE
#         time.sleep(wait)
#         pixels.show()
#     time.sleep(0.01)

# def rainbow_cycle(wait):
#     for j in range(255):
#         for i in range(num_pixels):
#             rc_index = (i * 256 // num_pixels) + j
#             pixels[i] = colorwheel(rc_index & 255)
#         pixels.show()
#         time.sleep(wait)

# for i in [GREEN, YELLOW, RED, CYAN, BLUE, PURPLE]:
#         pixels.fill(i)
#         pixels.show()
#         # Increase or decrease to change the speed of the solid color change.
#         time.sleep(1)

# while True:
#     pixels.fill(NONE)
#     color_chase(RED, 0.075)  # Increase the number to slow down the color chase
    # rainbow_cycle(0)  # Increase the number to slow down the rainbow
