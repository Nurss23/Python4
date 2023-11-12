from sea0 import Sea
# функция отрисовки моря (рендер)
def render(self):
    for row in self.field:
        for cell in row:
            print(cell, end='')
        print()
