#!/usr/bin/python3

import pygame
from random import randint

from Util.Constants import *
from Util.GameState import GameState
from Util.Windows import IntroScreen, OutroScreen

from TetrisGrid.Grid import Grid
from TetrisGrid.Wall import Wall
from TetrisGrid.Floor import Floor
from TetrisPiece.Shape import Shape

from TetrisPiece.Obstacles import Obstacles
from TetrisPiece.MovePiece import MovePiece

class TetrisGame:
    def __init__(self):
        self.grid = Grid()
        self.floor = Floor(LEFT, ROWS, COLUMNS)
        self.left_wall = Wall(LEFT - 1, 0, ROWS)
        self.right_wall = Wall(RIGHT, 0, ROWS)
        
        self.game_state = GameState()
        self.shape_no = randint(1, 7)
        
        self.game_state.shape = Shape(MIDDLE, TOP, self.shape_no)
        self.obstacles = Obstacles(LEFT, FLOOR, 0)
        
        self.intro_screen = IntroScreen(screen, intro_screen)
        self.outro_screen = OutroScreen(screen, outro_screen)
        
        self.in_play = False
        self.has_played = False

    def process_key_events(self, event):
        """Handle keyboard events for controlling the game pieces"""
        # Retrieve current shape and the number of the next shape
        shape = self.game_state.shape
        next_shape_no = self.game_state.nextShapeNo

        # Rotate, move left/right, and drop the piece based on key press
        if event.key == pygame.K_UP:
            MovePiece.rotate_piece_clockwise(shape, self.left_wall, self.right_wall, self.floor, self.obstacles, block_rotate)
        elif event.key == pygame.K_LEFT:
            MovePiece.move_piece_left(shape, self.left_wall, self.obstacles)
        elif event.key == pygame.K_RIGHT:
            MovePiece.move_piece_right(shape, self.right_wall, self.obstacles)
        elif event.key == pygame.K_DOWN:
            MovePiece.drop_piece(shape, self.floor, self.obstacles, next_shape_no)
        elif event.key == pygame.K_SPACE:
            self.game_state.drop_instant_piece(self.obstacles, self.floor, line_remove, tetris_remove)


    def update_game_state(self, counter):
        """Update the game state based on the game loop counter"""
        # Create a shadow of the current shape for visual aid
        shadow = Shape(self.game_state.shape.col, self.game_state.shape.row, self.game_state.shape.clr, self.game_state.shape._rot, True)
        # Continuously drop the shadow shape
        MovePiece.drop(shadow, self.floor, self.obstacles, slow_hit)

        # Handle the movement of the active shape based on the game counter
        if counter % LEVELS[self.game_state.level] == 0:
            # Move the shape down by one row
            self.game_state.shape.move_down()
            # Check for collision with the floor or other shapes
            if self.game_state.shape.collides(self.floor) or self.game_state.shape.collides(self.obstacles):
                # Move the shape back up and add it to the list of obstacles
                self.game_state.shape.move_up()
                self.obstacles.append(self.game_state.shape)
                # Play sound effect for shape placement
                pygame.mixer.Channel(5).play(slow_hit)
                # Update the game score and handle line removals
                self.game_state.update_score_and_sound_effects(self.obstacles, line_remove, tetris_remove)
                # Spawn a new shape and check if the game should continue
                shape_no = self.game_state.nextShapeNo
                self.game_state.nextShapeNo = randint(1, 7)
                if self.game_state.shape.row > 1:
                    self.game_state.shape = Shape(MIDDLE, TOP, shape_no)
                else:
                    self.game_state.inPlay = False

        # Update the game level and reset Tetris combo flag
        self.game_state.level = self.game_state.update_level()
        self.game_state.prevTetris = False
        return shadow

    def handle_event(self, event):
        """Handle different types of events"""
        if event.type == pygame.QUIT:
            self.game_state.inPlay = False
        elif event.type == pygame.KEYDOWN:
            self.process_key_events(event)

    def main_game_loop(self):
        state = 0
        while self.game_state.inPlay:
            # Update the game state
            shadow = self.update_game_state(state)
            # Handle all events in the event queue
            for event in pygame.event.get():
                self.handle_event(event)
            state += 1
            # Redraw the screen with updated game elements
            self.grid.redraw_screen(screen,
                                    grid_img, tetris_img, 
                                    self.game_state.shape, shadow, self.obstacles, block_img,
                                    self.game_state.nextShapeNo, self.game_state.score, self.game_state.level,
                                    font)
        return self.game_state 


    def run(self):
        while True:
            if not self.in_play:
                pygame.display.set_caption("Pixel Tetris Horizon")
                self.intro_screen.run()
                self.in_play = self.intro_screen.inPlay
                self.has_played = self.intro_screen.hasPlayed

            if self.in_play:
                pygame.display.set_caption("!AMADEUS WAS HERE!")
                self.game_state = self.main_game_loop()
                self.in_play = self.game_state.inPlay

            if not self.in_play and self.has_played:
                pygame.display.set_caption("!GAME OVER!")
                self.outro_screen.run()
                self.in_play = self.outro_screen.inPlay
                self.has_played = self.outro_screen.hasPlayed

            if not self.in_play and not self.has_played:
                break  # Exit the game

if __name__ == "__main__":
    tetris_game = TetrisGame()
    tetris_game.run()
    pygame.quit()
