import sys


def dfs(adj):

    # init the global variables
    global color, has_cycle

    has_cycle = False
    color = {node: "w" for node in adj}

    # loop through each node in the graph
    for node in adj:
        if color[node] == "w":
            dfs_visit(adj, node)

    return has_cycle


def dfs_visit(adj, node):

    global color, has_cycle

    # update state of the node
    color[node] = "g"

    for child in adj[node]:

        # go deeper in the search
        if color[child] == "w":
            dfs_visit(adj, child)

        # if the node is a grey, a cycle is detected
        elif color[child] == "g":
            has_cycle = True

    # update state of the node
    color[node] = "b"


def main(filename):

    with open(filename, "r") as fp:
        lines = fp.readlines()

    # clean the ends on files
    lines = [line.strip() for line in lines]

    num_nodes = int(lines.pop(0))
    adj = {i: [] for i in range(num_nodes)}

    # populate the adjacency list
    for line in lines:
        node1, node2 = [int(i) for i in line.split()]
        adj[node1].append(node2)

    has_cycle = dfs(adj)
    print(has_cycle)


if __name__ == "__main__":

    main(sys.argv[1])
