import const
import evaluate

graph = const.GetGraph()
INFINITY = evaluate.INFINITY

def minimax(maximizingPlayer, depth, node, alpha, beta):
    if depth == 3:
        return evaluate.evaluationFunction(node)
    if maximizingPlayer:
        value = -INFINITY
        for child in graph[node]:
            value = max(value, minimax(False, depth, child, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = INFINITY
        for child in graph[node]:
            value = min(value, minimax(True, depth + 1, child, alpha, beta))
            alpha = min(alpha, value)
            if beta <= alpha:
                break
        return value


def expectimax(maximizingPlayer, depth, node):
    if depth == 3:
        return evaluate.evaluationFunction(node)
    if maximizingPlayer:
        return max(expectimax(False, depth, child) for child in graph[node])
    else:
        return sum(expectimax(True, depth + 1, child) for child in graph[node]) / float(len(graph[node]))