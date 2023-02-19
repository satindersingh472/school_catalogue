class School:
    def __init__(self,name,numberOfStudents,level="primary"):
        self.name = name
        self.level = level
        self._numberOfStudents = numberOfStudents
    
    def __repr__(self):
        return "This is {} with a {} level teaching {} students".format(self.name,self.level,self._numberOfStudents)

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level
    
    def get_numberOfStudents(self):
        return self._numberOfStudents
    
    def set_numberOfStudents(self,new_number):
        self._numberOfStudents = new_number


class Primary(School):
    def __init__(self, name, numberOfStudents, pickupPolicy,level='primary'):
       super().__init__(name, numberOfStudents,level)
       self.pickUpPolicy = pickupPolicy
    
    def get_pickupPolicy(self):
       return self.pickUpPolicy

    def __repr__(self):
        schoolRepr = super().__repr__()
        return schoolRepr + " The pickup Policy is {}".format(self.get_pickupPolicy())

# nps = Primary('Narain Public School',2300,"Pick up before 2 pm")
# print(nps)

class High(School):
    def __init__(self, name, numberOfStudents, sportsTeam,level="high"):
        super().__init__(name, numberOfStudents, level)
        self.sportsTeams = sportsTeam

    def get_sportTeams(self):
        return list(self.sportsTeams)
    
    def __repr__(self):
        schoolRepr = super().__repr__()
        return schoolRepr + " the list of school's sports teams: {}".format(self.get_sportTeams())
    
bdps = High('BDPS',5000,['basketball','cricket','tennis'])
print(bdps)
