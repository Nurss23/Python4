# def binary_search(list, item):
#     low = 0
#     high = len(list)-1
#     while low <= high : 
#         mid = (low + high) 
#         guess = list[mid] 
#         if guess == item : 
#             return mid 
#         if guess > item: 
#             high = mid - 1 
#         else: 
#             low = mid + 1 
#         return None 
# my_list = [1, 3, 5, 7, 9]
# print(binary_search(my_list, 3)) # => 1
# print(binary_search(my_list, -1)) # => None
# for i in range(1, 128):
#     if 2 ** i == 128:
#         break
# print(i)

# def Smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         smallest = arr[i]
#         smallest_index = i
#         return smallest_index

# def selectionSort(arr): 
#     newArr = [] 
#     for i in range(len(arr)): 
#         smallest = indSmallest(arr)
#         newArr.append(arr.pop(smallest)) 
#     return newArr 
# print(selectionSort[6, 2, 10])  

# def small_m(arr):




# res = small_m()    