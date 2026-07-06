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
            
            if 225<=x<=375  and 125<=y<=275:
                    if current_player=="X":
                         board[0]="X"
                         current_player="O"
                    else:
                         board[0]="O"
                         current_player="X"
            

            if 375<=x<=525  and 125<=y<=275:
                 if current_player=="X":
                      board[1]="X"
                      current_player="O"

                 else:
                      board[1]="O"
                      current_player="X"

            if 525<=x<=675 and 125<=y<=275:
                 if current_player=="X":
                      board[2]="X"
                      current_player="O"

                 else:
                      board[2]="O"
                      current_player="X"


            
            if 225<=x<=375 and 275<=y<=425:
                 if current_player=="X":
                      board[3]="X"
                      current_player="O"

                 else:
                      board[3]="O"
                      current_player="X"


            
            if 375<=x<=525 and 275<=y<=425:
                 if current_player=="X":
                      board[4]="X"
                      current_player="O"

                 else:
                      board[4]="O"
                      current_player="X"



            
            if 525<=x<=675 and 275<=y<=425:
                 if current_player=="X":
                      board[5]="X"
                      current_player="O"

                 else:
                      board[5]="O"
                      current_player="X"


            
            if 225<=x<=375 and 425<=y<=575:
                 if current_player=="X":
                      board[6]="X"
                      current_player="O"

                 else:
                      board[6]="O"
                      current_player="X"

            
            if 375<=x<=525 and 425<=y<=575:
                 if current_player=="X":
                      board[7]="X"
                      current_player="O"

                 else:
                      board[7]="O"
                      current_player="X"


            
            if 525<=x<=675 and 425<=y<=575:
                 if current_player=="X":
                      board[8]="X"
                      current_player="O"

                 else:
                      board[8]="O"
                      current_player="X"


            
          
                

                    

   
    
    


    

    
    pygame.display.update()

pygame.quit()
