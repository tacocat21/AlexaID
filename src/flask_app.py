from flask import Flask
from door_control.door_control import DoorControl as DoorControlObj
from door_control.camera_control import capture_image


app = Flask(__name__)

def initialize_door():
    DoorControl = DoorControlObj()
    DoorControl.reset_groups()
    DoorControl.create_groups()
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
    DoorControl.add_family_member('Bill', bill_images)
    DoorControl.add_family_member('Kendall', kendall_images)
    DoorControl.add_friend('Taccio', taccio_images)
    DoorControl.add_ban('Viraat', viraat_images)
    DoorControl.train()
    return DoorControl
        
DoorControl = initialize_door

@app.route('/', methods=['GET'])
def identify_person():
    image = capture_image()
    return str(DoorControl.identify_incoming_person(image))
