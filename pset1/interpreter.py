# Ask the user to type a math expression like: 1 + 2  or  10 / 4
expression = input("Expression: ")

# Split the expression into 3 parts using the space as a separator
# For example "1 + 2" becomes: x = "1", y = "+", z = "2"
x, y, z = expression.split(" ")

# Convert x and z from text (string) to whole numbers (integers) so we can do math
x = int(x)
z = int(z)

# Check which operator was typed and do the matching math operation
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Print the result with exactly 1 decimal place (e.g. 3.0 or 2.5)
print(f"{result:.1f}")
