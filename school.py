class School:
    
    def __init__(self, name):
        self.name = name
        self.roster = {}
      
    def add_student(self, fullname, grade):
        self.fullname = fullname
        self.grade = grade
        if grade in self.roster:
            self.roster[grade].append(fullname)
        else:
            self.roster[grade] = [fullname]
            
    def getgrade(self, number):
        return self.roster[number]
    
    def sort_roster(self):
        sorteddictionary = self.roster
        for key in sorteddictionary:
            sorteddictionary[key].sort()
        return sorteddictionary