import pygame

pygame.init()

screen=pygame.display.set_mode((900,700))

pygame.display.set_caption("Tic Tac Toe")

WHITE=(255,255,255)

board=["","","","","","","","",""]

current_player="X"
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
    

    for i in range(9):
         row=i//3
         col=i%3

         centre_x=300+col*150
         centre_y=200+row*150

         if(board[i]=="X"):
           pygame.draw.line(screen,(0,0,0) ,(centre_x-55,centre_y-55),(centre_x+55,centre_y+55),5)
           pygame.draw.line(screen,(0,0,0) ,(centre_x-55,centre_y+55),(centre_x+55,centre_y-55),5)

         elif board[i]=="O":
           pygame.draw.circle(screen,(255,0,0),(centre_x,centre_y),65,5)

         
    


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=event.pos
            x,y=mouse_pos

            row=(y-125)//150
            col=(x-225)//150

            index=row*3+col

            if board[index]=="":
                board[index]=current_player

                if(current_player=="X"):
                    current_player="O"

                else:
                    current_player="X"


            


            
            
            
          
                

                    

   
    
    


    

    
    pygame.display.update()

pygame.quit()
