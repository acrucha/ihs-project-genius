from pygame.locals import *
import pygame

N_ROUNDS = 10
INITIAL_SCREEN, CHOOSE_LEVEL, GAME_ON, GAME_OVER, WINNER = [i for i in range(0,5)]

BRIGHT_GREEN = (0, 255, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_YELLOW = (255, 255, 0)
GREEN = (0, 100, 0)
RED = (139, 0, 0)
BLUE = (18, 10, 143)
YELLOW = (180, 140, 0)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

begin = (RED, GREEN, YELLOW, BLUE)
red_on = (BRIGHT_RED, GREEN, YELLOW, BLUE)
green_on = (RED, BRIGHT_GREEN, YELLOW, BLUE)
yellow_on = (RED, GREEN, BRIGHT_YELLOW, BLUE)
blue_on = (RED, GREEN, YELLOW, BRIGHT_BLUE)
all_on = (BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE)

key_colors = {
    K_w : red_on,
    K_e : green_on,
    K_d : yellow_on,
    K_s : blue_on 
}

levels = {
    K_1 : 0.4,
    K_2 : 0.3,
    K_3 : 0.2
}

RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934