# exception handling python : handle system generated error into user friendly error using try , except

try:
    a = 10
    b = 20
    print(a / b)

except ZeroDivisionError:
    print("Division by zero")

