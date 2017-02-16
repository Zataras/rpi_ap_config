# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as gpio
import os

gpio_pin_no=7

# Define a function to keep script running
def loop():
   raw_input()

# Define a function to run when an interrupt is called
def shutdown(pin):
    os.system("sudo shutdown -k now") # Send shutdown command to os
    #call('halt', shell=False)

gpio.setmode(gpio.BOARD) # Set pin numbering to board numbering
gpio.setup(gpio_pin_no, gpio.IN) # Set up pin x as an input
gpio.add_event_detect(gpio_pin_no, gpio.RISING, callback=shutdown, bouncetime=200) # Set up an interrupt to look for button presses

loop() # Run the loop function to keep script running
