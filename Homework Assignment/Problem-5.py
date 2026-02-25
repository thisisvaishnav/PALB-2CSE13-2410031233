def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        seen[nums[i]] = i
    return []


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
