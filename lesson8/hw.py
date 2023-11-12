even_numbers = []
odd_numbers = []
even_cubes = []
for odd in range(1, 51, 2):
    odd_numbers.append(odd)
for even in range(2, 51, 2):
    even_numbers.append(even)
    even_cubes.append(even ** 3)
print(odd_numbers)
print(even_numbers)
print(even_cubes)