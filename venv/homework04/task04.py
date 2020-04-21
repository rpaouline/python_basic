from random import randint

if __name__ == "__main__":

    nums = [randint(15, 25) for _ in range(20)]

    result_nums = [i for i in nums if nums.count(i)==1]

    print(nums)
    print(result_nums)
