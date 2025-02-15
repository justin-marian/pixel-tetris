import pygame
import platform
from random import choice

# Get the current operating system
system_os = platform.system()

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(6)

# Constants for the game grid
TOP = 1
ROWS = 24
COLUMNS = 14
FLOOR = TOP + ROWS

# Screen dimensions
WIDTH = 575
HEIGHT = 600
GRIDSIZE = HEIGHT // ROWS
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initial game level, score, and a list of levels
SCORE = 0
LEVELS = [300, 250, 200, 175, 150, 125, 112, 100, 90]

# Constants for grid positions
LEFT = 0
RIGHT = LEFT + COLUMNS
MIDDLE = (LEFT + COLUMNS) // 2

# Define colors
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
AGRAY = (200, 200, 200, 75)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ORANGE = (255, 127, 0)
CYAN = (0, 183, 235)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

COLOURS = [BLACK, RED, GREEN, BLUE, ORANGE, CYAN, MAGENTA, YELLOW]

# Names corresponding to Tetris pieces
figures = [None, 'Z', 'S', 'J', 'L', 'I', 'T', 'O', None]

# Initialize Pygame fonts
pygame.font.init()

# Set the font for the game depending on the operating system
if system_os == "Windows":
    font = pygame.font.SysFont('Algerian', 28)
else:
    font = pygame.font.SysFont('Algerian', 42)

# Function to load images and sounds
def load_images(files):
    return [pygame.image.load(file).convert_alpha() for file in files]

def load_sounds(files):
    return [pygame.mixer.Sound(file) for file in files]

# Background music
music_files = ['../Music/Rondo_Alla_Turka.ogg',
                '../Music/Lacrimosa.ogg', 
                '../Music/Allegro.ogg']
music = choice(load_sounds(music_files))
pygame.mixer.Channel(0).play(music, -1)

# Load game images
tetris_img, grid_img, \
intro_screen, outro_screen, \
icon = load_images([
    '../Image/Tetris.jpg',
    '../Image/Grid.png',
    '../Image/Intro.png',
    '../Image/Outro.png',
    '../Image/Icon.png'
])
pygame.display.set_icon(icon)

# Load game sounds
block_rotate, force_hit, \
line_remove, slow_hit, \
tetris_remove = load_sounds([
    '../Sound/block-rotate.ogg',
    '../Sound/Force-Hit-Line.ogg',
    '../Sound/Remove-Line.ogg',
    '../Sound/Slow-Hit-Line.ogg',
    '../Sound/Amadeus-Laughing.ogg'
])

# Load block images for Tetris pieces
block_img = load_images([
    '../View/Z.png',
    '../View/S.png',
    '../View/L.png', 
    '../View/J.png',
    '../View/I.png',
    '../View/T.png',
    '../View/CUBE.png'])
