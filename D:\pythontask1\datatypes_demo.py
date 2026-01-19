# datatypes_demo.py

# Declare variables of different data types

int_var = 10
float_var = 5.5
string_var = "Python"
bool_var = True

# Print the type of each variable

print("int_var:", int_var, "| Type:", type(int_var))
print("float_var:", float_var, "| Type:", type(float_var))
print("string_var:", string_var, "| Type:", type(string_var))
print("bool_var:", bool_var, "| Type:", type(bool_var))

print("\nArithmetic Operations:")

# Perform arithmetic operations

print("Addition:", int_var + float_var)
print("Subtraction:", int_var - float_var)
print("Multiplication:", int_var * float_var)
print("Division:", int_var / float_var)

print("\nType Casting with Error Handling:")

# Convert string input to int and float with error handling

try:
user_int = int(input("Enter an integer: "))
user_float = float(input("Enter a float: "))
print("Converted Integer:", user_int)
print("Converted Float:", user_float)
except ValueError:
print("Invalid input! Please enter numeric values.")

print("\nString Concatenation:")

# Concatenate string and number

age = 20
print("My age is " + str(age))

print("\nDynamic Typing:")

# Demonstrate dynamic typing

dynamic_var = 100
print(dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = "Now I am a string"
print(dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = 3.14
print(dynamic_var, "| Type:", type(dynamic_var))
