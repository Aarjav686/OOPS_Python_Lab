def print_variable_info():
   
    integer_var = int(input("Enter an integer: "))
    float_var = float(input("Enter a float: "))
    string_var = input("Enter a string: ")
    bool_var = input("Enter a boolean value (True/False): ") == "True"  # Convert input to boolean

    print("\nVariable Values and their Types:")
    print(f"Integer value: {integer_var}, Type: {type(integer_var)}")
    print(f"Float value: {float_var}, Type: {type(float_var)}")
    print(f"String value: '{string_var}', Type: {type(string_var)}")
    print(f"Boolean value: {bool_var}, Type: {type(bool_var)}")

print_variable_info()
