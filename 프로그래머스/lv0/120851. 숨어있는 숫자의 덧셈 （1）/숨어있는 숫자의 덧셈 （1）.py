def solution(my_string):
    answer = 0
    number = '1234567890'
    num2 = []
    for i in my_string:
        if i in number:
            num2.append(int(i))
    for j in num2:
        answer += j
    return answer