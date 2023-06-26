def solution(n):
    answer = 0
    for i in range(101):
        if n/7 > i:
            answer = i+1
        if n/7 == i:
            answer = i
        elif n/7 <1:
            answer = 1
    return answer