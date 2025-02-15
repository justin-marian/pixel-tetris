from typing import List 
from random import randint
from .Constants import *

from TetrisPiece.Shape import Shape
from TetrisPiece.MovePiece import MovePiece

class GameState:
    def __init__(self):
        """
        Initialize the game state.

        Attributes:
            shape (Shape): Current falling shape.
            nextShapeNo (int): Next shape's number.
            score (int): Player's score.
            prevTetris (bool): Flag to track previous Tetris completion.
            level (int): Current game level.
            inPlay (bool): Flag to check if the game is active.
        """
        self.shape = None
        self.nextShapeNo = 1
        self.score = 0
        self.prevTetris = False
        self.level = 0
        self.inPlay = True

    def update_level(self) -> int:
        """
        Update the current game level based on the player's score.

        Returns:
            int: The updated game level.
        """
        thresholds = [500, 1000, 1500, 2000, 2250, 2500, 2750, 3000, 3250]
        return next((i for i, threshold in enumerate(thresholds) if self.score < threshold), 9)

    def update_score_and_sound_effects(self, obstacles: List[Shape], line_remove: pygame.mixer.Sound, tetris_remove: pygame.mixer.Sound) -> None:
        """
        Update the player's score and play sound effects based on completed rows.

        Args:
            obstacles (List[Shape]): The list of obstacles (shapes) on the game board.
            line_remove (pygame.mixer.Sound): The sound effect for removing a single line.
            tetris_remove (pygame.mixer.Sound): The sound effect for removing four or more lines (Tetris).

        Returns:
            None
        """
        fullRows = obstacles.findFullRows(TOP, FLOOR, COLUMNS)
        if 3 > len(fullRows) > 0:
            # Score for completing rows (less than Tetris)
            self.score += 100 * len(fullRows)
            pygame.mixer.Channel(3).play(line_remove)
        elif len(fullRows) >= 3:
            # Score for Tetris (four or more completed rows)
            self.score += 500 + (100 * (len(fullRows) - 3))
            pygame.mixer.Channel(4).play(tetris_remove)
            self.prevTetris = True

        obstacles.removeFullRows(fullRows)

    def drop_instant_piece(self, obstacles: List[Shape], floor: int, line_remove: pygame.mixer.Sound, tetris_remove: pygame.mixer.Sound) -> None:
        """
        Drop the current shape instantly to the bottom, prepare for the next shape,
        and handle completed rows to update the score.

        Args:
            obstacles (List[Shape]): The list of obstacles (shapes) on the game board.
            floor (int): The floor position of the game board.
            line_remove (pygame.mixer.Sound): The sound effect for removing a single line.
            tetris_remove (pygame.mixer.Sound): The sound effect for removing four or more lines (Tetris).

        Returns:
            None
        """
        # Drop the current shape instantly to the bottom
        MovePiece.drop(self.shape, floor, obstacles, force_hit)
        obstacles.append(self.shape)

        # Prepare for the next shape
        shapeNo = self.nextShapeNo
        self.nextShapeNo = randint(1, 7)
        self.shape = Shape(MIDDLE, TOP, shapeNo)

        # Check and handle completed rows and update the score
        self.update_score_and_sound_effects(obstacles, line_remove, tetris_remove)
