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
    
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=event.pos
            print(mouse_pos)

    pygame.draw.line(screen,(0,0,0),(225,125),(675,125),5)
    pygame.draw.line(screen,(0,0,0),(225,275),(675,275),5)
    pygame.draw.line(screen,(0,0,0),(225,425),(675,425),5)
    pygame.draw.line(screen,(0,0,0),(225,575),(675,575),5)
    
    pygame.draw.line(screen,(0,0,0),(225,125),(225,575),5)   
    pygame.draw.line(screen,(0,0,0),(375,125),(375,575),5)
    pygame.draw.line(screen,(0,0,0),(525,125),(525,575),5)
    pygame.draw.line(screen,(0,0,0),(675,125),(675,575),5)


    pygame.draw.line(screen,(0,0,0) ,(385,290),(510,410),5)
    pygame.draw.line(screen,(0,0,0) ,(385,410),(510,290),5)

    pygame.draw.circle(screen,(255,0,0),(300,200),65,5)
    pygame.display.update()

pygame.quit()
