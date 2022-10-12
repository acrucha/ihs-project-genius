from curses import KEY_ENTER
from gzip import WRITE
import pygame
import time
import random
from PIL import Image, ImageDraw
from pygame.locals import *
from Utils import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Genius")

        self.font = pygame.font.Font('freesansbold.ttf', 36)
        self.screen = pygame.display.set_mode((600,600))
        
        self.state = INITIAL_SCREEN

        self.fsm()
    
    def fsm(self):
        while True:
            if self.state == INITIAL_SCREEN:    
                self.start_screen()
            elif self.state == GAME_ON:
                self.game_on()
            elif self.state == GAME_OVER:
                self.game_over()
            elif self.state == WINNER:
                self.winner_screen()

    def start_screen(self):
        messages = ['WELCOME TO GENIUS', 
                    'press SPACE to START', 
                    'press ESC to LEAVE',
                    'use your keyboard to play:']
            
        colors = [[BLACK, BRIGHT_YELLOW], 
                    [WHITE, BLUE], 
                    [WHITE, RED], 
                    [BLACK, GREEN]]

        pos = [(300, 120), (300, 180), (300, 220), (300, 270)]

        self.render_screen(messages, colors, pos)   

        img = pygame.image.load("WESD.jpeg").convert()
        self.screen.blit(img, (170, 300))
        pygame.display.flip()
            
        while self.state == INITIAL_SCREEN:
            for event in pygame.event.get():
                pygame.display.update()

                self.check_quit(event)
                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.state = GAME_ON

    def show_sequence(self, sequence):
        next = self.next_color()
        sequence.append(next)
        for tela in sequence:
            self.create(tela)
            self.create(begin)
    
    def next_color(self):
        colors = [red_on, green_on, yellow_on, blue_on]
        return random.choice(colors)

    def check_sequence(self, sequence):
        i = 0
        while True:
            if i >= len(sequence):
                break

            event = pygame.event.wait()
            
            self.check_quit(event)
            
            if event.type == KEYDOWN:
                if event.key != key[sequence[i]]:
                    return False # se a tecla apertada não corresponde à cor, retorna falso
                else:
                    i += 1
                    self.show_input(event.key)
                    pygame.event.clear()

        return True

    def check_quit(self ,event):
        if (event.type ==  QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            quit()

        
    def game_on(self):
        sequence = []
        
        while self.state == GAME_ON:
            self.create(begin)
            
            self.show_sequence(sequence)

            pygame.event.clear()

            check = self.check_sequence(sequence)

            if not check:
                self.state = GAME_OVER

            seq_size = len(sequence)
            
            if seq_size == N_ROUNDS:
                self.state = WINNER
    
    def render_screen(self, message, colors, pos):
        self.screen.fill(WRITE)
        
        for i in range(0, len(message)):
            text = self.font.render(message[i], True, colors[i][0], colors[i][1])
            text_rect = text.get_rect()
            text_rect.center = pos[i]
            self.screen.blit(text, text_rect)
        
        pygame.display.flip()

    def game_over(self):
        message = ['GAME OVER!!!', 'press SPACE to GO TO MENU', 'press ENTER to TRY AGAIN']
        colors = [[WHITE, BRIGHT_RED], [WHITE, BLUE], [WHITE, GREEN]]
        pos = [(300, 120), (300, 180), (300, 220)]
        
        self.render_screen(message, colors, pos)

        while self.state == GAME_OVER:
            pygame.display.update()
            for event in pygame.event.get():
                self.check_quit(event)
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.state = INITIAL_SCREEN
                    elif event.key == K_RETURN:
                        self.state = GAME_ON

    def winner_screen(self):
        message = ['WINNER!!!', 'press SPACE to PLAY AGAIN']
        colors = [[WHITE, GREEN], [WHITE, BLUE]]
        pos = [(300, 120),(300, 180)]

        self.render_screen(message, colors, pos)
        
        pygame.display.flip()

        while self.state == WINNER:
            pygame.display.update()
            for event in pygame.event.get():
                self.check_quit(event)
                time.sleep(SLEEP)
                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.state = INITIAL_SCREEN
                    
    def create(self, pattern):
        image = Image.new("RGBA", (620,620), "#000")
        draw = ImageDraw.Draw(image, image.mode)

        draw.pieslice((20, 20 , 600, 600), 180, 270, fill=pattern[0])
        draw.pieslice((50, 20 , 600, 600), 270, 360, fill=pattern[1])
        draw.pieslice((50, 50 , 600, 600), 0, 90, fill=pattern[2])
        draw.pieslice((20, 50 , 600, 600), 90, 180, fill=pattern[3])
        del draw

        mode = image.mode
        size = image.size
        data = image.tobytes()
        image = pygame.image.fromstring(data, size, mode)
        image_rect = image.get_rect(center=self.screen.get_rect().center)

        self.screen.fill(BLACK)
        self.screen.blit(image, image_rect)
        pygame.display.flip()

        time.sleep(SLEEP)

    def show_input(self, evento):
        choice = begin
        # Aqui depois dá pra usar o dicionario de key
        
        if(evento==K_w):
            choice = red_on
        elif(evento==K_e):
            choice = green_on
        elif(evento==K_d):
            choice = yellow_on
        elif(evento==K_s):
            choice = blue_on

        self.create(choice)
        self.create(begin)

if __name__ == "__main__":
    Game()