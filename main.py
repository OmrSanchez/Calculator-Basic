from art import logo
print(logo)

def add(n1, n2):
	return n1 + n2
def subtract(n1, n2):
	return n1 - n2
def divide(n1, n2):
	return n1 / n2
def multiply(n1, n2):
	return n1 * n2

operations = {
	"+": add,
	"-": subtract,
	"/": divide,
	"*": multiply
}

def calculator():
	num1 = float(input("What's the first number?: "))
	calculator_on = True
	while calculator_on:
		for operators in operations:
			print(f"[{operators}]")

		operation_symbol = input("Pick an operation: ")
		num2 = float(input("What's the next number?: "))
		calculation_function = operations[operation_symbol]
		answer = calculation_function(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")
		calc_another = input(f"Type 'y' to continue calculating with "
		                     f"{answer}, or type 'n' to start a new "
		                     f"calculation: fd")
		if calc_another == "y":
			num1 = answer
		else:
			calculator_on = False
			calculator()

calculator()














# ##### Second Operation ####
# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
# calc_another = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to exit. : ")
# if calc_another == "n":
# 	calculator_on = False