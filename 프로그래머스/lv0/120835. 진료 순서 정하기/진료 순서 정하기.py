def solution(emergency):
    answer = []
    b = []
    answer.extend(emergency)
    emergency.sort(reverse=True)
    for i in answer :
        b.append(emergency.index(i)+1)
    return b