# Implements the Maze ADT using a 2-D array.
from Mase.arrays import Array2D
from linkedstack import LinkedStack as Stack

class Maze :
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    # Creates a maze object with all cells marked as open.
    def __init__( self, num_rows, num_cols ):
        self._mazeCells = Array2D( num_rows, num_cols )
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maze.
    def num_rows( self ):
        return self._mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols( self ):
        return self._mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def setWall( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition( row, col )

    # Sets the exit cell position.
    def setExit( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition( row, col )

    #g Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath( self ):
        stack = Stack()
        stack.push(self._startCell)
        while not stack.isEmpty():
            cell = stack.pop()
            self._markTried(cell.row, cell.col)
            if self._exitFound(cell.row, cell.col):
                for i in cell.path:
                    self._markPath(i.row, i.col)
                self._markPath(cell.row, cell.col)
                return True
            if self._validMove(cell.row + 1, cell.col):
                new = _CellPosition(cell.row + 1, cell.col, cell.path + [cell])
                stack.push(new)
            if self._validMove(cell.row - 1, cell.col):
                new = _CellPosition(cell.row - 1, cell.col, cell.path + [cell])
                stack.push(new)
            if self._validMove(cell.row, cell.col + 1):
                new = _CellPosition(cell.row, cell.col + 1, cell.path + [cell])
                stack.push(new)
            if self._validMove(cell.row, cell.col - 1):
                new = _CellPosition(cell.row, cell.col - 1, cell.path + [cell])
                stack.push(new)

        return False


    # Resets the maze by removing all "path" and "tried" tokens.
    def reset( self ):
        for a in range(self.num_rows()):
            for b in range(self.num_cols()):
                c = self._mazeCells[a, b]
                if c == self.TRIED_TOKEN or c == self.PATH_TOKEN:
                    self._mazeCells[a, b] = None

    # Prints a text-based representation of the maze.
    def draw( self ):
        for a in range(self.num_rows()):
            for b in range(self.num_cols()):
                c = self._mazeCells[a, b]
                if c is None:
                    c = " "
                print(c, end="")
            print()

    # Returns True if the given cell position is a valid move.
    def _validMove( self, row, col ):
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exitFound( self, row, col ):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried( self, row, col ):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath( self, row, col ):
        self._mazeCells[row, col] = self.PATH_TOKEN

# Private storage class for holding a cell position.
class _CellPosition( object ):
    def __init__( self, row, col, path = []):
        self.row = row
        self.col = col
        self.path = path

