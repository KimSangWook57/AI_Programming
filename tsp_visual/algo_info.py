from util import *
from algo import BruteForce
# 알고리즘을 담아둘 컨테이너 생성
ALGO_INFO = [
    {
        "name" : "Brute Algo",
        "displacement" : (0, FONT_HEIGHT), 
        "name_coords" : (0, 0),
        "length_coords" : (0, HEIGHT + FONT_HEIGHT),
        "depends" : -1,
        "sim" : BruteForce.BruteForceSolver # 알고리즘 넣을 자리
    },

]
# 대각선으로 찍기
DIVIDERS = [
    (0, HEIGHT + FONT_HEIGHT, WINDOW_WIDTH, HEIGHT + FONT_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
]