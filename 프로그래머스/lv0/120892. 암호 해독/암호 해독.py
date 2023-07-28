def solution(cipher, code):
    answer = ''
    num = 1
    for i in str(cipher):
        if num % code == 0:
            answer += str(i)
            num +=1
        else:
            num +=1
    return answer