import board
import neopixel
import time

num_pixels = 39
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=1.0)

# Yellow is a mix of red and green
# Format is (green, red, blue) for NeoPixel
increment = 5
brightness = 0

while True:
    print(f"Brightness: {brightness}")
    brightness += increment
    
    # Reverse direction at limits
    if brightness >= 255:
        increment = -5
    elif brightness <= 0:
        increment = 5
    
    # Set all pixels to yellow with current brightness
    # Yellow = full green + full red, no blue
    pixels.fill((brightness, brightness, 0))
    pixels.show()
    
    # Small delay for smooth fading
    time.sleep(0.02)