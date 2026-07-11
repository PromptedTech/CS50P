text = input("Input: ")
output = ""

for char in text:
    if char.lower() in "aeiou":
        continue
    output += char

print(output)