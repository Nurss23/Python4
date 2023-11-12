class Contact:
    all_contacts = []
    def __init__(self,name, phone_number):
        # self.c = (name, phone_number)
        self.name = name
        self.phone_number = phone_number
        # self.all_contacts.append(self.friend)
        Contact.all_contacts.append(self)
        # print(Contact.all_contacts)


class Friend(Contact):
    def play_football_with_me(self):
        pass

class ContactList(list):
    def search_by_name(self,name):
        lst_contact = []
        # print(self)
        for i in self:
                if name in k:
                    lst_contact.append(name) 
        print(lst_contact)
        return lst_contact


con1 = Contact("alibek", 123)
con2 = Contact("Nurs", 456)
con3 = Contact("NurBek", 789)
# all_contacts = ContactList([con1,con2,con3])

s = ContactList([con1,con2,con3])

s.search_by_name("alibek")
print(s.search_by_name("alibek"))