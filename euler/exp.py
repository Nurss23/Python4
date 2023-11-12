# n = 100
# nums = list(range(n+1))

# for k in range(2, n + 1):
#     for m in range(2 * k, n + 1, k):
#         nums[m] = 0
# print(max(nums))

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
