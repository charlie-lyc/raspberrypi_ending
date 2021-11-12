from time import sleep
import picamera


with picamera.PiCamera() as picam:
    picam.resolution = (640, 480)
    picam.start_preview()
    sleep(5) # Wait to capture
    picam.capture('mycapture.jpg')
    picam.stop_preview()