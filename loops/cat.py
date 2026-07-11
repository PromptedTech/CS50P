# i = 3
# while i > 0:
#     print('meow')
#     i = i - 1

# for i in range(6):
#     print('meow')

# while True:
#     n = int(input("Number of meows: "))
#     if n > 0:
#         break

# for _ in range(n):
#         print("meow")

def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input('Whats n? '))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print('meow')

main()