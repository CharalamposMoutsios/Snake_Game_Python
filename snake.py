import pygame
import random

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 50]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
        
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, white, element, self.radius)
            
    def move(self):
        for i in range(len(self.elements) - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
            
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        
        if self.elements[0][0] < 0 or self.elements[0][0] > width - 10 or self.elements[0][1] < 0 or self.elements[0][1] > height - 10:
            raise Exception('Game over')

class Food:
    def __init__(self):
        self.position = [random.randrange(0, width - 10, 10), random.randrange(0, height - 10, 10)]
        self.radius = 5
        
    def draw(self):
        pygame.draw.circle(screen, red, self.position, self.radius)

def game():
    snake = Snake()
    food = Food()
    
    while True:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.dx = -5
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake.dx = 5
                    snake.dy = 0
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -5
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 5

        try:
            snake.move()
        except Exception as e:
            print(e)
            return False

        snake.draw()
        food.draw()

        if abs(snake.elements[0][0] - food.position[0]) < 15 and abs(snake.elements[0][1] - food.position[1]) < 15:
            snake.size += 1
            snake.elements.append([0, 0])
            food.position = [random.randrange(0, width - 10, 10), random.randrange(0, height - 10, 10)]

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

while True:
    if not game():
        font = pygame.font.SysFont(None, 40)
        text = font.render('Game over! Play again? (Y/N)', True, white)
        text_rect = text.get_rect(center=(width/2, height/2))
        screen.blit(text, text_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame
