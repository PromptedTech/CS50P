# Ask for mass in kilograms (the "m" in E = mc²)
m = int(input('m: '))

# Calculate energy using Einstein's famous formula E = mc²
# The speed of light (c) is approximately 300,000,000 meters per second
E = m * 300000000 ** 2

# Print the result (energy in joules)
print(f'E: {E}')
