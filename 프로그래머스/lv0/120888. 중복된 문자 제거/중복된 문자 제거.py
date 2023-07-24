def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += str(i)
    return answer