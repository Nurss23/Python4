def arithmetic(num_1, num_2, operation):
    if operation == "+":
        res = num_1 + num_2
    elif operation == "-":
        res = num_1 - num_2
    elif operation == "*":
        res = num_1 * num_2
    elif operation == "/" and not num_2 == 0:
        res = num_1 / num_2
    else:
        res = "Неизвестная операция"
    return res
num_1 = 248679506896
num_2 = 34435
operation = "/"
arithmetic_1 = arithmetic(num_1, num_2, operation)
print(round(arithmetic_1, 2))