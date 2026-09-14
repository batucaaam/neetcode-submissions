from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum = 0
    for i in nums:
        sum += i
    return sum

def get_min(nums: List[int]) -> int:
    min = 999999
    for i in nums:
        if i < min:
            min = i
    return min

def get_max(nums: List[int]) -> int:
    max = 0
    for i in nums:
        if i > max:
            max = i
    return max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
