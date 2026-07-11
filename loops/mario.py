# def main():
#     print_row(4)

# def print_row(width):
#     print('?' * width)

# main()

# def main():
#     num = int(input('What num is in your head? '))
#     print_square(num)

# def print_square(size):
#     #for each row in square
#     for i in range(size):
         
#          # for each brick in square
#          for j in range(size):
             
#              # print bricks
#              print("#", end='')
#          print()

# main()

def main():
    num = int(input('what num is in your head? '))
    print_square(num)

def print_square(size):
    for i in range(size):
        print('#' * size)

main()