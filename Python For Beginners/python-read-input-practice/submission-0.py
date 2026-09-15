def add_two_numbers() -> int:
    nums = input().split(",")
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
