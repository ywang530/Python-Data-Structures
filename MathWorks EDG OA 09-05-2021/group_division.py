def minNumGroup(weights, maxRange):
    i = 0
    weights = sorted(weights)
    result = []
    path = []
    for j in range(len(weights)):
        # print(path)
        diff = weights[j] - weights[i]
        if diff <= maxRange:
            path.append(weights[j])
            if j == len(weights) - 1:
                result.append(list(path))
        else:
            result.append(list(path))
            path = []
            i = j
            path.append(weights[i])

    if i == j:
        result.append(list(path))

    print(result)
    return len(result)
            
        







if __name__ == '__main__':
    n = 5
    weights = [2, 5, 8, 4, 5, 7, 11]
    maxRange = 2

    N = minNumGroup(weights, maxRange)
    print(N)