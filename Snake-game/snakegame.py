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

    def endGame():
        message = game_over_font.render("GAME OVER",1,pygame.Color("black"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

