def divide(a: int, b: int) -> float:
    """
    The function returns result of two integers division
    :param a: dividend
    :param b: divider
    :return: a/b
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("We cant divide on 0")


args_input = input("Input a and b separated by comma to get a/b:\n")

args = args_input.split(",")

try:
    print(divide(int(args[0]), int(args[1])))
except IndexError:
    print("Input two arguments (extra will be ignored)!")
except ValueError:
    print("Input two integers!")
finally:
    print("Bye.")
