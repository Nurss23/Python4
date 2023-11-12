class Student:
    name = "Gregor"
    age = 18
    groupNumber = "10A"

    def getName(self,name):

        self.name = name
        return self.name

    def getAge(self,age):

        self.age = age
        return self.age

    def getGroupNumber(self, groupNumber):

        self.groupNumber = groupNumber
        return self.groupNumber

    def setNameAge(self):

        Student.name = self.name
        Student.age = self.age

    def setGroupNumber(self):
        
        Student.groupNumber = self.groupNumber

n = Student()
u = Student()
a = Student()
j = Student()
b = Student()

n.name = "Nurs"
n.age = 20
n.groupNumber = "10N"

u.name = "Ularbek"
u.age = 23
u.groupNumber = "10U"

a.name = "Asan"
a.age = 17
a.groupNumber = "10B"

j.name = "Janar"
j.age = 18
j.groupNumber = "10J"

b.name = "Bayaman"
b.age = 19
b.groupNumber = "10C"

n.setNameAge()
n.setGroupNumber()
print(n.name)
print(n.age)
print(n.groupNumber)

student = Student
print(student.name)
print(student.age)
print(student.groupNumber)