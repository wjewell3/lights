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
    # More red than green for a warmer yellow
    green = int(brightness * 0.6)  # Less green
    red = brightness  # Full red
    pixels.fill((green, red, 0))
    pixels.show()
    
    # Small delay for smooth fading
    time.sleep(0.02)