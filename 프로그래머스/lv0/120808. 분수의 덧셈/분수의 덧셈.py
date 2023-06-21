import math

def solution(denum1, num1, denum2, num2):
    num = num1 * num2
    denum = denum1 * num2 + denum2 * num1

    gcd_value = math.gcd(num, denum)

    return [denum / gcd_value, num / gcd_value]