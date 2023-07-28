def solution(my_string):
    answer = ''
    small = 'abcdefghijklmnopqrstuwyz'
    for i in range(len(my_string)):
        if my_string[i] == my_string[i].upper():
            answer += my_string[i].lower()
        else:
            answer += my_string[i].upper()
        
    return answer