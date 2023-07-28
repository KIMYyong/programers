def solution(array, n):
    array.sort()
    num = []
    for i in range(len(array)):
        if n - array[i] < 0:
            num.append(array[i]-n)
        else:
            num.append(n-array[i])
    
    return array[num.index(min(num))]