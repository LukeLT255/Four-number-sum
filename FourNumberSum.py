def fourNumberSum(array, targetSum):
    quads = []
    allPairSums = {}


    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quads.append(pair + [array[i], array[j]])

        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quads


if __name__ == '__main__':
    size = input('Please enter the size of the list you wish to enter: ' + '\n')
    sumList = [int(input('Number ' + str(x + 1) + ': ')) for x in range(int(size))]
    targetSum = input('Please enter a target sum.' + '\n')
    print(fourNumberSum(sumList, int(targetSum)))
