from functools import reduce

if __name__ == "__main__":

    my_list = [i for i in range(100,1001) if i & 1 == 0]

    result = reduce(lambda a, b : a * b, my_list)
