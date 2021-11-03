from queue import Queue


def Search_Pass(graph, start, goal):
    visited = set()
    queue = Queue()
    queue.put((start, [start]))

    while queue:
        (cur_node, path) = queue.get()
        if cur_node not in visited:
            visited.add(cur_node)

            if cur_node == goal:
                return path
            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited:
                    queue.put((next_node, path + [next_node]))