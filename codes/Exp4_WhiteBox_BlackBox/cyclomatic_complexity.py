# cyclomatic_complexity.py - compute V(G) = E - N + 2P for a flow graph
# Edit the edges list for the graph given in your exam.
def cyclomatic(edges, P=1):
    nodes = {n for e in edges for n in e}
    E, N = len(edges), len(nodes)
    return E, N, E - N + 2 * P

# Loop example from the guide: sum of even numbers 1..n
loop_edges = [(1, 2), (2, 3), (2, 6), (3, 4), (3, 5), (4, 5), (5, 2)]
# Login validator: decisions D1..D5, returns R2..R12, end node X
login_edges = [('D1','R2'),('D1','D2'),('D2','R4'),('D2','D3'),('D3','R6'),('D3','D4'),
               ('D4','R8'),('D4','D5'),('D5','R10'),('D5','R12'),
               ('R2','X'),('R4','X'),('R6','X'),('R8','X'),('R10','X'),('R12','X')]
for name, g in [('Loop example', loop_edges), ('Login validator', login_edges)]:
    E, N, v = cyclomatic(g)
    print(f'{name}: E={E}, N={N}, V(G)={E}-{N}+2 = {v}')
