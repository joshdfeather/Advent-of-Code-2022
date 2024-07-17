
import functools

with open("input16.txt", "r") as file:
    lines = [line.strip() for line in file]

g = {}
f = {}
for line in lines:
    valve = line[6:8]
    a, valves = line.split(';')
    _, flowrate = a.split('=')
    f[valve]= int(flowrate)
    valves = valves.replace("valves", "valve")[len(" tunnels lead to valve "):]
    g[valve] = valves.split(', ')

cur = "AA"

@functools.lru_cache(maxsize = None)
def maxflow(cur, opened, minleft):
    if minleft <= 0:
        return 0
    best = 0
    if cur not in opened:
        cur_opened = tuple(sorted(opened + (cur,)))
        val = (minleft - 1) * f[cur]
        for adj in g[cur]:
            if f[cur] != 0:
                best = max(best, val + maxflow(adj, cur_opened, minleft - 2))
            best = max(best, maxflow(adj, opened, minleft - 1))
    return best
        
print(maxflow("AA", (), 30))