import pygame

pygame.init()

screen=pygame.display.set_mode((900,700))

pygame.display.set_caption("Tic Tac Toe")

WHITE=(255,255,255)

board=["","","","","","","","",""]

running=True
while running:
    screen.fill(WHITE)

    pygame.draw.line(screen,(0,0,0),(225,125),(675,125),5)
    pygame.draw.line(screen,(0,0,0),(225,275),(675,275),5)
    pygame.draw.line(screen,(0,0,0),(225,425),(675,425),5)
    pygame.draw.line(screen,(0,0,0),(225,575),(675,575),5)
    

    pygame.draw.line(screen,(0,0,0),(225,125),(225,575),5)   
    pygame.draw.line(screen,(0,0,0),(375,125),(375,575),5)
    pygame.draw.line(screen,(0,0,0),(525,125),(525,575),5)
    pygame.draw.line(screen,(0,0,0),(675,125),(675,575),5)

    if(board[0]=="X"):
        pygame.draw.line(screen,(0,0,0) ,(245,145),(355,255),5)
        pygame.draw.line(screen,(0,0,0) ,(245,255),(355,145),5)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=event.pos
            x,y=mouse_pos

            if 225<=x<=375  and 125<=y<=275:
                    board[0]="X"

                    

   
    
    


    

    # pygame.draw.circle(screen,(255,0,0),(300,200),65,5)
    pygame.display.update()

pygame.quit()
