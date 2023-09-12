def solution(numbers):
    numbers.sort()
    mul = []
    mul = [numbers[0]*numbers[1],
           numbers[0]*numbers[-1],
           numbers[-1]*numbers[-2]]
    mul.sort()
    return mul[-1]