from pygame.locals import *
import pygame

N_ROUNDS = 2 # Jogo terá 10 rodadas
N_INIT_SEQ = 4 # Inicialmente, a sequência tem 4 itens
SLEEP = 0.3 # Tempo para a pŕoxima cor (depende dos switches)

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

#telas
begin = (RED, GREEN, YELLOW, BLUE)
red_on = (BRIGHT_RED, GREEN, YELLOW, BLUE)
green_on = (RED, BRIGHT_GREEN, YELLOW, BLUE)
yellow_on = (RED, GREEN, BRIGHT_YELLOW, BLUE)
blue_on = (RED, GREEN, YELLOW, BRIGHT_BLUE)
all_on = (BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE)

# Associa a cor da sequencia a um evento de teclado

key = {
    red_on : K_w,
    green_on : K_e,
    yellow_on : K_d,
    blue_on : K_s
}

INITIAL_SCREEN, GAME_ON, GAME_OVER, WINNER = [i for i in range(0,4)]
