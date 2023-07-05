def solution(age):
    answer = ''
    age962 = ['a','b','c','d','e','f','g','h','i','j']
    for i in str(age):
        answer +=age962[int(i)]
    
    return answer