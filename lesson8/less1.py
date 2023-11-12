# n = 100000

#1
# for i in range(1, n + 1):
#     need_b = False
#     for j in range(2, i):
#         if i % j == 0:
#             need_b = True
#             break
#     if not need_b:
#         print(i)

n = 100000
nums = list(range(n+1))
for k in range(2, n + 1):
    for m in range(2 * k, n + 1, k):
        nums[m] = 0

for p in nums:
    if p > 0:
        print(p)