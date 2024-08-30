
WIDTH, HEIGHT = 700, 700
CELL_SIZE = 30
PADDING = 8
nrows = HEIGHT // CELL_SIZE
ncols = WIDTH // CELL_SIZE  
nempty = nrows//2
MAX_moves = 600

def set_initial_val(width, height, max_moves, cell_size=30, padding=8):
    global WIDTH,HEIGHT,CELL_SIZE,PADDING,nrows,ncols,nempty, MAX_moves
    WIDTH, HEIGHT = width, height
    CELL_SIZE = cell_size
    PADDING = padding 
    nrows = height // cell_size
    ncols = width // cell_size 
    nempty = nrows//2
    MAX_moves = max_moves



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
OLIVE = (128, 128, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
FPS = 30