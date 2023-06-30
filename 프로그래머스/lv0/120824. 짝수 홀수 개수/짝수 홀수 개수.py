def solution(num_list):
    num1 = 0
    num2 = 0
    for i in num_list:
        if i % 2 ==0:
            num1 += 1
        elif i % 2 != 0:
            num2 += 1
    return [num1,num2]