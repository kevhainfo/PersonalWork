"""
This is where the data for the pong bot is collected. You play an indefinite amount of rounds against an invincible opponent until you decide that there is enough data for the pong bot.
Then, in trainBot.py, the bot is trained to mimic your movements.
In playAgainstBot.py, you play against the bot, which updates the opponent's paddle in real time.
"""
###IMPORTS
import pygame
import time
import random
import pandas as pd

###initalize pygame
pygame.init()

###define size of screen
SIZE = (1200, 800)
screen = pygame.display.set_mode(SIZE)

### set game loop to run
run = True

### important variables to keep time
now = 0
last = time.time()
delta = 0

### initalize scores for player and opponent
scorePlayer = 0
scoreEnemy = 0

### declare paddle array
paddles = []

###ball class has six variables: x, y, velocity in x direction, velocity in y direction, radius, and speed
class ball:

    def __init__(self, speed):

        self.speed = speed

        self.x = int(SIZE[0] / 2)
        self.y = int(SIZE[1] / 2)
        self.vX = self.speed * random.choice([-1, 1])
        self.vY = random.randint(-100, 100) / 100.0 * self.speed

        # radius initialization/definition
        self.radius = 8

    def draw(self):
        global scorePlayer, scoreEnemy

        self.x = self.x + self.vX * delta
        self.y = self.y + self.vY * delta
        ### check if ball hits paddles
        for p in paddles:
            if (self.y > p.y and self.y < p.y + p.h):

                if (self.x + self.radius > p.x and self.x - self.radius < p.x + p.w):
                    self.vX = -self.vX
                    self.vY+=random.randint(-100, 100) / 100* self.speed
                    if self.vX < 0:
                        self.x = p.x - self.radius
                    else:
                        self.x = p.x + p.w + self.radius

        # ----------------------------------------Hitting Left and Right
        if (self.x > SIZE[0] - self.radius):
            scorePlayer += 1
            self.x = int(SIZE[0] / 2)
            self.y = int(SIZE[1] / 2)
            self.vX = -self.speed
            self.vY = random.randint(-100, 100) / 100.0 * self.speed
            # self.vX = -abs(self.vX)
            # self.x = SIZE[0]-self.radius

        if (self.x < self.radius):
            scoreEnemy += 1
            self.x = int(SIZE[0] / 2)
            self.y = int(SIZE[1] / 2)
            self.vX = self.speed
            self.vY = random.randint(-100, 100) / 100.0 * self.speed
            # self.vX = abs(self.vX)
            # self.x = self.radius
        # ----------------------------------------Hitting Top and Bottom
        if (self.y > SIZE[1] - self.radius):
            self.vY = -abs(self.vY)
            self.y = SIZE[1] - self.radius

        if (self.y < self.radius):
            self.vY = abs(self.vY)
            self.y = self.radius

        # surface, color, position, radius
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)


class paddle:

    def __init__(self, x, y=0, height=100, width=10,v=0):
        global paddles

        paddles.append(self)

        self.x = x
        self.y = y
        self.h = height
        self.w = width

    def draw(self):
        self.y = min(max(self.y, 0), SIZE[1] - self.h)
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.w, self.h))

### periodically save training data into dataframe(table)
class results:
    def __init__(self):
        self.i=1 ### saves which row to save data to
    def record(self,ball, player):
        df.loc[self.i] = [ball.x, ball.y, ball.vX, ball.vY, player.y+player.h/2, player.y-df.loc[self.i-1][4]+player.h/2]
        self.i = self.i + 1
        print(df)

###initialize data frame
df = pd.DataFrame(columns=['ballX', 'ballY','ballVX','ballVY','playerY','dir']);

###initialize paddles and ball
player = paddle(0)
enemy = paddle(SIZE[0] - 10)
data_saver = results()
mainBall = ball(600)
font = pygame.font.Font('freesansbold.ttf', 64)
###INITIALIZE FIRST ROW OF DATAFRAME
df.loc[0] = [mainBall.x, mainBall.y, mainBall.vX, mainBall.vY, 392, 0]





while run:

    # deltaTime
    now = time.time()
    delta = now - last
    last = now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # make the screen black
    screen.fill((0, 0, 0))

    # draw the middle line
    dash = SIZE[1] / 32
    middle = int(SIZE[0] / 2)
    for i in range(0, 32):
        pygame.draw.line(screen, (255, 255, 255), (middle, int(dash * i + dash * 0.25)),
                         (middle, int(dash * i + dash * .75)), 4)

    # draw the ball
    mainBall.draw()
    # set the player's paddle to the mouse y position
    player.y = pygame.mouse.get_pos()[1]

    enemy.y=mainBall.y-enemy.h/2;

    # draw the paddles
    player.draw()
    enemy.draw()

    ### record data to dataframe
    data_saver.record(mainBall,player)


    ###display score
    ScoreText = font.render(str(scorePlayer), True, (255, 255, 255))
    screen.blit(ScoreText, (middle - 60, 32))
    ScoreText = font.render(str(scoreEnemy), True, (255, 255, 255))
    screen.blit(ScoreText, (middle + 28, 32))

    pygame.display.flip()
    pygame.display.update()

### drop rows that contain data from when you first start the game and right before you click "x"
df.drop(df.head(50).index,
        inplace = True)
df.drop(df.tail(50).index,
        inplace = True)
##save dataframe to csv file
df.to_csv('data.csv', index=False)

pygame.quit()
print(0)