# import os

# #  Will list directories
# directories = os.listdir()
# print(directories)


def say_something():
    print("Hello from this module")


# say_something()


def square(x):
    return x * x


def even_or_odd(n):
    if n % 2 == 0:
        # print(True)
        return True
    else:
        # print(False)
        return False


def main():
    x = 25
    num = 5
    say_something()
    square_num = square(x)
    new_num = even_or_odd(num)


# comes back as __main__ when calling specifically this file else it comes back as the name of the file ("test_export")
# print(__name__)

if __name__ == '__main__':  # This is good for testing
    main()
