

from picamera import PiCamera
from time import sleep
import datetime

#camera.start_preview()

camera = PiCamera()

print("Food Type: ")
food_type = input()

print("State: ")
state = input()

# for i in range(5):
stamp = '{}{}'.format(state, datetime.datetime.now())
camera.capture('/home/pi/food_images/{}/{}.jpg'.format(food_type, stamp))


# camera.stop_preview()




