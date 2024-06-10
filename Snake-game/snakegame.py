import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption('Snake')
pygame.font.init()
random.speed()

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 25
KEY = {"UP":1 , "DOWN":2 , "LEFT":3, "RIGHT":4}

#we will initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.HWSURFACE)
#we have used hw surface which stands for hardware refers to using memory on the video card for storing
#draws as opposed to main memory

#Resources

score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0) # we will fill bg-color as black
black = pygame.Color(0,0,0)

#for click at the left corner
gameClock = pygame.time.Clock()

#to check the boundarie. here we are not limiting boundaries like it can pass through like it can pass through screen and come from other

def checkCollision(posA,As,posB,Bs):
    if(posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x =SNAKE_SIZE
    if(snake.x <0):
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y =SNAKE_SIZE
    if(snake.y <0): #also same half half
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE

#we will make class for food of  the snake let's name it as apple

class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("orange")

    def draw(self,screen:
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)

def getKey(event):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            #for exit
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            elif event.key == pygame.K_y:
                return "yes"
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit()

def endGame():
    message = game_over_font.render("GAME OVER",1,pygame.Color("black"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

pygame.display.flip()
pygame.display.update()

mKey = getKey()
while (mKey != "exit"):
    if(mKey == "yes"):
        main()
    elif(mKey == "no"):
        break
    mKey = getKey()
    gameClock.tick(FPS)
sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg,(SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb,(SCREEN_WIDTH -45,14))

def drawGameTime(gameTime):
    game_time = score_font.render("Time:" , 1, pygame.Color("white"))
def main():
    print("bvhfbvhfbf")