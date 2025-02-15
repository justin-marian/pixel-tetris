import sys
import pygame
from random import randint

class IntroScreen:
    """
    Represents the introduction screen of the game.

    Args:
        screen (pygame.Surface): The game screen where the intro screen is displayed.
        intro_screen_img (pygame.Surface): The image to be displayed on the intro screen.

    Attributes:
        screen (pygame.Surface): The game screen where the intro screen is displayed.
        intro_screen_img (pygame.Surface): The image to be displayed on the intro screen.
        inPlay (bool): Flag indicating whether the game is in play.
        hasPlayed (bool): Flag indicating whether the intro screen has been played.

    Methods:
        run: Display the intro screen and handle user input to start the game.

    Example:
        To create an intro screen for the game:
        
        >>> intro_screen = IntroScreen(screen, intro_screen_img)
    """

    def __init__(self, screen, intro_screen_img):
        self.screen = screen
        self.intro_screen_img = intro_screen_img
        self.inPlay = False
        self.hasPlayed = False

    def run(self):
        """
        Display the intro screen and handle user input to start the game.

        The method displays the intro screen image and waits for the user to press the Enter key
        to start the game. Once the Enter key is pressed, it sets the 'inPlay' and 'hasPlayed'
        flags to True, indicating that the game is in play and the intro screen has been played.

        Returns:
            None
        """
        while not self.inPlay and not self.hasPlayed:
            self.screen.blit(self.intro_screen_img, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.inPlay = True
                    self.hasPlayed = True

class OutroScreen:
    """
    Represents the outro screen of the game.

    Args:
        screen (pygame.Surface): The game screen where the outro screen is displayed.
        outro_screen_img (pygame.Surface): The image to be displayed on the outro screen.

    Attributes:
        screen (pygame.Surface): The game screen where the outro screen is displayed.
        outro_screen_img (pygame.Surface): The image to be displayed on the outro screen.
        inPlay (bool): Flag indicating whether the game is in play.
        hasPlayed (bool): Flag indicating whether the outro screen has been played.

    Methods:
        run: Display the outro screen and handle user input to reset the game state and start a new game.

    Example:
        To create an outro screen for the game:
        
        >>> outro_screen = OutroScreen(screen, outro_screen_img)
    """

    def __init__(self, screen, outro_screen_img):
        self.screen = screen
        self.outro_screen_img = outro_screen_img
        self.inPlay = False
        self.hasPlayed = True

    def run(self):
        """
        Display the outro screen and handle user input to reset the game state and start a new game.

        The method displays the outro screen image and waits for the user to press the Enter key
        to reset the game state and start a new game. Once the Enter key is pressed, it sets the 'inPlay'
        flag to True, indicating that the game is in play, and 'hasPlayed' flag to False, indicating
        that the outro screen has not been played.

        Returns:
            None
        """
        while not self.inPlay and self.hasPlayed:
            self.screen.blit(self.outro_screen_img, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.reset_game_state()
                    self.inPlay = True
                    self.hasPlayed = False

    def reset_game_state(self):
        """
        Reset the game state to start a new game.

        This method resets the game state, including the global SCORE, shapeNo, and nextShapeNo,
        to start a new game.

        Returns:
            None
        """
        global SCORE
        SCORE = 0
        global shapeNo
        shapeNo = randint(1, 7)
        global nextShapeNo
        nextShapeNo = randint(1, 7)
