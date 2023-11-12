# class Contact:
#     all_contacts = []
#     def __init__(self,name, lastname, phone_number):
#         self.friend = [name, lastname, phone_number]
#         self.all_contacts.append(self.friend)
#         print(self.all_contacts)


# class Friend(Contact):
#     def play_football_with_me(self):
#         pass

# class ContactList(list):
#     def search_by_name(self,name):
#         lst_contact = []
#         for i in self:
#             for k in i:
#                 if name in k:
#                     return i


# con1 = Contact("ali", 'bek', "123")
# con2 = Contact("Nurs", "Su", "456")
# con3 = Contact("Nur", "Bek", "789")

# all_contacts = ContactList()

# s = ContactList()

# print(s.search_by_name("ali"))

# Создайте класс, сохраняющий каждый экземпляр в переменную класса all_contacts = [ ]. 
# В инициализаторе класса должны быть параметры name, lastname, phone_number. Подсказка: подумайте о self.

# Создайте субкласс Friend, у которого должен быть метод play_football_with_me()

# Создайте класс ContactList, который должен наследоваться от встроенного класса list. 
# В нем должен быть реализован метод search_by_name, который должен принимать имя, и возвращать список всех совпадений. 
# Замените all_contacts = [ ] на all_contacts = ContactList(). Создайте несколько контактов, используйте метод search_by_name.

class Person:
 
    def __init__(self, name, age, known_persons = []):
        self.name = name
        self.age = age
        self.known_persons = known_persons
 
    def know (self, person):
        if not person in self.known_persons:
            self.known_persons.append(person)
            # print(self.known_persons)
        else:
            print('{} уже знает человека по имени {}'.format(self.name, person.name))
 
    def is_known(self, person):
        text_action = {True: 'знает человека по имени', False : 'не знает человека по имени'}
        is_known_person = person in self.known_persons
        print('{} {} {}'.format(self.name, text_action[is_known_person], person.name))
 
if __name__ == '__main__':
    #anna = Person('Anna Ross', 25)
    cliff = Person('Cliff Birds', 45)
    jhon = Person('Jhon Smit', 37)
    anna = Person('Anna Ross', 25, [cliff])
    
    #anna.is_known(cliff)
    #anna.know(cliff)
    anna.is_known(cliff)
    anna.know(cliff)
    anna.is_known(jhon)
    anna.know(jhon)
    anna.is_known(jhon)
    anna.know(jhon)