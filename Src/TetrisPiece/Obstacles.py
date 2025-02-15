from TetrisGrid.Grid import Grid

class Obstacles(Grid):
    """ Represents the grid of obstacles formed by placed Tetriminos.

    Inherits from Grid to create a grid of obstacles formed by Tetriminos.
    This class provides methods for finding and removing full rows of obstacles.

    Args:
        col (int): The column where the anchor block is located.
        row (int): The row where the anchor block is located.
        blocksNo (int): The number of blocks in the grid.

    Attributes:
        col (int): The column where the anchor block is located.
        row (int): The row where the anchor block is located.
        blocksNo (int): The number of blocks in the grid.

    Methods:
        findFullRows(top, bottom, columns): Find full rows within a specified range.
        removeFullRows(fullRows): Remove full rows from the grid.

    """
    def __init__(self, col=0, row=0, blocksNo=0):
        # Initialize the Obstacles object using the parent Grid class
        super().__init__(col, row, blocksNo)
        
    def findFullRows(self, top, bottom, columns):
        """
        Find full rows within a specified range.

        Args:
            top (int): The top row of the range to search for full rows.
            bottom (int): The bottom row of the range to search for full rows.
            columns (int): The number of columns in the grid.

        Returns:
            list: A list of row indices that are full within the specified range.

        """
        rows = [block['row'] for block in self.blocks]
        return [row for row in range(top, bottom) if rows.count(row) == columns]

    def removeFullRows(self, fullRows):
        """
        Remove full rows from the grid.

        Args:
            fullRows (list): A list of row indices to remove from the grid.

        Returns:
            None

        """
        for row in fullRows:
            # Remove blocks in the full row
            self.blocks = [block for block in self.blocks if block['row'] != row]

            # Move down blocks above the removed row
            for block in self.blocks:
                if block['row'] < row:
                    block['row'] += 1
