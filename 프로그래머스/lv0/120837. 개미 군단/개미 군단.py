def solution(hp):
    answer = 0
    answer = (hp//5)+(hp-(hp//5)*5)//3+(hp-(hp//5)*5)%3
    return answer