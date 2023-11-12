my_file = open("names.txt", mode='r',encoding='utf-8')

row_1 = my_file.readline()
print(row_1)

row_2 =my_file.readline()
print(row_2) 

row = my_file.read()
print(row)