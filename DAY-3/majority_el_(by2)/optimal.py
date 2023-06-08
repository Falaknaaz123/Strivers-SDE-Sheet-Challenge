def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    return candidate
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(result)  # Output: 2
