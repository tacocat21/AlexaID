import cognitive_face as CF
from camera_control import capture_image
from person_type import PersonType
import time

fd = open('./src/door_control/subscription_key', 'r')
KEY = fd.readline()
CF.Key.set(KEY)

class DoorControl:

    def __init__(self):
        self.family_group = 'family'
        self.friend_group = 'friend'
        self.no_entry_group  = 'no-entry'
        self.groups = [self.family_group,
                       self.friend_group,
                       self.no_entry_group]
    
    def create_groups(self):
        CF.person_group.create(self.family_group)
        CF.person_group.create(self.friend_group)
        CF.person_group.create(self.no_entry_group)

    def identify_incoming_person(self, image):
        # used for deciding if the door should be opened
        # return 
        detect_face = CF.face.detect(image)
        faceIds = []
        for face in detect_face:
            faceIds.append(face['faceId'])
        if(len(faceIds) == 0):
            # No matches found
            return PersonType.UNKNOWN
        return_type = PersonType.UNKNOWN
        for group in self.groups:
            try:
                CF.face.identify(faceIds, self.friend_group)
                if(group == self.family_group):
                    return_type = PersonType.FAMILY
                elif(group == self.friend_group):
                    return_type = PersonType.FRIEND
                else:
                    return_type = PersonType.NO_ENTRY
                break
            except:
                continue
        return return_type


    def train(self):
        for group in self.groups:
            print('training: '+ group)
            CF.person_group.train(group)
        time.sleep(30)

    def add_family_member(self, name, images):
        # check if the family member already exists later
        # images should be an array of images
        new_person_id = CF.person.create(self.family_group, name)
        for image in images:
            CF.person.add_face(image, self.family_group, new_person_id['personId'])

    def add_friend(self, name, images):
        new_person_id = CF.person.create(self.friend_group, name)
        for image in images:
            CF.person.add_face(image, self.friend_group, new_person_id['personId'])

    def add_ban(self, name, images):
        new_person_id = CF.person.create(self.no_entry_group, name)
        for image in images:
            CF.person.add_face(image, self.no_entry_group, new_person_id['personId'])

    def reset_groups(self):
        for group in self.groups:
            CF.person_group.delete(group)


