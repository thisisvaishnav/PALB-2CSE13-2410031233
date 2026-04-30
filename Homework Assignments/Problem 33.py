def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    
    def dfs(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current.append(candidates[i])            
            dfs(i + 1, current, remaining - candidates[i])
            current.pop()
    
    dfs(0, [], target)
    return result


# Given Examples
print(combinationSum2([10,1,2,7,6,1,5], 8))
print(combinationSum2([2,5,2,1,2], 5))