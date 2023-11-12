class List:
    all_contacts = []
    def __init__(self,name, lastname, phone_number):
        self.friend = [name, lastname, phone_number]
        self.all_contacts.append(self.friend)
        # print(self.all_contacts)

class Friend(List):
    def play_football_with_me(self):
        pass

class ContactList(List):
    def search_by_name(self,name):
        for i in self.all_contacts:
            for k in i:
                if name in k:
                    return i

# nurs = List("nurs", "Su", "000")
ali = List("ali", 'bek', "123")

n = ContactList("nurs", "Su", "000")
print(n.search_by_name("nurs"))