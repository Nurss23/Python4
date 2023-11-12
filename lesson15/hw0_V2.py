class Dog:
    size = 0.5
    tail = 1
    is_running = True
    def talk(self):
        print("Гав!")
Sharik = Dog()
Sharik.size
Sharik.tail
print(Sharik.size)
print(Sharik.tail)
Sharik.talk()

Rex = Dog()
Rex.size = 1
Rex.tail
print(Rex.size)
print(Rex.tail)
Rex.talk()

Tuzik = Dog()
Tuzik.size
Tuzik.tail
print(Tuzik.size)
print(Tuzik.tail)
Tuzik.talk()

class Video:
    views = 0
    likes = 100
    subscribers = []
    is_published = True
    def subscribe(self):
        print("Вы успешно подписаны")
python_course = Video()
python_course.views = 324
python_course.likes = 200
print(python_course.views)
print(python_course.likes)
python_course.subscribe()

lofi = Video()
lofi.views = 45346
lofi.likes = 2345
print(lofi.views)
print(lofi.likes)
lofi.subscribe()

vlog = Video()

vlog.views = 133413
vlog.likes = 123
print(vlog.views)
print(vlog.likes)
vlog.subscribe()

class Students:
    def __init__(self,name,age,course):
        self.name= name
        self.age = age
        self.course = course
    def get_student_info(self):
        print(f"Студент: {self.name}, Возраст: {self.age} лет")
    def god_rozhdenya_studenta(self):
        print(f"Год рождения: {2023 - self.age}")

student1 = Students("Нурс", 20, 1)
student1.get_student_info()
student1.god_rozhdenya_studenta()
student2 = Students("Али", 21 , 2)
student2.get_student_info()
student2.god_rozhdenya_studenta()
student3 = Students("Бека", 22, 3)
student3.get_student_info()
student3.god_rozhdenya_studenta()   