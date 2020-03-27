#class to define a User and store its details
class User:
    def __init__(self):
        self.uid = -1
        self.full_name = 'abc'
        self.groups = []
    def details(self):
        print("userID :",self.uid)
        print("full_name :",self.full_name)
        print("groups :",self.groups )
       