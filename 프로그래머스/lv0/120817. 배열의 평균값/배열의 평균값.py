
def solution(numbers):
    num = 0
    for i in range(len(numbers)):
        num += numbers[i]
        answer = num/len(numbers)
    return answer