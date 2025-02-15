import pygame
from random import randint
from Util.Constants import *

from TetrisPiece import Obstacles
from TetrisGrid import Floor, Wall
from TetrisPiece.Shape import Shape

class MovePiece:
    @staticmethod
    def drop(my_shape: Shape, floor: Floor, obstacles: Obstacles, force_hit: pygame.mixer.Sound) -> None:
        """
        Drop a shape until it collides with the floor or other obstacles.

        Args:
            my_shape (Shape): The shape to drop.
            floor (Floor): The floor object representing the bottom boundary.
            obstacles (Obstacles): The obstacles on the grid.
            force_hit (Sound): The sound effect to play when the shape hits the floor.

        Drops the given shape vertically until it collides with either the floor or other obstacles. If the shape
        is not a shadow, it plays the 'force_hit' sound effect upon hitting the floor.

        Returns:
            None
        """
        while True:
            my_shape.move_down()
            if my_shape.collides(floor) or my_shape.collides(obstacles):
                my_shape.move_up()
                break
        if not my_shape.shadow:
            pygame.mixer.Channel(2).play(force_hit)

    @staticmethod
    def move_piece_left(shape: Shape, leftWall: Wall, obstacles: Obstacles) -> None:
        """
        Move a shape to the left if possible.

        Args:
            shape (Shape): The shape to move.
            leftWall (Wall): The left wall object representing the left boundary.
            obstacles (Obstacles): The obstacles on the grid.

        Moves the given shape one step to the left if it does not collide with the left wall or other obstacles.

        Returns:
            None
        """
        shape.move_left()
        if shape.collides(leftWall) or shape.collides(obstacles):
            shape.move_right()

    @staticmethod
    def move_piece_right(shape: Shape, rightWall: Wall, obstacles: Obstacles) -> None:
        """
        Move a shape to the right if possible.

        Args:
            shape (Shape): The shape to move.
            rightWall (Wall): The right wall object representing the right boundary.
            obstacles (Obstacles): The obstacles on the grid.

        Moves the given shape one step to the right if it does not collide with the right wall or other obstacles.

        Returns:
            None
        """
        shape.move_right()
        if shape.collides(rightWall) or shape.collides(obstacles):
            shape.move_left()

    @staticmethod
    def rotate_piece_clockwise(shape: Shape, leftWall: Wall, rightWall: Wall, floor: Floor, obstacles: Obstacles, block_rotate: pygame.mixer.Sound) -> None:
        """
        Rotate a shape clockwise if possible.

        Args:
            shape (Shape): The shape to rotate.
            leftWall (Wall): The left wall object representing the left boundary.
            rightWall (Wall): The right wall object representing the right boundary.
            floor (Floor): The floor object representing the bottom boundary.
            obstacles (Obstacles): The obstacles on the grid.
            block_rotate (Sound): The sound effect to play when the shape rotates.

        Rotates the given shape clockwise if the rotation does not result in collisions with the walls, floor,
        or other obstacles. If the rotation is successful, it plays the 'block_rotate' sound effect.

        Returns:
            None
        """
        shape.rotateClkwise()
        shape.rotate()
        if shape.collides(leftWall) or shape.collides(rightWall) or shape.collides(floor) or shape.collides(obstacles):
            shape.rotateCntclkwise()
            shape.rotate()
        else:
            pygame.mixer.Channel(1).play(block_rotate)

    @staticmethod
    def drop_piece(shape: Shape, floor: Floor, obstacles: Obstacles, nextShapeNo: int) -> None:
        """
        Drop a shape one step and handle collision.

        Args:
            shape (Shape): The shape to drop.
            floor (Floor): The floor object representing the bottom boundary.
            obstacles (Obstacles): The obstacles on the grid.
            nextShapeNo (int): The next shape number for spawning a new shape.
            MIDDLE (int): The middle column for spawning a new shape.
            TOP (int): The top row for spawning a new shape.

        Drops the given shape one step vertically. If the shape collides with the floor or other obstacles,
        it adds the shape to the obstacles and removes any full rows. Then, it spawns a new shape at the
        specified location.

        Returns:
            None
        """
        shape.move_down()
        if shape.collides(floor) or shape.collides(obstacles):
            shape.move_up()
            obstacles.append(shape)
            fullRows = obstacles.findFullRows(TOP, FLOOR, COLUMNS)
            obstacles.removeFullRows(fullRows)
            shapeNo = nextShapeNo
            nextShapeNo = randint(1, 7)
            shape = Shape(MIDDLE, TOP, shapeNo)
