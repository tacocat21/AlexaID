import cognitive_face as CF

fd = open('./subscription_key', 'r')
KEY = fd.readline()
CF.Key.set(KEY)

class DoorControl:

    def identify_incoming_person():
        pass

    def add_family_member():
        pass

    
