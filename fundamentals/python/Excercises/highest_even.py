def highest_even(nums):
    highest = None
    for n in nums:
        if n % 2 == 0:
            if highest is None or n > highest:
                highest = n
    return highest

print(highest_even([10, 2, 3, 400, 8]))
