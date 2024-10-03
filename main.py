import chess
import chess.engine

class SimpleChessEngine:
    def __init__(self):
        self.board = chess.Board()

    def evaluate(self):
        # Simple evaluation function based on material count
        material_count = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0,  # King has no material value
        }

        score = 0
        for piece in chess.PIECE_TYPES:
            score += len(self.board.pieces(piece, chess.WHITE)) * material_count[piece]
            score -= len(self.board.pieces(piece, chess.BLACK)) * material_count[piece]
        
        return score

    def generate_moves(self):
        return list(self.board.legal_moves)

    def minimax(self, depth, is_maximizing):
        if depth == 0 or self.board.is_game_over():
            return self.evaluate()

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.generate_moves():
                self.board.push(move)
                eval = self.minimax(depth - 1, False)
                self.board.pop()
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.generate_moves():
                self.board.push(move)
                eval = self.minimax(depth - 1, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, depth=3):
        best_move = None
        max_eval = float('-inf')
        for move in self.generate_moves():
            self.board.push(move)
            eval = self.minimax(depth - 1, False)
            self.board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move

    def play(self):
        while not self.board.is_game_over():
            print(self.board)
            if self.board.turn == chess.WHITE:
                move = self.best_move(depth=3)
                self.board.push(move)
            else:
                user_move = input("Enter your move: ")
                self.board.push(chess.Move.from_uci(user_move))

if __name__ == "__main__":
    engine = SimpleChessEngine()
    engine.play()
