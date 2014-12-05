import random


class GameLogic:

    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def isWinner(self, player_letter):
        return ((self.board[0] == player_letter and self.board[1] == player_letter and self.board[2] == player_letter)
                or (self.board[3] == player_letter and
                    self.board[4] == player_letter and self.board[5] == player_letter)
                or (self.board[6] == player_letter and
                    self.board[7] == player_letter and self.board[8] == player_letter)
                or (self.board[0] == player_letter and
                    self.board[4] == player_letter and self.board[8] == player_letter)
                or (self.board[3] == player_letter and
                    self.board[5] == player_letter and self.board[7] == player_letter)
                or (self.board[0] == player_letter and
                    self.board[3] == player_letter and self.board[6] == player_letter)
                or (self.board[1] == player_letter and
                    self.board[4] == player_letter and self.board[7] == player_letter)
                or (self.board[2] == player_letter and
                    self.board[5] == player_letter and self.board[8] == player_letter))

    def makeMove(self, player_letter, index):

        if self.isEmpty(index):
            self.board[index] = player_letter
        else:
            print("choose another place!")

    def isEmpty(self, index):
        if self.board[index] == ' ':
            return True
        return False

    def printBoard(self):
        for index in range(0, 7, 3):
            print('-------------')
            print('| ' + self.board[index] + ' | ' + self.board[index + 1] + ' | ' + self.board[index + 2] + ' |')
        print('-------------')

    def inputPlayerLetter(self):

        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def isBoardFull(self):
        index = 0
        while index <= 8 and not self.isEmpty(index):
            index += 1
        if index == 9:
            return True
        else:
            return False

        # for i in range(0, 9):
        #    if isEmpty(i):
        #        pass
        # return False

    def gameEnd(self, player, computer):
        if self.isWinner(player) or self.isWinner(computer) or self.isBoardFull():
            return True
        return False

    def chooseRandomMoveFromList(self, movesList):
        possibleMoves = []
        for i in movesList:
            if self.isEmpty(i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            #no free spaces
            return 'none'

    def computerIndex(self):
        move = self.chooseRandomMoveFromList([0, 2, 6, 8])
        if move != 'none':
            return move
        if self.isEmpty(4):
            return 4
        return self.chooseRandomMoveFromList([1, 3, 5, 7])

    def main(self):
        print("Hello you are playing tic-tac-toe game")
        letters = self.inputPlayerLetter()
        player_letter = letters[0]
        computer_letter = letters[1]
        self.printBoard()
        while(not self.gameEnd(player_letter, computer_letter)):
            #self.printBoard()
            print("Players turn")
            print("Choose field(0-8)")
            player_index = int(input("Enter your field number: "))
            while not self.isEmpty(player_index):
                player_index = int(input("Enter correct number: "))
            self.makeMove(player_letter, player_index)
            if self.isWinner(player_letter):
                print("player wins")
                break
            self.makeMove(computer_letter, self.computerIndex())
            if self.isWinner(computer_letter):
                print("computer wins")
                break
            self.printBoard()
        self.printBoard()

def main():

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    game = GameLogic()
    game.main()

if __name__ == '__main__':
    main()
