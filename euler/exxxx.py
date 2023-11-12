n = 10001
n_2 = n * n
nums = list(range(n_2))
num_2 = list(range(n))
a = 0

# while a < len(num_2):
for k in range(1, n_2, 2):
    for m in range(2 * k, n_2, k):
        nums[m] = 0
        if len(nums) == 10001:
            break
print(max(nums))
