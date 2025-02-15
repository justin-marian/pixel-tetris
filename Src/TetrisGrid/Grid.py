from typing import List, Optional
from Util.Constants import *

class Grid:
    def __init__(self, col: int = 1, row: int = 1, blocksNo: int = 1, clr_list: Optional[List[int]] = None) -> None:
        """
        Initialize a Grid object.

        Parameters:
            col (int): Starting column position.
            row (int): Starting row position.
            blocksNo (int): Number of blocks in the grid.
            clr_list (list): List of color indices for the blocks (optional).

        Raises:
            ValueError: If there are invalid color indices in clr_list.
        """
        clr_list = clr_list or [1] * blocksNo
        if any(clr not in range(len(COLOURS)) for clr in clr_list):
            raise ValueError("Invalid color index in clr_list")
        self.col = col
        self.row = row
        self._colOffsets = [0] * blocksNo
        self._rowOffsets = [0] * blocksNo
        self.blocks = [{'col': col, 'row': row, 'clr': clr} for clr in clr_list]

    def update(self) -> None:
        """
        Update the positions of the blocks based on col and row offsets.
        """
        self.blocks = [{'col': self.col + col_offset, 'row': self.row + row_offset, 'clr': block['clr']}
                       for block, col_offset, row_offset in zip(self.blocks, self._colOffsets, self._rowOffsets)]

    def collides(self, other: 'Grid') -> bool:
        """
        Check if this grid collides with another grid.

        Parameters:
            other (Grid): Another grid to check for collisions.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        return any(block['col'] == obstacle['col'] and block['row'] == obstacle['row']
                   for block in self.blocks for obstacle in other.blocks)

    def append(self, other: 'Grid') -> None:
        """
        Append the blocks of another grid to this grid.

        Parameters:
            other (Grid): Another grid whose blocks will be appended to this grid.
        """
        self.blocks.extend(other.blocks)

    def draw(self, surface: pygame.Surface, shadow: bool = False) -> None:
        """
        Draw the grid on a given surface.

        Parameters:
            surface (pygame.Surface): The surface to draw on.
            shadow (bool): Whether to draw a shadow (default is False).
        """
        border_thickness = 3
        shadow_thickness = 4 

        for block in self.blocks:
            x, y = block['col'] * GRIDSIZE, block['row'] * GRIDSIZE

            if not shadow:
                inner_rect = (x + border_thickness, y + border_thickness,
                              GRIDSIZE - 2 * border_thickness, GRIDSIZE - 2 * border_thickness)
                border_rect = (x, y, GRIDSIZE, GRIDSIZE)

                pygame.draw.rect(surface, COLOURS[block['clr']], inner_rect)
                pygame.draw.rect(surface, GRAY, border_rect, border_thickness)
            else:
                pygame.draw.rect(surface, AGRAY, (x, y, GRIDSIZE, GRIDSIZE), shadow_thickness)

    @staticmethod
    def draw_grid(screen: pygame.Surface) -> None:
        """
        Draw the grid lines on the game screen.

        Parameters:
            screen (pygame.Surface): The game screen surface.
        """
        grid_line_thickness = 2

        for i in range(COLUMNS + 1):
            pygame.draw.line(screen, BLACK, (i * GRIDSIZE, 0), (i * GRIDSIZE, HEIGHT), grid_line_thickness)
        for i in range(ROWS + 1):
            pygame.draw.line(screen, BLACK, (0, i * GRIDSIZE), (GRIDSIZE * COLUMNS, i * GRIDSIZE), grid_line_thickness)

    @staticmethod
    def redraw_screen(screen, grid_img, tetris_img, shape, shadow, obstacles, block_img_lst, next_shape_no, score, level, my_font):
        """
        Redraw the game screen with updated elements.

        Parameters:
            screen  (pygame.Surface): The game screen surface.
            grid_img (pygame.Surface): The background grid image.
            tetris_img (pygame.Surface): The Tetris logo image.
            shape (Shape): The current game shape.
            shadow (Shape): The shadow of the game shape.
            obstacles (Grid): The grid containing obstacles (other shapes).
            block_img_lst (list): List of block images for next shape preview.
            next_shape_no (int): Index of the next shape.
            score (int): The player's score.
            level (int): The current game level.
            my_font (pygame.Font): Font for displaying text.
        """
        screen.blit(grid_img, (0, 0))
        Grid.draw_grid(screen)
        screen.blit(tetris_img, (GRIDSIZE * COLUMNS, 0))
        shape.draw(screen)
        shadow.draw(screen, True)
        obstacles.draw(screen)

        # Fixed base positions
        base_x_position = GRIDSIZE * COLUMNS
        fixed_y_offset = 160

        # Fixed positions for score, level, and timer
        score_pos = (base_x_position + 100, 540 - fixed_y_offset / 2)   # Score
        level_pos = (base_x_position + 100, 540 - fixed_y_offset)       # Level
        timer_pos = (base_x_position + 100, 540)                        # Timer
        next_shape_pos_x = base_x_position + 72

        # Dictionary for text rendering
        texts = {
            'score': (str(level + 1), score_pos),
            'level': (str(score), level_pos),
            'timer': (str(round(pygame.time.get_ticks() / 1000, 2)), timer_pos),
        }

        # Render and blit the text onto the screen
        for text, position in texts.values():
            text_surface = my_font.render(text, True, RED)
            screen.blit(text_surface, position)
            
        shape_offset = 0
        if next_shape_no == 5:
            shape_offset = -10
        elif next_shape_no == 7:
            shape_offset = 10

        screen.blit(block_img_lst[next_shape_no - 1], (next_shape_pos_x + shape_offset, 240))

        pygame.display.flip()
