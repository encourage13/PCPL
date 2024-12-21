from builtins import sorted

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
def sortArray(array):
    for i in range( len(array)-1):
        for j in range( len(array)-i-1):
            if abs(array[j]) < abs(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

sort = lambda array: sorted(array, key=abs, reverse=True)



if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)

