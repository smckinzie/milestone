import time
import RPi.GPIO as GPIO
import os
from pathlib import Path

def main():
    milestone = Path("/home/pi/milestone.txt")
    song = "/home/pi/Music/Money.mp3"
    #set GPIO to defaults
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.LOW)
    while True:
        if milestone.is_file():
            print('File Exists')
            milestone.unlink()
            print("Party Time")
            # Close 120V circuit
            GPIO.output(23, GPIO.HIGH)
            os.system('cvlc -R ' + song + ' &')
            time.sleep(3000)
            exit()
        else:
            print('File Does Not Exist')
        time.sleep(10)
### Run the main function    
if __name__ == "__main__":
    main()
