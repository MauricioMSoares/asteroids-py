import pygame, sys, os, random, math
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# globals
WIDTH = 800
HEIGHT = 600
time = 0

# canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Asteroids")

# load images
bg = pygame.image.load(os.path.join("images", "bg.jpg"))
debris = pygame.image.load(os.path.join("images", "debris2_brown.png"))
ship = pygame.image.load(os.path.join("images", "ship.png"))

ship_x = WIDTH / 2 - 50
ship_y = HEIGHT / 2 - 50
ship_angle = 0
ship_is_rotating = False
ship_direction = 0


def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def draw(canvas):
    global time
    canvas.fill(BLACK)
    canvas.blit(bg, (0, 0))
    canvas.blit(debris, (time * 0.3, 0))
    canvas.blit(debris, (time * 0.3 - WIDTH, 0))
    time += 1
    canvas.blit(rot_center(ship, ship_angle), (ship_x, ship_y))


def handle_input():
    global ship_angle, ship_is_rotating, ship_direction

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                ship_is_rotating = True
                ship_direction = 0
            elif event.key == K_RIGHT:
                ship_is_rotating = True
                ship_direction = 1
        elif event.type == KEYUP:
            ship_is_rotating = False

    if ship_is_rotating:
        if ship_direction == 0:
            ship_angle += 10
        else:
            ship_angle -= 10


def update_screen():
    pygame.display.update()
    fps.tick(60)


# asteroids game loop
while True:
    draw(window)
    handle_input()
    # game_logic()
    update_screen()
