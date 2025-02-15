from .Grid import Grid

class Floor(Grid):
    """ Represents a horizontal line of blocks.

    Inherits from Grid to create a horizontal line (floor) of blocks.

    Args:
        col (int): The column where the anchor block is located.
        row (int): The row where the anchor block is located.
        blocksNo (int): The number of blocks in the floor.

    Attributes:
        col (int): The column where the anchor block is located.
        row (int): The row where the anchor block is located.
        blocksNo (int): The number of blocks in the floor.

    Note:
        This class inherits from Grid and represents a horizontal line of blocks.
        It allows you to create horizontal lines of blocks with the specified number.

    Example:
        To create a horizontal floor of 5 blocks at column 3, row 7:
        
        >>> floor = Floor(col=3, row=7, blocksNo=5)
    """

    def __init__(self, col: int = 1, row: int = 1, blocksNo: int = 1) -> None:
        # Initialize the Floor object using the parent Grid class
        super().__init__(col, row, blocksNo)
        # Calculate the column offsets for the floor
        self._colOffsets = list(range(blocksNo))
        # Update the positions of the floor blocks
        self.update()
