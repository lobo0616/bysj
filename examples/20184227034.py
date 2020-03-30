import time

# x, y =

def sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    while True:
        pass
    return nums


def two_sum(str1, str2):
    return str1 + str2
