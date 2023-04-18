import random
# 내가 직접 작성하기
# 읽기 좋게 쓰기

def create_problem(filename):
    f = open(filename, "r")
    expression = f.readline()

    var_names = []
    low = []
    up = []

    for line in f.readlines():
        _temp = line.split(",")
        var_names.append(_temp[0])
        low.append(float(_temp[1]))
        up.append(float(_temp[2]))
    domain = [var_names, low, up]
    return (expression, domain)


def random_init(p):
    domain = p[1]
    init = []
    for i in range(0, len(domain[0])):
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init


def evaluate(current, p):
    expr = p[0]
    var_names = p[1][0]
    for i in range(len(var_names)):
        assignment = var_names[i] + "=" + str(current[i])
        exec(assignment)
    return eval(expr)


def describe_problem(p):
    print()
    print("Objective function:")
    print(p[0])
    print("Search space:")
    var_names = p[1][0]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(f" {var_names[i]} : {low[i], up[i]}")


def display_result(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))


def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)


if __name__ == "__main__":
    # 문제 인스턴스 생성
    p = create_problem("./data/Convex.txt")
    # 문제 인스턴스 출력
    describe_problem(p)
    # 초기 솔루션 생성
    solution = random_init(p)
    # 솔루션에 대한 문제평가
    minimum = evaluate(solution, p)
    # 가장 작은 값을 표시
    print(f"{minimum}")
