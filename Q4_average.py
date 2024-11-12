def average_and_deviation(num1, num2):
    
    average = (num1 + num2) / 2
    deviation1 = num1 - average
    deviation2 = num2 - average
    
    return average, deviation1, deviation2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

average, deviation1, deviation2 = average_and_deviation(num1, num2)

print(f"Average of {num1} and {num2} is: {average:.2f}")
print(f"Deviation of {num1} from the average is: {deviation1:.2f}")
print(f"Deviation of {num2} from the average is: {deviation2:.2f}")