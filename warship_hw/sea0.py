# класс морей
class Sea:
    
    # создаём пустое поле/море
    def __init__(self, field_size):
        field = [[' ' for j in range(field_size)] for i in range(field_size)]
        self.field = field

            # функция отрисовки моря (рендер)
    def render(self):
        for row in self.field:
            for cell in row:
                print(cell, end='')
            print()
