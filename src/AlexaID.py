from door_control.door_control import DoorControl as DoorControlObj
from door_control.camera_control import capture_image
import time
import cognitive_face as CF

if __name__ == '__main__':

    DoorControl = DoorControlObj()
    # DoorControl.reset_groups()
    bill_images = ['./images/1.jpg',
                   './images/2.jpg',
                   './images/3.jpg',
                   './images/4.jpg']
    taccio_images =['./images/5.jpg',
                    './images/6.jpg']
    kendall_images = ['./images/7.jpg',
                      './images/8.jpg',
                      './images/9.jpg',
                      './images/10.jpg',
                      './images/11.jpg']
    viraat_images = ['./images/12.jpg',
                     './images/13.jpg',
                     './images/14.jpg']
    for image in bill_images:
        
    DoorControl.add_family_member('Kendall Koe', kendall_images)
    DoorControl.add_ban('Taccio Yamamoto', ['./src/images/test_taccio.jpg'])
    DoorControl.add_friend('Taccio Yamamoto', ['./src/images/test_taccio.jpg'])
    DoorControl.train()
#    time.sleep(1)
    print(DoorControl.identify_incoming_person('./src/images/test_kendall.jpg'))
    print(DoorControl.identify_incoming_person('./src/images/verify_kendall.jpg'))
    print(DoorControl.identify_incoming_person('./src/images/verify_kendall1.jpg'))
    print(DoorControl.identify_incoming_person('./src/images/test_taccio.jpg'))

