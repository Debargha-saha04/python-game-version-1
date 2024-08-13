import pygame
import random
import os
pygame.init()


#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)


#variables
screen_width=900
screen_height=600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snakes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text,color,x,y):
    screen_text=font.render (text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
       pygame.draw.rect(gameWindow, black, [x,y, snake_size, snake_size])


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    velocity_x = 0
    velocity_y = 0
    vel = 2
    food_x = random.randint(0, screen_width - 100)
    food_y = random.randint(0, screen_height - 100)
    score = 0
    fps = 100
    snk_list = []
    snk_length = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()



    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                highscore = f.write(str(highscore))
            gameWindow.fill(white)
            text_screen("tu mar gya bhai, yeh bhi na kar paya,", red, 100, 250)
            text_screen("chal phirse try kar", red, 100, 310)

            for event in pygame.event.get() :
                if event.type ==pygame.QUIT:
                    exit_game= True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = vel
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -vel
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -vel
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = vel
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y


            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                food_x = random.randint(0, screen_width-200 )
                food_y = random.randint(0, screen_height -200)
                snk_length +=5
                if (score > int(highscore)):
                    highscore=score

            gameWindow.fill(white)
            text_screen("score:" + str(score ) + "highscore:" + str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()
