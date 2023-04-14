# def	calculate(num1: int, oper: str, num2: int) -> int:
# 	if (oper == '+'):
# 		return (num1 + num2)
# 	elif (oper == '-'):
# 		return (num1 - num2)
# 	elif (oper == '*'):
# 		return (num1 * num2)
# 	elif (oper == '/'):
# 		return (num1 / num2)
# 	else:
# 		return (-1)

def	calculate(num1: int, oper: str, num2: int) -> int:
	ops = {
		"+" : (lambda a, b : a + b),
		"-" : (lambda a, b : a - b),
		"*" : (lambda a, b : a * b),
		"/" : (lambda a, b : a / b)
		}

	return (ops[oper](num1, num2))

print(calculate(10, "+", 10))
print(calculate(10, "-", 10))
print(calculate(10, "*", 10))
print(calculate(10, "/", 10))