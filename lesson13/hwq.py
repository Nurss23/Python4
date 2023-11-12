def create_squares_dict(n):
    dct_nums = {}
    num = list(range(1,n))
    for v in num:
        dct_nums[v] = v ** 2
    return dct_nums
print(create_squares_dict(13))

def  generate_even_numbers(g):
    return list(range(2,g,2))
print(generate_even_numbers(13))

def create_squares_dict(n):
    dct_nums = {}
    num = list(range(1,n))
    for k in (num):
        for v in str(k):
            r = int(v) ** 2
            dct_nums[k] = r
    return dct_nums
# n = 7
# res = create_squares_dict(n)
# print(res)
print(create_squares_dict(n = 13))

# def  generate_even_numbers(g):
#     lis 
#     for i in g:
#         if i % 2 == 0:
#             lis.append(i)