import mraa 
import time

import socket   #for sockets
import sys  #for exit

LED_GPIO = 5                   # The LED pin
BUTTON_GPIO = 6                # The button GPIO
led = mraa.Gpio(LED_GPIO)      # Get the LED pin object
led.dir(mraa.DIR_OUT)          # Set the direction as output
btn = mraa.Gpio(BUTTON_GPIO)   # Get the button pin object
btn.dir(mraa.DIR_IN)           # Set the direction as input


ledState = False               # LED is off to begin with
led.write(0)

def initSocket():



def getButtonPress():
    """ This function blocks until it registers an valid key press """
    while 1:
        if (btn.read() != 0):
            # No button press detected
            continue
        else:
            # Detected a click
            time.sleep(0.05)   # The debounce delay
            # Wait for the button to settle down
            if (btn.read() == 1):
                # and read the button state, if it is still pressed,
                # register this as an valid click
                return
            else:
                # else, ignore this button press and wait for it to be pressed
                continue

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 41234
    msg = '1'

    # initialize our socket...
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()

    while 1:
        # wait until someone clicks the button
        getButtonPress()

        try :
            #Set the whole string
            s.sendto(msg, (host, port))

            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]

            print 'Server reply : ' + reply

        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()

        # Button click, detected, now toggle the LED
        if ledState == True:
            led.write(1)
            ledState = False
        else:
            led.write(0)
            ledState = True

    time.sleep(0.005)
