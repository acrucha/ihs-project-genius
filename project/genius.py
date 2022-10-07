import random
import time
import pygame
from pygame.locals import *

N_ROUNDS = 10 # Jogo terá 10 rodadas
N_INIT_SEQ = 4 # Inicialmente, a sequência tem 4 itens
SLEEP = 0.3 # Tempo para a pŕoxima cor (depende dos switches)

BRIGHT_GREEN = (0, 255, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_YELLOW = (255, 255, 0)

GREEN = (0, 100, 0)
RED = (139, 0, 0)
BLUE = (18, 10, 143)
YELLOW = (255, 191, 0)

# TODO : PARAMETRIZAR ESSES VALORES, CENTRALIZAR NA TELA
red_triangle = ((81, 315), (230, 315), (230, 169))
green_triangle = ((412, 315), (263, 315), (263, 169))
yellow_triangle = ((412, 345), (263, 346), (263, 495))
blue_triangle = ((81, 345), (230, 346), (230, 495))

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((800, 800), RESIZABLE)
pygame.display.set_caption("Genius")

def show_init_screen():
    '''
        Exibe a tela inicial: 4 triângulos (luzes) "apagados"
    '''
    pygame.draw.polygon(screen, RED,  red_triangle)
    pygame.draw.polygon(screen, GREEN, green_triangle)
    pygame.draw.polygon(screen, YELLOW, yellow_triangle)
    pygame.draw.polygon(screen, BLUE, blue_triangle)


def choose_random_color():
    '''
        Escolhe uma das 4 cores aleatoriamente
    '''
    red_light = {'color': BRIGHT_RED, 'pos': red_triangle}
    green_light = {'color': BRIGHT_GREEN, 'pos': green_triangle}
    yellow_light = {'color': BRIGHT_YELLOW, 'pos': yellow_triangle}
    blue_light = {'color': BRIGHT_BLUE, 'pos': blue_triangle}

    colors = [green_light, yellow_light, blue_light, red_light]

    return random.choice(colors)

def show_color_sequence(sequence, sleep_time):
    '''
        Exibe a sequência de cores => "pisca" cada um dos triângulos da sequência
    '''
    for color in sequence:
        pygame.draw.polygon(screen, color['color'], color['pos']) # "Acende" triângulo da cor da vez
        pygame.display.update()
        time.sleep(sleep_time) 

        show_init_screen() # "Apaga" o triângulo que acendeu
        pygame.display.update()
        time.sleep(sleep_time) 


def game():
    color_sequence = [] # Lista com a sequência de cores

    # Insere as 4 primeiras cores aleatórias da sequência
    for i in range (0,N_INIT_SEQ):
        color_sequence.append(choose_random_color())

    # Exibe as 10 rodadas
    for i in range (0, N_ROUNDS):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        show_init_screen()

        # Gera uma cor aleatória e adiciona à sequência
        color_sequence.append(choose_random_color())

        # Exibe sequência na tela
        show_color_sequence(color_sequence, SLEEP)

        pygame.display.update()


if __name__ == '__main__':
    game()

