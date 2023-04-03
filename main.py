import pygame


pygame.init()


width = 500
height = 500
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([width, height])
run = True

while run:
    timer.tick(fps)



pygame.quit()