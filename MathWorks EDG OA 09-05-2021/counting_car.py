from collections import Counter

def frequencyOfMaxValue(numCars, hourStartQ):
    freq = {}

    for i in range(len(numCars)):
        count = Counter(numCars[i::]).most_common(1)
        freq[i+1] = count[0][1]
    
    result = []
    for hr in hourStartQ:
        result.append(freq[hr])
    
    return result
if __name__ == '__main__':
    numCars = [5, 3, 5, 4, 2]
    hourStartQ = [1, 2, 4, 5]

    N = frequencyOfMaxValue(numCars, hourStartQ)
    print(N)