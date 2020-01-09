class Student:

    def __init__(self,nm,gp):
        self.name=nm
        self.gpa=gp

    def setGPA(self, g):
        self.gpa=g

    def getGPA(self):

        return self.gpa
        
    def __str__(self):
        return self.name +'\t' + "GPA:"+ str(self.gpa)
