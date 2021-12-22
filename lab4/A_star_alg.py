def astar(grath, start, stop):
    open_lst = {start}
    closed_lst = set([])

    poo = {}
    poo[start] = 0

    par = {}
    par[start] = start

    while len(open_lst) > 0:
        n = None

        for v in open_lst:
            if n == None or poo[v] + 1 < poo[n] + 1:
                n = v

        if n == None:
            return []

        if n == stop:
            reconst_path = []

            while par[n] != n:
                reconst_path.append(n)
                n = par[n]

            reconst_path.append(start)

            reconst_path.reverse()

            return reconst_path

        temp = grath.get(n)
        for m in temp:
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                par[m] = n
                poo[m] = poo[n] + 1

            else:
                if poo[m] > poo[n] + 1:
                    poo[m] = poo[n] + 1
                    par[m] = n

                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)

        open_lst.remove(n)
        closed_lst.add(n)

    return []
