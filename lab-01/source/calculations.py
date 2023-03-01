def calc(a, b, operation):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Input a valid numbers!"
        
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        try:
          return a / b
        except ZeroDivisionError:
            return "Division by Zero!"
    else:
        return "Input a valid operator(+, -, *, /)"
