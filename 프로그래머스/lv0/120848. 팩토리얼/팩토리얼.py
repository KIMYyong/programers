def solution(n):
    answer = 1
    num = 0
    for i in range(1, n+1, 1):
        answer *= i
        num += 1
        if answer > n:
            return num-1
        elif answer == n:
            return num