### same game interface as trainData.py, the only difference is that we're using the computer class instead of training it
import pygame
import time
import random
from trainBot import computer
pygame.init()

SIZE = (1200, 800)
screen = pygame.display.set_mode(SIZE)

run = True

now = 0
last = time.time()
delta = 0

scorePlayer = 0
scoreEnemy = 0

paddles = []


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

        for p in paddles:
            if (self.y > p.y and self.y < p.y + p.h):

                if (self.x + self.radius > p.x and self.x - self.radius < p.x + p.w):

                    self.vX = -self.vX
                    self.vY+=random.randint(-100, 100) / 100.0 * self.speed
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


###YOU'RE ON THE RIGHT
enemy = paddle(0)
player = paddle(SIZE[0] - 10)
mainBall = ball(600)
enemyBrain=computer()




frameMod=0
sum=0
font = pygame.font.Font('freesansbold.ttf', 64)
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

    #given current ball position, predict position of your bot
    enemyData = [[mainBall.x, mainBall.y, mainBall.vX, mainBall.vY]]
    move= enemyBrain.move(enemyData)-enemy.h/2
    #have bot update itself every 10 frame, averaging the predicted movements
    if(frameMod==5):
        enemy.y=(sum)/5
        frameMod=0
        sum=0
    else:
        frameMod=frameMod+1
        sum=sum+move



    # draw the paddles
    player.draw()
    enemy.draw()

    # keep score between you and the bot
    ScoreText = font.render(str(scorePlayer), True, (255, 255, 255))
    screen.blit(ScoreText, (middle - 60, 32))
    ScoreText = font.render(str(scoreEnemy), True, (255, 255, 255))
    screen.blit(ScoreText, (middle+28, 32))


    pygame.display.flip()
    pygame.display.update()



pygame.quit()
print(0)