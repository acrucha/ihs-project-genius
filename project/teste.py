import pygame
import time
import random
from PIL import Image, ImageDraw
from pygame.locals import *

# --- constants ---
N_ROUNDS = 10 # Jogo terá 10 rodadas
N_INIT_SEQ = 4 # Inicialmente, a sequência tem 4 itens
SLEEP = 0.6 # Tempo para a pŕoxima cor (depende dos switches)
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

# Inicializando Pygame
pygame.init()
screen = pygame.display.set_mode((600,600), RESIZABLE)
pygame.display.set_caption("Genius")

def create(pattern):
    # - generate PIL image with black background -
    image = Image.new("RGBA", (600, 600), "#000")
    draw = ImageDraw.Draw(image, image.mode)
    draw.pieslice((50, 50 , 512, 512), 180, 270, fill=pattern[0])
    draw.pieslice((80, 50 , 512, 512), 270, 360, fill=pattern[1])
    draw.pieslice((80, 80 , 512, 512), 360, 450, fill=pattern[2])
    draw.pieslice((50, 80 , 512, 512), 450, 540, fill=pattern[3])
    del draw
    # - convert into PyGame image -
    mode = image.mode
    size = image.size
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    image_rect = image.get_rect(center=screen.get_rect().center)
    return image, image_rect

def next_color():
    colors = [red_on, green_on, yellow_on, blue_on]
    return random.choice(colors)

def show_screen(tela):
    image, image_rect = create(tela)
    screen.fill(BLACK)
    screen.blit(image, image_rect) # <- display image
    pygame.display.flip()
    time.sleep(SLEEP)

def show_sequence(sequence):
    next = next_color()
    sequence.append(next)
    for tela in sequence:
        show_screen(tela)
        show_screen(begin)

def show_input(evento):
    choice = begin
    if(evento==K_w):
        choice = red_on
    elif(evento==K_e):
        choice = green_on
    elif(evento==K_d):
        choice = yellow_on
    elif(evento==K_s):
        choice = blue_on
    show_screen(choice)
    show_screen(begin)

# - mainloop -
running = True
sequence = []
while running:

    #exibe a tela de inicio
    image, image_rect = create(begin)
    screen.fill(BLACK)
    screen.blit(image, image_rect) # <- display image
    pygame.display.flip()
    time.sleep(SLEEP)

    show_sequence(sequence)
    seq_size = len(sequence)
    print(seq_size)
    i=0

    pygame.event.clear()
    ok = True
    while ok:
        if(i>=len(sequence)):
            ok = False
            break
        event = pygame.event.wait()
        if event.type == QUIT:
            running = False
            ok = False
        elif event.type == KEYDOWN:
            if ((event.key == K_w) and(sequence[i] != red_on)):
                running = False
                ok = False
            elif ((event.key == K_e) and(sequence[i] != green_on)):
                running = False
                ok = False
            elif ((event.key == K_d) and(sequence[i] != yellow_on)):
                running = False
                ok = False
            elif ((event.key == K_s) and(sequence[i] != blue_on)):
                running = False
                ok = False
            elif (event.key == K_ESCAPE):
                    running = False
                    ok = False
            else:
                i += 1
                show_input(event.key)
                pygame.event.clear()


# - end -
pygame.quit()