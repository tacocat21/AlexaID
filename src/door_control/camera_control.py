import time
from SimpleCV import Camera



def capture_image():
    cam = Camera()
    time.sleep(0.1)  # If you don't wait, the image will be dark
    img = cam.getImage()
    # img.save('verify_image_kendall.jpg')
    return img
