class CalculatorError(Exception):
    pass


def operation(formula):
    print(formula)
    exp = formula.split()
    if len(exp) < 3:
        raise CalculatorError('invalid formula')
    elif exp[1] == '+':
        result = int(exp[0]) + int(exp[2])
        return result
    elif exp[1] == '-':
        result = int(exp[0]) - int(exp[2])
        return result
    elif exp[1] == '*':
        result = int(exp[0]) * int(exp[2])
        return result
    elif exp[1] == '/':
        result = int(exp[0]) // int(exp[2])
        return result

formula = input("enter the expression")

try:
    result =operation(formula)
    print(result)
except CalculatorError as e:
    print(e)

finally:
    print("your calculator operation is done")