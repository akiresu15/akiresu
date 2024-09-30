import turtle as tur
import colorsys as cs

tur.speed(0)               # Set the drawing speed to the maximum
tur.bgcolor("black")       # Set the background color to black
h = 0                      # Initialize hue variable

for i in range(16):        # Outer loop for the number of circles
    for j in range(18):    # Inner loop for arcs in each circle
        c = cs.hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB
        tur.color(c)       # Set the turtle's color
        h += 0.005         # Increment hue for the next color
        tur.rt(90)         # Turn right by 90 degrees
        tur.circle(150 - j * 6, 90)  # Draw the first quarter circle
        tur.lt(90)         # Turn left by 90 degrees
        tur.circle(150 - j * 6, 90)  # Draw the second quarter circle
        tur.rt(180)        # Turn right by 180 degrees
    tur.circle(40, 24)     # Draw a smaller circle at the end

tur.done()                 # Keep the window open until closed