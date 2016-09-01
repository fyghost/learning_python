class Student:
    
    def __init__(self, name):
        self.name = name

    def print_score(self):
        print('Student %s' % self.name)