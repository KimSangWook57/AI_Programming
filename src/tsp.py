import math
import random
# 내가 직접 작성하기
# 읽기 좋게 쓰기

# TODO: 인접행렬 그래프 만들고 다시 해보기
def create_problem(filename):
    f = open(filename, "r")
    num_cities = int(f.readline())

    locations = []
    for line in f.readlines():
        locations.append(eval(line))
    
    f.close()
    table = create_distance_table(num_cities, locations)
    return num_cities, locations, table

def create_distance_table(num_cities, locations):
    # 거리 계산 필요
    # 맨하튼 => 격자(grid world)
    # 유클리드 거리(점 2개 필요?)
    
    table = []
    for i in range(num_cities):
        # 재귀적인 코드
        line = []
        for k in range(num_cities):
            distance = math.sqrt(((locations[i][0] - locations[k][0]) ** 2) + (locations[i][1] - locations[k][1]) ** 2)
            # distance = abs(locations[i][0] - locations[k][0]) + abs(locations[i][1] - locations[k][1]) # 맨하튼 거리
            line.append(distance)
        table.append(line)
    return table

def random_init(p):
    # 결과 shuffle!
    # 무작위 좌표를 만들어내야 한다.
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init

def evaluate(current, p):
    cost = 0
    num_cities, locations, table = p
    # 인덱스를 써야 한다.
    for i in range(num_cities):
        cost += table[current[i]][current[i-1]]
    return cost

def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of cities : {n}")
    locations = p[1]
    table = p[2]
    for i in range(n):
        print(f"{i}")
        if i % 5 == 4:
            print()
        
if __name__ == "__main__":
    # 문제 인스턴스 생성
    p = create_problem("./data/tsp30.txt")
    # print(p)
    # describe_problem(p)
    # 초기 솔루션 생성
    init = random_init(p)
    # 솔루션에 대한 문제평가
    print(evaluate(init, p))