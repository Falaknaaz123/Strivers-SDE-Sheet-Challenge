def majority_element(nums):
    n = len(nums)
    
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
        if count > n // 2:
            return nums[i]
    
    return None
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(result)  # Output: 2
