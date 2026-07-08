import pygame

pygame.init()


screen=pygame.display.set_mode((900,700))

pygame.display.set_caption("Tic Tac Toe")

font =pygame.font.Font(None,60)

WHITE=(255,255,255)

board=["","","","","","","","",""]
winner=""
current_player="X"
game_over=False
draw=False
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
            if game_over==False:
            
               mouse_pos=event.pos
               x,y=mouse_pos
               if 225<=x<=675 and 125<y<=575:

                  row=(y-125)//150
                  col=(x-225)//150

                  index=row*3+col

                  if board[index]=="":
                    board[index]=current_player

                    if(current_player=="X"):
                        current_player="O"

                    else:
                        current_player="X"
                
               
               if( board[0]!=""   and board[0]==board[1] ==board[2]):
                        winner=board[0]
                        game_over=True

               if(board[0]!=""  and board[0]==board[3] ==board[6]):
                        winner=board[0]
                        game_over=True


               if(board[3]!=""  and board[3]==board[4] ==board[5]):
                        winner=board[3]
                        game_over=True

               if(board[6]!="" and board[6]==board[7] ==board[8]):
                        winner=board[6]
                        game_over=True


               if(board[1]!="" and board[1]==board[4] ==board[7]):
                        winner=board[1]
                        game_over=True


               if(board[2]!="" and  board[2]==board[5] ==board[8]):
                        winner=board[2]
                        game_over=True

               if(board[0]!="" and  board[0]==board[4] ==board[8]):
                        winner=board[0]
                        game_over=True


               if(board[2]!="" and   board[2]==board[4] ==board[6]):
                        winner=board[2]
                        game_over=True

   
    if winner=="" :
          if "" not in board:
                draw=True
                game_over=True

                text=font.render("sorry next time!",True,(255,0,0))

                screen.blit(text,(300,50))
                 
                
        

    if winner!="" and  game_over:
        text=font.render(winner+" "+   "WINS!",True,(255,0,0))

        screen.blit(text,(300,50))

    

                

    pygame.display.update()

pygame.quit()
