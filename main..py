import pygame

pygame.init()

screen=pygame.display.set_mode((900,700))

pygame.display.set_caption("Tic Tac Toe")

WHITE=(255,255,255)


running=True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.update()

pygame.quit()
