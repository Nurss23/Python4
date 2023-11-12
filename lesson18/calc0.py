n_1 = int(input())
op_1 = input()
n_2 = int(input())

op_object = Operation(n_1, op_1, n_2)
print(op_object.value)

def __init__(self, num_1, operation, num_2):
        while num_1 == 0:
            if operation == "+":
                self.value = num_1 + num_2
            elif operation == "*":
                self.value = num_1 * num_2
                