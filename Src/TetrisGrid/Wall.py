from .Grid import Grid

class Wall(Grid):
    """
    Represents a vertical line of blocks.

    Inherits from Grid to create a vertical line (wall) of blocks.

    Args:
        col (int): The column where the anchor block is located.
        row (int): The row where the anchor block is located.
        blocksNo (int): The number of blocks in the wall.
        clr (int): The color index for the wall.

    Attributes:
        col (int): The column where the anchor block is located.
        row (int): The row where the anchor block is located.
        blocksNo (int): The number of blocks in the wall.

    Note:
        This class inherits from Grid and represents a vertical line of blocks.
        It allows you to create walls of blocks with the specified color index.

    Example:
        To create a vertical wall of 3 blocks at column 5, row 2 with color index 2:
        
        >>> wall = Wall(col=5, row=2, blocksNo=3, clr=2)
    """
    def __init__(self, col: int = 1, row: int = 1, blocksNo: int = 1, clr: int = 1) -> None:
        # Create a list of color indices for the wall blocks
        color_indices = [clr] * blocksNo
        # Initialize the Wall object using the parent Grid class
        super().__init__(col, row, blocksNo, clr_list=color_indices)
        # Calculate the row offsets for the wall
        self._rowOffsets = list(range(blocksNo))
        # Update the positions of the wall blocks
        self.update()
