def create_squares_dict(n):
    dct_nums = {}
    num = list(range(1,n +1))
    for v in num:
        dct_nums[v] = v ** 2
    return dct_nums
print(create_squares_dict(13))

def  generate_even_numbers(g):
    return list(range(2,g+1,2))
print(generate_even_numbers(14))