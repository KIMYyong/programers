def solution(balls, share):
    answer = 0
    ball = 1
    ballshare = 1
    Share = 1
    for i in range(balls,0,-1):
        ball *= i
    for i in range(balls-share,0,-1):
        ballshare *= i
    for i in range(share,0,-1):
        Share *= i
    return ball/(ballshare*Share)