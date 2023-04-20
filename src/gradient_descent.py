from numeric import *

ALPHA = 0.01
EPSILON = 0.0001

def steepest_ascent(p):
    current = random_init(p)
    values = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, value_best_of) = best_of(neighbors, p)
        if value_best_of >= values:
            break
        else:
            current = successor
            values = value_best_of
    return (current, values)


def mutants(current, p):
    neighbors = []
    for i in range(0, len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors

def best_of(neighbors, p):
    all = []
    for i in range(0, len(neighbors)):
        all.append(evaluate(neighbors[i], p))
    best_value = min(all)
    best = neighbors[all.index(min(all))]
    return (best, best_value)

def display_setting():
    print()
    print("Search algorithm: Gradient Descent")
    print()
    print(f"Update rate: {ALPHA}")
    print(f"Calculating Drtivatives: {EPSILON}")

# 매개변수 뭐잡음?
# 미분은 내가 어떻게 해야 함?
# 기울기?
# y = ax + b (점과 직선의 방정식)
# 미분을 구해서 차이는 어떻게 구해야 함?
def gd(current, p, EPSILON):
    gradient = []
    domain = p[1] # 하한과 상한이 있어야 한다.
    low = domain[1]
    up = domain[2]
    for i in range(len(current)):
        # 첫번째 나와!
        value = current[1]
        # 주변에 애들 다 데려와!
        derivate = current[:i]
        # 중앙값이니?
        if (low[i] <= value + EPSILON <= up[i]):
            value = value + EPSILON
        derivate.append(value)
        # i 다음부터 
        derivate.extend(current[i+1:])
        gradient.append((evaluate(derivate, p) - value) / EPSILON )

    return gradient

def take_step(current, gradient):
    suc = []
    for i in range(len(current)):
        
        suc.append(current[i] - gradient[i])
    return suc

if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    current = random_init(p)
    value = evaluate(current, p)
    while True:
        gradient = gd(current, p, EPSILON)
        next_p = take_step(current, gradient)
        next_n = evaluate(next_p, p)
        if next_n < value:
            current = next_p
            value = next_n
        else:
            break
    print(current, value)


    # describe_problem(p)
    # display_setting()
    # display_result(solution, minimum)