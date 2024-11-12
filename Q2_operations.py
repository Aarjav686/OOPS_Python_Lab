def arithmetic_operations():
   
    num1 = float(input("Enter the first floating-point number: "))
    num2 = float(input("Enter the second floating-point number: "))

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 

    print("\nResults:")
    print(f"Addition: {addition:.2f}")
    print(f"Subtraction: {subtraction:.2f}")
    print(f"Multiplication: {multiplication:.2f}")
    print(f"Division: {division:.2f}")
    
arithmetic_operations()
