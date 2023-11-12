class University:
    def __init__(self,name_univ):
        self.name_univ = name_univ
        print(self.name_univ)
        self.departments = {}

    def add_department(self,faculty):   
        self.departments.update({faculty : []})

class Student(University):
    def __init__(self,firstname, lastname):
        self.student = f"{firstname} {lastname}"

    def add_student(self,faculty,univsty):
        univsty.departments[faculty].append(self.student)
        # print(univsty.departments)


univ_1 = University("University-1")
stud_1 = Student("Nurs", "Suiunbek")
stud_2 = Student("Ali", "Nur")
stud_3 = Student("Nur", "Bek")
stud_4 = Student("Bek", "Sultan")

univ_1.add_department("Music")
univ_1.add_department("History")
univ_1.add_department("jurisprudence")

stud_1.add_student("jurisprudence", univ_1)
print(univ_1.departments)
stud_2.add_student("jurisprudence", univ_1)
print(univ_1.departments)
stud_3.add_student("History", univ_1)
print(univ_1.departments)
stud_4.add_student("Music", univ_1)
print(univ_1.departments)