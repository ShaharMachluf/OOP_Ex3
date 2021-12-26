from DiGraph import DiGraph


def get_graph(size):
    g = DiGraph()
    for i in range(0, size):
        g.add_node(i)
    for i in range(10, int(size / 10)):
        for j in range(0, 10):
            g.add_edge(i * 3, i-j, 1)
    print(g.v_size())
    print(g.e_size())
    return g
