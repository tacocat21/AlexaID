import cognitive_face as CF
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.person_id = None

    def record_person(self, image):
        
    # TODO: add more details lolz

class PersonType(Enum):
    FAMILY = 0
    FRIEND = 1
    BAN = 2
    UNKNOWN = 3
