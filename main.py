import random

import pygame
from pygame.locals import *
import time

SIZE = 18


class Insect:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.cricket = pygame.image.load('frog.png').convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        # self.parent_screen.fill((0, 0, 0))

        self.parent_screen.blit(self.cricket, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 53) * SIZE
        self.y = random.randint(0, 27) * SIZE
        self.draw()


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("cube.png").convert()
        self.length = length

        self.x = [SIZE] * length
        self.y = [SIZE] * length

        self.direction = 'right'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((0, 0, 0))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.insect = Insect(self.surface)
        self.insect.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 <= x2 + SIZE:
            if y2 <= y1 <= y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.insect.draw()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.insect.x, self.insect.y):
            # print("collusion")
            self.insect.move()
            self.snake.increase_length()
        self.display_score()
        pygame.display.flip()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print("game over")
            

    def display_score(self):
        font = pygame.font.SysFont('bodoni', 20)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (900, 8))

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
