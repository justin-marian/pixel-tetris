from TetrisGrid.Grid import Grid

class Shape(Grid):
    """
    Represents a tetromino shape in the game, consisting of four blocks.

    Args:
        col (int): The column index where the shape is currently located.
        row (int): The row index where the shape is currently located.
        clr (int): The color index defining the shape's appearance.
        rot (int): The current rotation state of the shape (0 to 3).
        shadow (bool): Flag indicating whether the shape is a shadow.

    Attributes:
        col (int): The column index where the shape is currently located.
        row (int): The row index where the shape is currently located.
        clr (int): The color index defining the shape's appearance.
        rot (int): The current rotation state of the shape (0 to 3).
        shadow (bool): Flag indicating whether the shape is a shadow.
        _colOffsets (list): List of column offsets for each block in the shape.
        _rowOffsets (list): List of row offsets for each block in the shape.

    Methods:
        move_left: Move the shape one column to the left.
        move_right: Move the shape one column to the right.
        move_down: Move the shape one row down.
        move_up: Move the shape one row up.
        rotateCntclkwise: Rotate the shape counterclockwise (90 degrees).
        rotateClkwise: Rotate the shape clockwise (90 degrees).

    Note:
        This class inherits from Grid and represents a tetromino shape in the game.
        It provides methods to move and rotate the shape on the game grid.

    Example:
        To create a Z-shaped tetromino at column 3, row 7 with a rotation state of 2:
        
        >>> shape = Shape(col=3, row=7, clr=1, rot=2)
    """

    Trominos = {
        # Red Z-Tetromino
        1: {
            # Initial orientation
            0: ([-1, -1, 0, 0], [1, 0, 0, -1]),
            # 90 degrees rotation
            1: ([-1, 0, 0, 1], [-1, -1, 0, 0]),
            # 180 degrees rotation
            2: ([1, 1, 0, 0], [-1, 0, 0, 1]),
            # 270 degrees rotation
            3: ([1, 0, 0, -1], [1, 1, 0, 0])
        },
        # Green S-Tetromino
        2: {
            # Initial orientation
            0: ([-1, -1, 0, 0], [-1, 0, 0, 1]),
            # 90 degrees rotation
            1: ([1, 0, 0, -1], [-1, -1, 0, 0]),
            # 180 degrees rotation
            2: ([1, 1, 0, 0], [1, 0, 0, -1]),
            # 270 degrees rotation
            3: ([-1, 0, 0, 1], [1, 1, 0, 0])
        },
        # Blue J-Tetromino
        3: {
            # Initial orientation
            0: ([-1, -1, 0, 1], [-1, 0, 0, 0]),
            # 90 degrees rotation
            1: ([1, 1, 0, -1], [1, 0, 0, 0]),
            # 180 degrees rotation
            2: ([1, 0, 0, 0], [-1, -1, 0, 1]),
            # 270 degrees rotation
            3: ([-1, 0, 0, 0], [1, 1, 0, -1])
        },
        # Orange L-Tetromino
        4: {
            # Initial orientation
            0: ([1, 1, 0, -1], [-1, 0, 0, 0]),
            # 90 degrees rotation
            1: ([-1, -1, 0, 1], [1, 0, 0, 0]),
            # 180 degrees rotation
            2: ([-1, 0, 0, 0], [-1, -1, 0, 1]),
            # 270 degrees rotation
            3: ([1, 0, 0, 0], [1, 1, 0, -1])
        },
        # Cyan I-Tetromino
        5: {
            # Initial orientation
            0: ([0, 0, 0, 0], [-2, 1, 0, -1]),
            # 90 degrees rotation
            1: ([-2, 1, 0, -1], [0, 0, 0, 0]),
            # 180 degrees rotation
            2: ([-2, -1, 0, 1], [0, 0, 0, 0]),
            # 270 degrees rotation
            3: ([0, 0, 0, 0], [-2, -1, 0, 1])
        },
        # Purple T-Tetromino
        6: {
            # Initial orientation
            0: ([0, -1, 0, 0], [1, 0, 0, -1]),
            # 90 degrees rotation
            1: ([-1, 0, 0, 1], [0, -1, 0, 0]),
            # 180 degrees rotation
            2: ([0, 1, 0, 0], [-1, 0, 0, 1]),
            # 270 degrees rotation
            3: ([1, 0, 0, -1], [0, 1, 0, 0])
        },
        # Yellow O-Tetromino
        # Does not rotate, so all offsets are the same
        7: {
            # Initial orientation
            0: ([-1, -1, 0, 0], [0, -1, 0, -1]),
            # 90 degrees rotation
            1: ([-1, -1, 0, 0], [0, -1, 0, -1]),
            # 180 degrees rotation
            2: ([-1, -1, 0, 0], [0, -1, 0, -1]),
            # 270 degrees rotation
            3: ([-1, -1, 0, 0], [0, -1, 0, -1])
        }
    }

    def __init__(self, col=1, row=1, clr=1, rot=0, shadow=False):
        # Create a list of color indices for the blocks in the shape
        color_indices = [clr] * 4
        # Initialize the Shape object using the parent Grid class
        super().__init__(col, row, 4, clr_list=color_indices)
        self.clr = clr
        self.shadow = shadow
        self._rot = rot
        self._colOffsets = None
        self._rowOffsets = None
        self.rotate()

    def rotate(self):
        """
        Rotate the shape based on its current rotation state.

        This private method updates the column and row offsets for the shape based on its
        current color and rotation state. It uses the 'Trominos' dictionary to look up the
        offsets for the given color and rotation.

        Returns:
            None
        """
        if self.clr in Shape.Trominos:
            self._colOffsets, self._rowOffsets = Shape.Trominos[self.clr][self._rot]
            self.update()

    def move_left(self):
        """
        Move the shape one column to the left.

        Returns:
            None
        """
        self.col = self.col - 1
        self.update()

    def move_right(self):
        """
        Move the shape one column to the right.

        Returns:
            None
        """
        self.col = self.col + 1
        self.update()

    def move_down(self):
        """
        Move the shape one row down.

        Returns:
            None
        """
        self.row = self.row + 1
        self.update()

    def move_up(self):
        """
        Move the shape one row up.

        Returns:
            None
        """
        self.row = self.row - 1
        self.update()

    def rotateCntclkwise(self):
        """
        Rotate the shape counterclockwise (90 degrees).

        Returns:
            None
        """
        self._rot = (self._rot - 1) % 4
        self.rotate()

    def rotateClkwise(self):
        """
        Rotate the shape clockwise (90 degrees).

        Returns:
            None
        """
        self._rot = (self._rot + 1) % 4
        self.rotate()
