class SolitaireMancala(object):
    '''
    Creates a solitaire Manchala object
    '''
    def __init__(self):
        '''
        Initializes a configuration with
        an empty store
        '''
        self._board = [0]

    def set_board(self, configuration):
        '''
        Sets a board with the passed configuration
        :param configuration: list
        :return: None
        '''
        self._board = list(configuration)

    def __str__(self):
        '''
        Returns a string representation of the board
        :return: String
        '''
        board_copy = list(self._board)
        board_copy.reverse()
        return ", ".join(map(str, board_copy))

    def get_num_seeds(self, house_num):
        '''
        Returns number of seeds at the index of a particular house
        :param house_num: int
        :return: int
        '''
        return self._board[house_num]

    def is_legal_move(self, house_num):
        '''
        Checks if the move is a legal move or not
        :param house_num: int
        :return: Boolean
        '''
        if house_num == 0:
            return False
        else:
            return self._board[house_num] == house_num

    def apply_move(self, house_num):
        '''
        Applies moves to the board
        :param house_num:
        :return: moves
        '''
        if self.is_legal_move(house_num):
            for index in range(0, house_num):
                self._board[index] += 1
                self._board[house_num] -= 1

    def choose_move(self):
        '''
        Chooses the next best legal move
        :return: int
        '''
        for index in range(1, len(self._board)):
            if self.is_legal_move(index):
                return index

        return 0

    def is_game_won(self):
        '''
        Checks if all indices on the game are 0
        :return: bool
        '''
        for index in range(1, len(self._board)):
            if self._board[index] != 0:
                return False

        return True

    def plan_moves(self):
        '''
        Keep finding available moves
        until you get the desired result
        :return: list
        '''
        moves = []
        move = self.choose_move()
        while move != 0:
            moves.append(move)
            self.apply_move(move)
            move = self.choose_move()

        return moves
