# - Importing Required Libraries
import serial
import time
from datetime import datetime

# - Setting the delay between each command
delay = 0.7

# - Setting the communication interface and speed
conn = serial.Serial("COM3", 9600)

# - Sending the commands to the device
conn.write("<ID**><MC>\r\n".encode("ascii")) # Setting color mode on both displays
time.sleep(delay)
conn.write("<ID01><HR><FU>\r\n".encode("ascii")) # Setting the color "High Red" and setting it to display time on display ID 1
time.sleep(delay)
conn.write("<ID02><HG><FU>\r\n".encode("ascii")) # Setting the color "High Green" and setting it to display time on display ID 2
time.sleep(delay)
conn.write("<ID01><M2>\r\n".encode("ascii")) # Setting display ID 1 to 24hr time format
time.sleep(delay)
conn.write("<ID02><M1>\r\n".encode("ascii")) # Setting display ID 1 to 12hr time format
time.sleep(delay)
now = datetime.now() # Getting the date and time now
current_time = now.strftime("%H%M%S") # Adjusting to the format that the LMS-1009 Understands
conn.write("<T{}>\r\n".format(current_time).encode("ascii")) # Updating the internal clock to the current time