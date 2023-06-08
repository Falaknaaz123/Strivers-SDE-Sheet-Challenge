from collections import defaultdict
def majority_element(nums):
    counter = defaultdict(int)

    for num in nums:
        counter[num] += 1
        if counter[num] > len(nums) // 2:
            return num

    return None
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(result)  # Output: 2
