import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Уворачивайся от врагов")

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5

        if self.rect.left < 0:
            self.rect.x = 0
        if self.rect.right > WIDTH:
            self.rect.x = WIDTH
        if self.rect.top < 0:
            self.rect.y = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.speedx = random.choice([-3, 3])
        self.speedy = random.choice([-3, 3])

    def update(self):
        self.rect.x = self.speedx
        self.rect.y = self.speedy
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speedy *= -1

all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(10):
    ball = Ball()
    all_sprites.add(ball)
    balls.add(ball)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    if pygame.sprite.spritecollide(player, balls, False):
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
