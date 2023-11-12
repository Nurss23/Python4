# dct = {
#     "name" : "Nurs",
#     "last_name" : "Suiunbek",
#     "age" : "20",
#     7 : 77,
#     "code_language": "python",
#     "city" : "Bishkek"}
# print(dct)

# dct = {
#     "name" : "Nurs",
#     "last_name" : "Suiunbek",
#     "age" : "20",
#     7 : 77,
#     "code_language": "python",
#     "city" : "Bishkek"}
# # print(dct)

# for k in dct:
#     dct[k] = 3
# print(dct)



dct = {}
while True:
    word = input()
    if word == "":
        break
    if word in dct:
        dct[word] += 1
    else:
        dct[word] = 1
print(dct)