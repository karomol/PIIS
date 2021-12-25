from queue import PriorityQueue
def Search_Pass(graph, start, end):

    frontier = PriorityQueue()
    frontier.put((0, start))
    visited = {start: None}

    while True:
        if frontier.empty():
            return []

        ucs_w, current_node = frontier.get()


        if current_node == end:
            break

        for node in graph[current_node]:
            if node not in visited:
                frontier.put((
                    ucs_w,
                    node
                ))
                visited[node] = current_node

    return visited