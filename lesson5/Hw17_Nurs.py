# word = input().lower()
# bb = word.replace(" ", "")
# bb.lower()
# print(bb)
# a = bb[::-1]
# a.lower()
# print(a)
# i = 0
# while i < len(bb):
#     s = bb[i]
#     if a == s:
#         o = ("yes")
#     elif a != s:  
#         o = ("no")
#     i += 1
# print(o)



word = input()
b = word.replace(" ", "").lower()
a = b[::-1].lower() 
if a == b:
    word1 = ("yes")
elif a != b:  
    word1 = ("no")
print(word1)



# last = lower_case[len(lower_case)-i-1]