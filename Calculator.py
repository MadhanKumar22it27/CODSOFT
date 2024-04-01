import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error! Cannot calculate factorial of a negative number."
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def main():
    while True:
        print("\nAdvanced Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Quit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", exponentiate(num1, num2))
                
        elif choice in ('6', '7'):
            num = float(input("Enter a number: "))
            
            if choice == '6':
                print("Result:", square_root(num))
            elif choice == '7':
                print("Result:", factorial(int(num)))
                
        elif choice == '8':
            print("Exiting Advanced Calculator. Goodbye!")
            break
            
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
