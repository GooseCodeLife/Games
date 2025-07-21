import settings 
from settings import * 
start = True 
stand1 = True 
size =1.1

#class for Mario!!
class PlayerMario ():
    stand = True  
    global stand1
    def __init__ (self, run): 
        self.run = run 
        
    def stand_movement (self) :
            if stand1 == True :
                Mstand1_rect = Mstand1.get_frect(center = (px, py))
                Mstand1_rect= Mstand1_rect.inflate(50, 50)
                #pygame.Surface.blit(Mstand1, screen, Mstand1_rect)
                #screen.blit(Mstand1, Mstand1_rect)
                pg.display.update()
                clock.tick(15)
                screen.blit(Mstand2, Mstand1_rect)
                pg.display.update()
            if Mstand1_rect.colliderect(toad_rect) :
                stand = False 

    def stand_movement_real (self) :
        Pstand1_rect = Pstand1.get_frect(center=(px,py))
        screen.blit(Pstand1,Pstand1_rect )
        pg.display.update() 
        clock.tick(15)
        screen.blit()

#tile stuff //////////////////////////////////////////////////////////////////////////////////////////////////////
    def tiles_current_pos(self):
        x= px
        y= py 
        current_row = y// TILE_SIZE
        current_col = x // TILE_SIZE
        print (current_row , current_col)
        return  current_row , current_col

    def tiles_below_pos(self):
        current_row , current_col= self.tiles_current_pos()
        return  current_row+1 , current_col
        
    def tiles_below(self,mapData):
        row , col= self.tiles_below_pos()
        row_data = mapData[row]
        col_data = row_data[col]
        print("Tile Below is" , col_data)
        return col_data
    

    def tiles_at(self,mapData,left_right=0, top_below =0):
        row , col= self.tiles_current_pos()
        row_data = mapData[row+top_below]
        col_data = row_data[col+left_right]
        print("Tile tiles_at is" , left_right, top_below,col_data)
        return col_data
    
    def tiles_right(self,mapData):
        return self.tiles_at(mapData,1)
    
    def tiles_left(self,mapData):
        return self.tiles_at(mapData,-1)
    
    def tiles_up(self,mapData):
        return self.tiles_at(mapData,0,-1)
    
    
    def tiles_down(self,mapData):
        return self.tiles_at(mapData,0,1)
 #///////////////////////////   tile stuff /////////////////////////////////////
    
#create a player!
player1 = PlayerMario(0)
skyx = 0
# Main game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==  pg.KEYDOWN : 
            if event.key == pg.K_RIGHT:
                px = px + 3
            elif event.key == pg.K_LEFT: 
                px = px - 3
            else: 
                stand = True  
    if skyx < -1300: 
        skyx = 0 
    else: 
        skyx -= 0.08
    # Draw the map
    screen.fill((0, 0, 0))
    screen.blit(sky, (skyx,0))
    draw_map(map_data, tiles)
    screen.blit(toad,toad_rect)
    tiles_below = player1.tiles_below(map_data) 
    if start == True : 
        player1.stand_movement()

    
    pg.display.update()
    # Update the display
    #pygame.display.flip()
# Quit Pygame
pygame.quit()