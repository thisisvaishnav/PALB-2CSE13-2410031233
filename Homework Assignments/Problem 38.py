def subsets(nums):
    result = []
    
    def dfs(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            dfs(i + 1, current)
            current.pop()
    
    dfs(0, [])
    return result


# Given Examples
print(subsets([1,2,3]))
print(subsets([0]))