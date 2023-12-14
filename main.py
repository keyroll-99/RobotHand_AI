import pygame

from Robot.Robot import Robot

pygame.init()

white = (255, 255, 255)

screen = pygame.display.set_mode((600., 400))
pygame.display.set_caption("Robot Hand")

running = True

robot = Robot(screen)
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            angle += 1
    robot.rotate_upper_hand(angle)

    screen.fill(white)
    robot.draw()

    pygame.display.update()
