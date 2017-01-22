from door_control.door_control import DoorControl as DoorControlObj
from door_control.camera_control import capture_image
import time
import cognitive_face as CF

if __name__ == '__main__':

    DoorControl = DoorControlObj()
    # DoorControl.reset_groups()
    kendall_images = ['./src/images/test_kendall.jpg',
                      './src/images/test_kendall1.jpg',
                      './src/images/test_kendall2.jpg']
    DoorControl.add_family_member('Kendall Koe', kendall_images)
    DoorControl.add_ban('Taccio Yamamoto', ['./src/images/test_taccio.jpg'])
    DoorControl.add_friend('Taccio Yamamoto', ['./src/images/test_taccio.jpg'])
    DoorControl.train()
#    time.sleep(1)
    print(DoorControl.identify_incoming_person('./src/images/test_kendall.jpg'))
    print(DoorControl.identify_incoming_person('./src/images/verify_kendall.jpg'))
    print(DoorControl.identify_incoming_person('./src/images/verify_kendall1.jpg'))
    print(DoorControl.identify_incoming_person('./src/images/test_taccio.jpg'))

