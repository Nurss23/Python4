# def email_func(email):
#     if "@" and "." in email:
#         res = "Да"
#     else:
#         res = "Нет"
#     print(f'{email}- {res}')

# email = input()
# email_func(email)

def func_rectangle(nums):
    nums = [i for i in nums.split() if i.isdigit()]
    p = 2 * (int(nums[0]) + int(nums[1]))
    print(f"Периметр прямоугольника, равен {p}")

num = input()
func_rectangle(num)

# def func_lst(lst_nums):
#     lst_nums = [int(n) for n in lst_nums.split()]
#     v_max = max(lst_nums)
#     v_min = min(lst_nums)
#     v_sum = sum(lst_nums)
#     # v_max = (max(map(int, lst_nums.split())))
#     # v_min = (min(map(int, lst_nums.split())))
#     # v_sum = (sum(map(int, lst_nums.split())))
#     print(f"Max= {v_max}, min= {v_min}, sum= {v_sum}")

# lst_nums = input()
# func_lst(lst_nums)