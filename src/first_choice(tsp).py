import tsp
import random

LIMITS = 100

def first_choice(p):
    current = tsp.random_init(p)
    # value_distance는 최적값일 것이다.
    value_distance = tsp.evaluate(current, p)
    # 다시 처음부터 돌리기 위한 값 선언
    i = 0
    # 제한횟수까지 돌 동안...
    while i < LIMITS:
        successer = random_mutant(current, p)
        _value_distance = tsp.evaluate(successer, p)
        # 혹시 기존 값보다 작니?
        if _value_distance < value_distance:
            current = successer
            value_distance = _value_distance
            i = 0
        else:
            i += 1

    # 알고리즘을 활용해서 최적값을 변경하는 코드 작성
    # value_distance를 어떻게 줄일까?
    return current, value_distance
# 변이 알고리즘 -> 유전 알고리즘
def random_mutant(current, p):
    while True:
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j:
            # 순서 뒤집기
            cur_copy = inversion(current, i, j)
            break
    return cur_copy

# 순서 뒤집기
def inversion(current, i, j):
    cur_copy = current[:]
    while i < j:
        cur_copy[i], cur_copy[j] = cur_copy[j], cur_copy[i]
        # 거꾸로 돌기
        i += 1
        j -= 1
    return cur_copy

if __name__ == "__main__":
    p = tsp.create_problem("./data/tsp30.txt")
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)
