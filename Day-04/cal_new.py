import sys
def add(value1, value2):
    return value1 + value2

def sub(value1, value2):
    return value1 - value2

def mul(value1, value2):
    return value1 * value2


num1= float(sys.argv[1])
operation= sys.argv[2]
num2= float(sys.argv[3])

if operation=="add":
    print(add(num1,num2))