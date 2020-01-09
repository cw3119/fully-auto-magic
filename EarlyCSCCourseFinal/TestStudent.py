# a few students

from Student import *

student1 = Student("Mary Jones", 3.15)
student2 = Student("Bill Smith", 3.01)
student3 = Student("Mars Landon", 2.85)

print(student1)
print(student2)
print(student3)

print(student1.name, "has a GPA of", student1.getGPA())

student2.setGPA(3.9)
print(student2)

