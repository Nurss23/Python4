                #a
def calc_average( *args):
    if args:
        average = sum(*args) / len(*args)
              #a     
        return average

#v1
# print(calc_average('grades1', [5, 6, 10]))
# print(calc_average('grades2 =', [1, 2, 3, 4, 5]))
#V2
print("grades1 =" ,int(calc_average([334, 2, 3, 4, 5, 6])))
print("grades2 =" ,int(calc_average([44, 56, 77, 3])))
print("grades3 =" ,int(calc_average([23, 3, 4, 5, 3])))
print("grades4 =" ,int(calc_average([23, 534, 54, 3, 4])))
print("grades5 =" ,int(calc_average([2, 34, 3, 3, 4])))