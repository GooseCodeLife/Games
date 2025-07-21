import pygame 
import pygame as pg 
import csv
import time 
pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480+140

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define tile size
TILE_SIZE = 32
px = 5 * TILE_SIZE
py = 14* TILE_SIZE+16

# loading images
Mstand1 = pygame.image.load('FinalMStanding.png').convert_alpha() 
Mstand2 = pygame.image.load('FinalMStanding2.png').convert_alpha() 
runningImg = pygame.image.load('running1.png').convert_alpha()
sky = pygame.image.load('sky1.png').convert_alpha()
tileset_image = pygame.image.load('tiles_grass.png').convert_alpha()
toad = pg.image.load('Toad.png').convert_alpha()
Pstand2 = pg.image.load('BiggerMStanding2.png').convert_alpha()
Pstand1 = pg.image.load('BiggerMStanding1.png').convert_alpha()
#rects 
Mstand1_rect = Mstand1.get_frect(center = (px, py ) )
Mstand2_rect = runningImg.get_frect(center = (px,py))
toad_rect = toad.get_frect(center = (5*TILE_SIZE+40,14*TILE_SIZE+18))
Pstand1_rect = Pstand1.get_frect(center = (px,py))
Pstand2_rect = Pstand2.get_frect(center = (px,py))













#////////////////////////////////////////////////////TILES///////////////////////////////////////
# Get the width and height of the tileset image
tileset_width, tileset_height = tileset_image.get_size()

# Calculate the number of tiles horizontally and vertically
tileset_columns = tileset_width // TILE_SIZE
tileset_rows = tileset_height // TILE_SIZE

# Create a list to hold individual tile images
tiles = []

for row in range(tileset_rows):
    for col in range(tileset_columns):
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        tile = tileset_image.subsurface((x, y, TILE_SIZE, TILE_SIZE))
        tiles.append(tile)

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        map_data = [list(map(int, row)) for row in reader]
    return map_data

def draw_map(map_data, tiles):
    for row_index, row in enumerate(map_data):
        for col_index, tile_index in enumerate(row):
            if tile_index >= 0:
                tile = tiles[tile_index]
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                screen.blit(tile, (x, y))

map_data = read_csv('map.csv')
#////////////////////////////////////////////////////TILES///////////////////////////////////////
