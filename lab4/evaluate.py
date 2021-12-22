import const
INFINITY = 100000000000

def getClosestEnemyCoordsAndDistance(node):
    shortestDistance = INFINITY
    coords = (0, 0)

    for enemy in const.enemies:
        enemyNode = const.get_element_pos(enemy.rect.x, enemy.rect.y)
        distance = const.getDistance(node, enemyNode)
        if distance < shortestDistance:
            shortestDistance = distance
            coords = (enemy.rect.x, enemy.rect.y)
    return coords, shortestDistance

def getDistanceToClosestEnemy(node):
    if node == const.player.goal:
        return -INFINITY

    distance = (getClosestEnemyCoordsAndDistance(node))[1]
    return distance

def evaluationFunction(node):
    return getDistanceToClosestEnemy(node) * -1

