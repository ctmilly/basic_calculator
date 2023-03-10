import sys
import matplotlib.pyplot as plt

# define each operation
def add (x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply (x, y):
    return x * y 
def divide (x, y):
    return x / y 

#choose an operation
print("""
      1. addition
      2. subtraction
      3. multiplication
      4. division
      9. Exponential Computation
      10. Graph"""
)

    
operation = int(input('''
Choose an operation by entering a number associated with an operation: '''))
while operation not in [1, 2, 3, 4, 9, 10]:
    print("Invalid operation, try again. ")
    operation = int(input("Choose an operation: "))
if operation in ['9']:
    # for base of exponent
    e = float(input("Enter base of exponent: "))
    j = float(input("Enter exponent: "))
    result = (e ** j)
    print(result)
    sys.exit()

if operation == 10:
    xg = []
    yg = []
    numsx = int(input("How many x values do you want to input?: "))
    for i in range(numsx):
        xg.append(float(input("Enter your x values: ")))
        if not xg:
            na_entry = float(input("Invalid entry, try again:"))
    numsy = int(input("How many y values do you want to input?: "))
    for i in range(numsy):
        yg.append(float(input("Enter your y values: ")))
    plt.plot(xg, yg)
    plt.show()
    sys.exit()
#chose integer or fraction input
print('''
    5. integer/decimal
    6. fraction'''  
)

number_type_choice = int(input("Enter '5' for integer/decimal input or '6' for fractional input: "))
while number_type_choice not in [5, 6]:
    print("Invalid entry, try again. ")
    number_type_choice = int(input("Choose an input: "))

if number_type_choice == 5:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: ")) 
    if operation == 1:
        result = add(x, y)
        print(result)
    elif operation == 2:
        result = subtract(x, y)
        print(result)
    elif operation == 3:
        result = multiply(x, y)
        print(result)
    elif operation == 4:
        if y == 0:
            ZeroDivisionError
            print("Error, cannot divide by 0.")
            y = float(input("Enter new denominator: "))
            result = divide(x , y)
            print(result)
        elif y not in ['0']:
            result = divide(x, y)
            print (result)
        
# for irrational values
if number_type_choice == 6:
    #first fraction
    from fractions import Fraction
    print('''       
    For fraction one
          ''')
    x1 = int(input("Enter numerator: "))
    y1 = int(input("Enter denominator: "))
    if y1 == 0:
        ZeroDivisionError
        y1 = int(input("Invalid entry, input new denominator: "))
    f = Fraction(x1,y1)
    #second fraction
    print('''
    For fraction two''')
    x1 = int(input("Enter numerator: "))
    y1 = int(input("Enter denominator: "))
    if y1 == 0:
        ZeroDivisionError
        y1 = int(input("Invalid entry, input new denominator: "))
    g = Fraction(x1,y1)
    if operation == 1:
        result = add(f,g)
        print(result)
    elif operation == 2:
        result = subtract(f,g)
        print(result)
    elif operation == 3:
        result = multiply(f,g)
        print(result)
    elif operation == 4:
        result = divide(f,g)
        print(result)