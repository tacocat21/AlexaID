import cognitive_face as CF
from door_control.person import Person, PersonType

fd = open('./subscription_key', 'r')
KEY = fd.readline()
CF.Key.set(KEY)

class DoorControl:

    def __init__(self):
        self.family_group = 'family'
        self.friend_group = 'friend'
        self.no_entry_group  = 'no-entry'
        CF.person_group.create(self.family_group)
        CF.person_group.create(self.friend_group)
        CF.person_group.create(self.no_entry_group)
    
    def identify_incoming_person(self, image):
        # used for deciding if the door should be opened
        # return 
        detect_person = CF.face.detect(image, )

    def add_family_member(self, name, image):
        # check if the family member already exists later
        new_person_id = CF.person.create(self.family_group, name)
        CF.person.add_face(image, self.family_group, new_person_id.personId)


    def add_friend(self):
        new_person = Person(first_name, last_name)
        new_person.record_person(image)
        self.friends.append(new_person)


    def add_ban(self):
        new_person = Person(first_name, last_name)
        new_person.record_person(image)
        self.bans.append(new_person)
