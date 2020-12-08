#this would be the graph
gr = dict() #maps a integer to a list of integer, where the integers represent indexes of nodes
w = dict() #maps 2D tuple to a float, or an edge to a distance or weight
#change this according to your needs...

v = sorted(w, key=lambda x:w[x])
dc = {}
tr = {}
for u in v:
    if dc.get(u, None)==None:
        if tr.get(u[0], None)==None:
            tr[u[0]] = [u[1]]
            if tr.get(u[1], None)==None:
                tr[u[1]] = [u[0]]
            else:
                tr[u[1]].append(u[0])
            dc[u]=1
            dc[(u[1], u[0])] = 1
        elif tr.get(u[1], None)==None:
            tr[u[1]] = [u[0]]
            tr[u[0]].append(u[1])
            dc[u]=1
            dc[(u[1], u[0])] = 1
        else:
            r=True
            q = [u[0]]
            vis = {k:False for k in gr}
            while len(q)>0:
                f = q.pop(0)
                vis[f] = True
                for n in tr[f]:
                    if n==u[1]:
                        r=False
                    if not vis[n]:
                        q.append(n)
            if r:
                tr[u[0]].append(u[1])
                tr[u[1]].append(u[0])
                dc[u]=1
                dc[(u[1], u[0])] = 1
