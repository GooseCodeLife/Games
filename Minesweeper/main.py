from settings2 import * 

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            for b in buttons : 
                b.is_hit(pos)
                
    screen.fill((0, 0, 0))  # Clear the screen

    for b in buttons : 
        b.draw()


    pg.display.flip()

pg.quit 