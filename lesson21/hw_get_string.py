# Создайте класс, который будет иметь два метода get_string и print_string.
# get_string принимает строку от пользователя и print_string печатает строку в верхнем регистре.

class Round_HW:

    def get_string(self):
        self.strn = input('Введите строку:')

    def print_string(self):
        if isinstance(self.strn, str):
            print(f"{self.strn.upper()}")
        else:
            print("Error")

string_0 = Round_HW()
string_0.get_string()
string_0.print_string()


# class Round_HW:

#     def get_string(self, strn):
#         self.strn = strn

#     def print_string(self):

#         if isinstance(self.strn, str):
#             print(f"{self.strn.title()}")
#         else:
#             print("Error")

# string_0 = Round_HW()
# string_0.get_string("qwerty")
# string_0.print_string()
