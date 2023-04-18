import numeric
import random

# 리미트는 반드시 필요하다.
LIMITS = 100

def first_choice(p):
    current = numeric.random_init(p)
    # value_distance는 최적값일 것이다.
    value_distance = numeric.evaluate(current, p)
    # 다시 처음부터 돌리기 위한 값 선언
    i = 0
    # 제한횟수까지 돌 동안...
    while i < LIMITS:
        pass

    # 알고리즘을 활용해서 최적값을 변경하는 코드 작성
    # value_distance를 어떻게 줄일까?
    return current, value_distance

# 어떤 변이가 제일 좋을까?
def random_mutant(current, p):
    DELTA = 0.01
    # 델타값 구간 안의 어떤 값을 가져오면 된다.
    delta = [-DELTA, DELTA]
    d = random.choice(delta)
    return d

def inversion(current, i, j):
    pass

if __name__ == "__main__":
    p = tsp.create_problem("./data/Convex.txt")
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)
