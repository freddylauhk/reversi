from matplotlib.style import available


class Gameboard:
    
    __boardsize = 8
    __maxboardsizeIndex = __boardsize - 1

    __board = []

    def __init__(self):
        for row in range(self.__boardsize):
            temparray = []
            for column in range(self.__boardsize):
                temparray.append(0)
            
            self.__board.append(temparray)

        self.__board[3][3] = 1
        self.__board[3][4] = 2
        self.__board[4][3] = 2
        self.__board[4][4] = 1

        print("Gameboard initialized")

    def placePiece(self, row, column, piece):

        nullpiece = 0
        enermyPiece = 2 if piece == 1 else 1

        self.__board[row][column] = piece

        # flip pieces

        # Horizontal
        # Horizontal Left
        horizontalFliper = column
        if(column != 0):
            for horizontalChecker in range(column - 1, 0 , -1):
                if self.__board[row][horizontalChecker] == enermyPiece:
                    continue
                elif self.__board[row][horizontalChecker] == piece:
                    horizontalFliper = horizontalChecker
                    break
                elif self.__board[row][horizontalChecker] == nullpiece:
                    break

        if(horizontalFliper < column):
            for fliper in range(horizontalFliper + 1, column):
                self.flipPiece(self.__board[row][fliper])

        # Horizontal Right
        horizontalFliper = column
        if(column != self.__maxboardsizeIndex):
            for horizontalChecker in range(column + 1, self.__boardsize):
                if self.__board[row][horizontalChecker] == enermyPiece:
                    continue
                elif self.__board[row][horizontalChecker] == piece:
                    horizontalFliper = horizontalChecker
                    break
                elif self.__board[row][horizontalChecker] == nullpiece:
                    break
        
        if(horizontalFliper > column):
            for fliper in range(column + 1 , horizontalFliper):
                self.flipPiece(self.__board[row][fliper])


        # Vertical
        # Vertical Left
        verticalFliper = row
        if(row != 0):
            for verticalChecker in range(row - 1, 0 , -1):
                if self.__board[verticalChecker][column] == enermyPiece:
                    continue
                elif self.__board[verticalChecker][column] == piece:
                    verticalFliper = verticalChecker
                    break
                elif self.__board[verticalChecker][column] == nullpiece:
                    break

        if(verticalFliper < row):
            for fliper in range(verticalFliper + 1, row):
                self.flipPiece(self.__board[fliper][column])

        # Vertical Right
        verticalFliper = row
        if(row != self.__maxboardsizeIndex):
            for verticalChecker in range(row + 1, self.__boardsize):
                if self.__board[verticalChecker][column] == enermyPiece:
                    continue
                elif self.__board[verticalChecker][column] == piece:
                    verticalFliper = verticalChecker
                    break
                elif self.__board[verticalChecker][column] == nullpiece:
                    break
        
        if(verticalFliper > row):
            for fliper in range(row + 1 , verticalFliper):
                self.flipPiece(self.__board[fliper][column])

        # Diagonal
        # Top left
        diagonalFliper = 0
        if(row != 0 and column != 0):
            for diagonalChecker in range(1, (row if row < column else column) + 1):
                if self.__board[row - diagonalChecker][column - diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row - diagonalChecker][column - diagonalChecker] == piece:
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row - diagonalChecker][column - diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(self.__board[row - fliper][column - fliper])

        # Top right
        diagonalFliper = 0
        if(row != 0 and column != self.__maxboardsizeIndex):
            for diagonalChecker in range(1, (row if row < self.__maxboardsizeIndex - column else self.__maxboardsizeIndex - column) + 1):
                if self.__board[row - diagonalChecker][column + diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row - diagonalChecker][column + diagonalChecker] == piece:
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row - diagonalChecker][column + diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(self.__board[row - fliper][column + fliper])

        # Bottom left
        diagonalFliper = 0
        if(row != self.__maxboardsizeIndex and column != 0):
            for diagonalChecker in range(1, (self.__maxboardsizeIndex - row if self.__maxboardsizeIndex - row < column else column) + 1):
                if self.__board[row + diagonalChecker][column - diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row + diagonalChecker][column - diagonalChecker] == piece:
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row + diagonalChecker][column - diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(self.__board[row + fliper][column - fliper])

        # Bottom right
        diagonalFliper = 0
        if(row != self.__maxboardsizeIndex and column != self.__maxboardsizeIndex):
            for diagonalChecker in range(1, (self.__maxboardsizeIndex - row if row > column else self.__maxboardsizeIndex - column) + 1):
                if self.__board[row + diagonalChecker][column + diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row + diagonalChecker][column + diagonalChecker] == piece:
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row + diagonalChecker][column + diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(self.__board[row + fliper][column + fliper])

    def flipPiece(self, row, column):
        if self.__board[row][column] == 1:
            self.__board[row][column] = 2
        elif self.__board[row][column] == 2:
            self.__board[row][column] = 1


    def getAvaliableMove(self, piece):

        nullpiece = 0
        enermyPiece = 2 if piece == 1 else 1

        # Check duplicate in list
        availableMoveList = []

        for row in range(self.__boardsize):
            for column in range(self.__boardsize):
                if(self.__board[row][column] == piece):
                    # Horizontal
                    # Horizontal Left
                    

                    # Horizontal Right

                    # Vertical
                    # Vertical Left

                    # Vertical Right


                    # Diagonal
                    # Top Left


                    # Top Right


                    # Bottom left


                    # Bottom right

                    pass

        return 0


    def countPiecesOnBoard(self, pieceType):
        count = 0
        for row in range(self.__boardsize):
            for column in range(self.__boardsize):
                if(self.__board[row][column] == pieceType):
                    count += 1
        
        return count

    def getWinner(self):
        return self.countPiecesOnBoard(1) if self.countPiecesOnBoard(1) > self.countPiecesOnBoard(2) else self.countPiecesOnBoard(2)

    def getBoard(self):
        return self.__board

    def printBoard(self):
        for i in self.__board:
            print(i)

    def resetBoard(self):
        for row in range(self.__boardsize):
            temparray = []
            for column in range(self.__boardsize):
                temparray.append(0)
        
        self.__board[3][3] = 1
        self.__board[3][4] = 2
        self.__board[4][3] = 2
        self.__board[4][4] = 1

        print("Gameboard reset completed")