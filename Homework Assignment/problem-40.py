def subsets(nums):
    result = [[]]
    for num in nums:
        new_subsets = []
        for s in result:
            new_subsets.append(s + [num])
        for s in new_subsets:
            result.append(s)
    return result


nums = list(map(int, input("Enter array elements: ").split()))
print("Subsets:", subsets(nums))
