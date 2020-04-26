from random import randint

if __name__ == "__main__":

    nums = [randint(15, 35) for _ in range(10)]

    result_nums = [nums[i] for i in range(1,len(nums)) if nums[i]>nums[i-1]]

    print(nums)
    print(result_nums)
