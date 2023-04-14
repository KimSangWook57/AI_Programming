import random

# 1. 파일을 읽어서 뭔가 만듬
# 2. 그 무언가로 초기값을 생성
# 3. Convex.txt 파일의 수식과 값을 이용해서 계산

def create_problem(filename):
    # 1-1 파일을 읽자!
    ini_file = open(filename, 'r')
    expression = ini_file.readline().strip()
    var_names = []
    low = []
    up = []

    for line in ini_file.readlines():
        # 1-2 수식과 리스트로 분리
        var_names.append(line.split(",")[0])
        low.append(float(line.split(",")[1]))
        up.append(float(line.split(",")[2]))

        # print(tuple(line.split(",")))
        # x, y, z = tuple(line.split(","))
    ini_file.close()
    domain = [var_names, low, up]
    return (expression, domain)

def random_init(p):
    expression, domain = p
    init = []
    for i in range(len(domain[0])):
        # 최대 / 최소 사이의 랜덤 값
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init

# state = 상태
def evaluate(state, p):
    num_eval = 0
    # p는 튜플이라고 가정(해체문법)
    # expression, _ = p
    # 현실은 p값이 튜플이라는 보장이 없음
    expression = p[0]
    var_name = p[1][0] # x1  

    for i in range(len(var_name)):
        assignment = var_name[i] + '=' + str(state[i])
        exec(assignment)
    return num_eval

# 메인 실행시점 정해주기
if __name__ == "__main__":
    # print(create_problem("./data/Convex.txt"))
    create_problem("./data/Convex.txt")