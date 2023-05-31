
class config:
    name = 0
    age = 0

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def setName(self, _name):
        self.name = _name

    def getName(self):
        return self.name

    def setAge(self, _age):
        self.age = _age

    def getAge(self):
        return self.age

    def control(self,h):
        if h.getName()==1 :return True
        else: return False
