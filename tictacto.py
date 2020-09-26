import pygame as pg
import time

pg.init()

screen = pg.display.set_mode((900, 900))
running = True
intro = True

pg.key.set_repeat(1, 1)

def draw_background(mouse):
    screen.fill((255,255,255))
    for line in range(2):
        pg.draw.line(screen, (0,0,0), (300+300*line, 0),(300+300*line, 1200),2)
        pg.draw.line(screen, (0,0,0), (0, 300+300*line),(1000, 300+300*line, ),2)
    if not game:
        for a in return_:
            pg.draw.rect(screen, (255,255,0), (2+(a%3)*300,2+(a//3)*300,298,298))
    for a in enumerate(ttt_list):
        if a[1] == "O":
            pg.draw.circle(screen, (0,255,0), (150 + a[0]%3*300 , 150+a[0]//3*300), 120, 30)
        elif a[1] == "X":
            pg.draw.line(screen,(255, 0, 0),((a[0]%3)*300+50, (a[0]//3)*300+50), ((a[0]%3)*300+250, (a[0]//3)*300+250), 50 )
            pg.draw.line(screen,(255, 0, 0),((a[0]%3)*300+250, (a[0]//3)*300+50), ((a[0]%3)*300+50, (a[0]//3)*300+250), 50 )

def check_win():
    global return_, draw
    win = False
    return_ = []
    draw = True
    for player in ["O", "X"]:
        for a in range(3):
            if player == ttt_list[a*3] and ttt_list[a*3] == ttt_list[a*3+1] and  ttt_list[a*3+1] == ttt_list[a*3+2]:
                win = True
                return_ = [a*3,a*3+1,a*3+2]
        for a in range(3):
            if player == ttt_list[a] and ttt_list[a] == ttt_list[a+3] and  ttt_list[a+3] == ttt_list[a+6]:
                win = True
                return_ = [a, a+3, a+6]
        if player == ttt_list[0] and  ttt_list[0] == ttt_list[4] and  ttt_list[4] == ttt_list[8]:
            return_ = [0,4,8]
            win = True
        if player == ttt_list[2] and ttt_list[2] == ttt_list[4] and  ttt_list[4] == ttt_list[6]:
            win = True
            return_ = [2,4,6]
    for a in ttt_list:
        if a == " ":
            draw = False
    # if win or draw:
    #     return True

    if win and not draw:
        draw = False
        return True
    elif draw and not win:
        draw = True
        return True
    elif win and draw:
        draw = False
        return True
    else:
        return False

def draw_text(text, font_size, x,y):
    global screen
    screen.blit(pg.font.SysFont("arial", font_size).render(text, True, (0,0,0)),(x,y))

while running:
    game = True
    ttt_list = [" "," "," "," "," "," "," "," "," "]
    player = "O"
    while game:
        if check_win():
            game = False
        mouse = []
        for a in pg.mouse.get_pos():
            mouse.append(a//300)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
                running  = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if  ttt_list[mouse[0] + mouse[1]*3] == " ":
                    ttt_list[mouse[0] + mouse[1]*3] = player
                    if player == "O":
                        player = "X"
                    else:
                        player = "O"
            if event.type == pg.KEYDOWN:
                    intro = False
                    time.sleep(0.5)
            if event.type == pg.QUIT:
                running = False
                game = False
                end = False
        if intro:
            screen.fill((255,255,255))
            draw_text("Press Any Key To Start", 70,99, 342)
        else:
            draw_background(mouse)
            if  ttt_list[mouse[0] + mouse[1]*3] == " ":
                if player == "O":
                    pg.draw.circle(screen, (0,255,0), (150 + mouse[0]*300 , 150+mouse[1]*300), 120, 30)
                else:
                    pg.draw.line(screen,(255, 0, 0),(mouse[0]*300+50, mouse[1]*300+50), (mouse[0]*300+250, mouse[1]*300+250), 50 )
                    pg.draw.line(screen,(255, 0, 0),(mouse[0]*300+250, mouse[1]*300+50), (mouse[0]*300+50, mouse[1]*300+250), 50 )
        pg.display.update()
    if not draw:
        time.sleep(3)
    else:
        time.sleep(0.5)
    end = True
    if player == "O":
        player = "X"
    else:
        player = "O"
    change_x = 0
    change_y = 0
    while end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                end = False
            if event.type == pg.KEYDOWN:
                end = False
        screen.fill((255,255,255))
        if draw:
            draw_text("Draw !".format(player),100, 310, 237)
        else:
            draw_text("player {} Win !".format(player),100, 145, 237)
        draw_text("Press Any Key To Start", 50, 198, 492)
        pg.display.update()