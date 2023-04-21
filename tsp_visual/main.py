import pygame
import gfx
import threading
from util import *
from algo_info import ALGO_INFO, DIVIDERS

# 0. 알고리즘은 껍데기만 만들었다.
# 1. 좌표 찍기
# 2. Loop 만들기

# 1. 알고리즘 정보를 가져온다.
# 2. 무한반복
# 2-1. 알고리즘을 배치한다.
# 2-2. 그리면 된다.(?)
# 점, 선, 텍스트
# draw_point(x, y) => 값 반환하지 않음
# draw_line(x, y) => 값 반환하지 않음
# draw_text(x, y) => 값 반환하지 않음
def loop():
    for i in range(len(ALGO_INFO)):
        if ALGO_INFO[i]["depends"] == -1:
            threads[i].run()

    while True:
        gfx.check_events()
        gfx.draw_dividers(surface, DIVIDERS)

        for i in range(len(ALGO_INFO)):
            if i < len(sim):
                gfx.draw_text_top_left(surface, 
                                       ALGO_INFO[i]["name"],
                                       GREEN,
                                       font,
                                       *ALGO_INFO[i]["name_coords"])
                gfx.draw_path(surface, list_of_cities_list[i], sim[i].best_order)

            elif len(sim[ALGO_INFO[i]["depends"]].best_order) != 0:
                pass

        pygame.display.update()
        surface.fill(BLACK)

    # 애니메이션 나오게 하고 싶다!!!!
    # p를 만들어야 한다.(랜덤으로 만들 껀데, 답이 있는 랜덤이어야 한다!)

    
    

pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Consolas", FONT_HEIGHT)
cities = make_cities(5)
list_of_cities_list = []
sim = []
threads = []

# *을 붙여서 해체구문으로 구현.
for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]["displacement"]))

# Thread 에러(동기화 문제)
for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] == -1:
        sim.append(ALGO_INFO[i]["sim"](list_of_cities_list[i]))
        threads.append(threading.Thread(target=sim[i].find))
        threads[i].daemon = True

if __name__ == "__main__":
    pygame.display.set_caption("TSP - Visualizer")
    # print(ALGO_INFO[i]["displacement"])
    loop()
    



