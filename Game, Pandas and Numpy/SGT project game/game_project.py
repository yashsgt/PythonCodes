import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 1200, 700
SCREEN = pygame.display.set_mode(SIZE)

#rgb color code
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
BLACK = 0,0,0
GREEN = 0,255,0

def homeScreen ():
    font1 = pygame.font.SysFont(None, 150)
    text = font1.render(f"SPACE  SHOOTER", True, RED)
    text_2 = font1.render(f"Press Space To Start", True, WHITE)

    while True:
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        SCREEN.blit(text, (100, 200))
        SCREEN.blit(text_2, (100, 450))
        pygame.display.flip()

def playerHealth(count):
    font = pygame.font.SysFont(None, 60)
    text = font.render(f"Health : {count}", True , RED)
    SCREEN.blit(text, (50, 500))

def gameOver():
    font = pygame.font.SysFont(None, 150)
    text = font.render(f"GAME_OVER", True, RED)
    # SCREEN.blit(text, (10, 500))
    while True:
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        SCREEN.blit(text,(245, 400))
        pygame.display.flip()

def gameWon():
    font = pygame.font.SysFont(None, 150)
    text = font.render(f"GAME_WON", True, RED)
    # SCREEN.blit(text, (10, 500))
    while True:
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        SCREEN.blit(text,(245, 400))
        pygame.display.flip()

def main():
    move_x =0

    ship = pygame.image.load("assests/Player Ship Final (1).jpeg")
    ship_w = ship.get_width()
    ship_h = ship.get_height()
    ship_x = WIDTH // 2 - ship_w // 2
    ship_y = (HEIGHT - ship_h)

    enemyShip = pygame.image.load("assests/Enemy final_image.jpg")
    eship_w = enemyShip.get_width()
    eship_w = enemyShip.get_width()
    eship_h = enemyShip.get_height()

    enemyList = []
    nrow = 2
    ncols = WIDTH // eship_w


    #BulletCode
    bullet_w = 8
    bullet_h = 15
    bullet_y = ship_y
    moveBullet = 0


    for i in range (nrow):
        for j in range (ncols):
            enemyX = eship_w * j
            enemyY = eship_h * i
            enemyRect = pygame.Rect(enemyX, enemyY, eship_w, eship_h)
            enemyList.append(enemyRect)

            # enemyList.append([enemyX, enemyY])

    random_enemy = random.choice(enemyList)
    enemy_bullet_w = 5
    enemy_bullet_h = 10
    enemy_bullet_x = random_enemy.x + eship_w//2
    enemy_bullet_y = random_enemy.bottom - 10

    playerHealthCount = 100


    while True:
        bullet_x = ship_x + ship_w // 2 - 2
        evenList = pygame.event.get()
        for event in evenList:
            # print(event)
            if event.type == pygame.QUIT:
                #update the game
                pygame.quit()
                #quit pyhton
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 0.8
                elif event.key == pygame.K_LEFT:
                    move_x = -0.8
                elif event.key == pygame.K_SPACE:
                    moveBullet = -5
            else:
                move_x =0

        SCREEN.fill(WHITE)
        bullet_rect = pygame.draw.rect(SCREEN, GREEN, [bullet_x, bullet_y, bullet_w, bullet_h])
        bullet_y += moveBullet
        SCREEN.blit(ship, (ship_x, ship_y))
        ship_x += move_x

        ship_rect = pygame.Rect(ship_x, ship_y, ship_w, ship_h)
        enemyBullet = pygame.draw.rect(SCREEN, RED, [enemy_bullet_x, enemy_bullet_y, enemy_bullet_w,enemy_bullet_h])
        enemy_bullet_y += 2

        for i in range (len(enemyList)):
            # SCREEN.blit(enemyShip, (enemyList[i][0],enemyList[i][1]))
            SCREEN.blit(enemyShip , (enemyList[i].x, enemyList[i].y))

        for i in range(len(enemyList)):
            if bullet_rect.colliderect(enemyList[i]):
                bullet_y = ship_y
                moveBullet = 0
                del enemyList[i]
                break


        if bullet_y < 0:
            bullet_y = ship_y
            moveBullet = 0

        if enemy_bullet_y > HEIGHT:
            random_enemy = random.choice(enemyList)
            enemy_bullet_x = random_enemy.x + eship_w // 2
            enemy_bullet_y = random_enemy.bottom - 10

        if enemyBullet.colliderect(ship_rect):
            if(len(enemyList) == 0):
                gameWon()
            playerHealthCount -= 1


        if playerHealthCount == 0:
            gameOver()



        playerHealth(playerHealthCount)
        #update the screen
        pygame.display.flip()

homeScreen()