from gzip import WRITE
import pygame
import time
import random
from PIL import Image, ImageDraw
from pygame.locals import *

# --- constants ---
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


key = {
    red_on : K_w,
    green_on : K_e,
    yellow_on : K_d,
    blue_on : K_s
}


def start_screen():
    font = pygame.font.Font('freesansbold.ttf', 42)
    font2 = pygame.font.Font('freesansbold.ttf', 34)
    text = font.render('WELCOME TO GENIUS', True, BLACK, BRIGHT_YELLOW)
    textRect = text.get_rect()
    textRect.center = (300, 120)
    text2 = font2.render('press SPACE to START', True, WHITE, BLUE)
    text2Rect = text2.get_rect()
    text2Rect.center = (300, 180)
    text3 = font2.render('press ESC to LEAVE', True, WHITE, RED)
    text3Rect = text3.get_rect()
    text3Rect.center = (300, 220)
    text4 = font2.render('use your keyboard to play:', True, BLACK, GREEN)
    text4Rect = text4.get_rect()
    text4Rect.center = (300, 270)
    img = pygame.image.load("WESD.jpeg").convert()
    pygame.display.flip()
    wait_user = True
    while wait_user:
        screen.fill(WRITE)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        screen.blit(text3, text3Rect)
        screen.blit(text4, text4Rect)
        screen.blit(img, (170, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
            if event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    pygame.quit()
                    quit()
                elif(event.key == K_SPACE):
                    wait_user = False
                    game()


def create(pattern):
    # - generate PIL image with black background -
    image = Image.new("RGBA", (620,620), "#000")
    draw = ImageDraw.Draw(image, image.mode)
    draw.pieslice((20, 20 , 600, 600), 180, 270, fill=pattern[0])
    draw.pieslice((50, 20 , 600, 600), 270, 360, fill=pattern[1])
    draw.pieslice((50, 50 , 600, 600), 0, 90, fill=pattern[2])
    draw.pieslice((20, 50 , 600, 600), 90, 180, fill=pattern[3])
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

def winner_screen():
    font = pygame.font.Font('freesansbold.ttf', 52)
    font2 = pygame.font.Font('freesansbold.ttf', 36)

    text = font.render('WINNER!!!', True, WHITE, GREEN)
    textRect = text.get_rect()
    textRect.center = (300, 120)

    text2 = font2.render('press SPACE to RESTART', True, WHITE, BLUE)
    text2Rect = text2.get_rect()
    text2Rect.center = (300, 180)

    pygame.display.flip()
    while True:
        pygame.display.update()
        screen.fill(WRITE)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    pygame.quit()
                    quit()
                elif(event.key == K_SPACE):
                    start_screen()

def game_over():
    font = pygame.font.Font('freesansbold.ttf', 52)
    font2 = pygame.font.Font('freesansbold.ttf', 36)

    text = font.render('GAME OVER!!!', True, WHITE, BRIGHT_RED)
    textRect = text.get_rect()
    textRect.center = (300, 120)

    text2 = font2.render('press SPACE to RESTART', True, WHITE, BLUE)
    text2Rect = text2.get_rect()
    text2Rect.center = (300, 180)

    pygame.display.flip()
    while True:
        pygame.display.update()
        screen.fill(WRITE)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    pygame.quit()
                    quit()
                elif(event.key == K_SPACE):
                    start_screen()


def get_level():
    # Colocar aqui a leitura dos switches para saber o nível
    # Atualizar o SLEEP
    return 1

def game():

    # - mainloop -
    running = True
    sequence = []
    score = 0
    while running:
        #exibe a tela de inicio
        image, image_rect = create(begin)
        screen.fill(BLACK)
        screen.blit(image, image_rect) # <- display image
        pygame.display.flip()
        time.sleep(SLEEP)
        
        level = get_level()

        seq_size = len(sequence)

        score += seq_size * level
        if seq_size == N_ROUNDS:
            winner_screen()
        
        show_sequence(sequence)
        i=0

        pygame.event.clear()
        ok = True

        # funcao dps
        while ok:
            if(i>=len(sequence)):
                ok = False
                break
            event = pygame.event.wait()
            if event.type == QUIT:
                running = False
                ok = False
            elif event.type == KEYDOWN:
                if event.key != key[sequence[i]]:
                    ok = False
                    running = False
                    game_over()
                elif (event.key == K_ESCAPE):
                        running = False
                        ok = False
                else:
                    i += 1
                    show_input(event.key)
                    pygame.event.clear()

    # - end -
    pygame.quit()

if __name__ == "__main__":
    # Inicializando Pygame
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Genius")
    start_screen()