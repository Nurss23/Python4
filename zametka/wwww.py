# a, b = 4, 7
# print(a,b)
######################################
# lst = [72, 23, -54]
# i = 0
# while i < 3:
#     print(i '''+1,''' lst[i])
#     i = i + 1

# lst = [72, 23, -54]
# i = 0
# while i < 3:
#     s = (lst[i] + lst[1])
#     i = i + 1
#     print(s)
#######################################

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# while i < 10:
#     s = (i,lst[i] * (lst[i]+1))
#     i = i + 1
#     print(s)
##########################################

# dct = {
#     'weather':  'cold',
#     'name':     'Smith',
#     'doors': 3,
#     'is_young': True 
# }

# for key in dct:
#     print(dct[key])
###############################

# s = 'spam'
# s = s[0] + 'b' + s[2:]
# print(s)
#########################################
#  Программа для итерации списка с использованием индексации

# genre = ['поп', 'рок', 'джаз']

#  проходимся по циклу, используя индекс i
# for i in range(len(genre)):
# 	print("Мне нравится", genre[i])
###########################################
# MyDictionary = {} 
# print("An Empty Dictionary: ") 
# print(MyDictionary)
########################################

# for i in range(1, 11):
#     need_b = False
#     for j in range(1, 2600):
#         if j % i == 0:
#             need_b = True
#             break
#     if not need_b:
#         print(i)
###########################################
# a = int(input())
# b = int(input())
 
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
 
# print(a + b)
#НОК(a, b) = (a * b) / НОД(a, b)
#############################################
# n = 100000
# nums = list(range(n+1))
# for k in range(2, n + 1):
#     for m in range(2 * k, n + 1, k):
#         nums[m] = 0

# for p in nums:
#     if p > 0:
#         print(p)
####################################################
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
 
# print(a + b)
####
# a = int(input())
# b = int(input())
 
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
 
# print(a)
#############################
# line = "привет 12 345"
# numbers = [c for c in line.split() if c.isdigit()]
# print(numbers)

# s = '46 235 4 8 37'
# nums = [int(n) for n in s.split()]  # [46, 235, 4, 8, 37]
# print(max(nums))
# print(max(map(int, s.split())))  # 235