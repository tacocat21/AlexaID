import time
from SimpleCV import Camera


class Camera:
    def capture_image():
        cam = Camera()
        time.sleep(0.1)  # If you don't wait, the image will be dark
        img = cam.getImage()
        return img
