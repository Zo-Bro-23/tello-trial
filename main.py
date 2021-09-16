from djitellopy import Tello
import time
me = Tello()
Tello.RESPONSE_TIMEOUT = 15
me.connect()
start_counter = 0
print(me.get_battery())
if start_counter == 0:
    me.takeoff()
    time.sleep(0.5)
    start_counter = 1
    me.land()

me.get_video_capture()