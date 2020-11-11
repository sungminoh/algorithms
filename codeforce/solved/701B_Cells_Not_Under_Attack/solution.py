class ChessBoard(object):
    def __init__(self, n):
        self.x_under_attack = set()
        self.y_under_attack = set()
        self.size = n
        self.number_of_not_under_attack = []

    def put(self, x, y):
        self.x_under_attack.add(x)
        self.y_under_attack.add(y)
        self.number_of_not_under_attack.append(self.count_not_under_attack())

    def count_not_under_attack(self):
        number_of_attacked_columns = len(self.x_under_attack)
        number_of_attacked_rows = len(self.y_under_attack)
        return self.size**2 -\
            self.size*(number_of_attacked_columns + number_of_attacked_rows) +\
            number_of_attacked_columns * number_of_attacked_rows

    def print_numbers_of_not_under_attack(self):
        print ' '.join(map(str, self.number_of_not_under_attack))


def main():
    n, m = map(int, raw_input().split())
    chess_board = ChessBoard(n)
    for i in xrange(m):
        chess_board.put(* map(int, raw_input().split()))
    chess_board.print_numbers_of_not_under_attack()



if __name__ == '__main__':
    main()
