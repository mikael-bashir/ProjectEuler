

def minimax(position, depth, maxPlayer, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if maxPlayer:
        maxEval = float('-inf')  # assume worst case scenario
        bestMove = None
        for move in position.getAllMoves():
            evaluation = minimax(move, depth-1, False, game)[0]
            if evaluation > maxEval:
                maxEval = evaluation
                bestMove = move
        return maxEval, bestMove

    else:
        minEval = float('inf')
        bestMove = None
        for move in position.getAllMoves():
            evaluation = minimax(move, depth-1, False, game)[0]
            if evaluation < minEval:
                minEval = evaluation
                bestMove = move
        return minEval, bestMove