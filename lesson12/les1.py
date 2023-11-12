# def srar(calc_average):
#     avg = sum(calc_average) / len (calc_average)
#     return avg
# calc_average = ([5, 6, 10])
# res = srar(calc_average)
# print(res)


# def res(num_1, num_2 = 100):
#     for i in range(num_1, num_2):
#         print(i)
#     return i
# # num_1 = 5
# # num_2 = 50
# # res_2 = res(num_1, num_2)
# # print(res_2)
# print(res(num_1 = 5))


def fib(num):
    for i in range(num-1):
        if i == 0:
            num_1 = 1
            num_2 = 2
        else:
            f_sym = num_1 + num_2
            num_1 = num_2
            num_2 = f_sym
    return f_sym
num = 6
res = fib(num)
print(res)


num_1 = 0
num_2 = 1
i = 0
while i < num:#n
    f_sym = num_1 + num_2
    num_1 = num_2
    num_2 = f_sym
    i += 1
print(num_2)


# info = {"address": "Isanova 103", "floors": 7, "has_parking": True}
# converted = [info[key] for key in info]
# print(converted)



# def convert(info):
#     res = []
#     for key in info:
#         res.append(info[key])
#     return res


# info = {"address": "Isanova 103", "floors": 7, "has_parking": True}
# r = convert(info)
# print(r)