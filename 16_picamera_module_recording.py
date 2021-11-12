## Install package
# $ sudo apt install python-picamera

import picamera


with picamera.PiCamera() as picam:
    picam.resolution = (640, 480)
    picam.start_preview()
    picam.start_recording('myvideo.h264')
    picam.wait_recording(10) # Record for 10 seconds
    picam.stop_recording()
    picam.stop_preview()

    