fruitNutrients = [1, 2, 3, 0]
reqNutrients = 3

def countNumberOfSubarrays(nums, target):
    result = []
    path = []
    
    def backtrack(nums, target, startIdx):
        if sum(path) == target and len(path) <= 2:
            result.append(list(path))

        for i in range(startIdx, len(nums)):
            path.append(nums[i])
            backtrack(nums, target, i + 1)
            path.pop()
        
        return

    
    backtrack(nums, target, 0)
    print(result)
    return len(result)



if __name__ == '__main__':
    fruitNutrients = [1, 2, 3, 0]
    reqNutrients = 3

    fruitNutrients = [1, 2, 3, 0, -2, 5]
    reqNutrients = 3

    N = countNumberOfSubarrays(fruitNutrients, reqNutrients)
    print(N)