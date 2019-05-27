#!/usr/bin/env python3

all_paths = []

def find_all_paths(graph, path):
    """
    Trivial function to traverse a DAG and get all paths,
    once a path has reached its end, it is logged in the global variable all_paths
    :param graph:
    :param path:
    :return:
    """
    start_node = path[len(path)-1]
    if start_node not in graph:
        all_paths.append(path)
    else:
        nodes = graph[start_node]
        if nodes:
            for node in nodes:
                next_path = path + [node]
                find_all_paths(graph, next_path)
        else:
            all_paths.append(path)


def get_all_paths(user_dag):
    """
    Gets paths for the top level nodes of the graph
    step 1: find top level nodes
    step 2: find all paths for each top level node
    :param user_dag:
    :return: prints paths
    """
    # # reset the global variable all_paths to empty
    # all_paths = []
    all_values = []

    # get all child nodes in graph
    for key, value in user_dag.items():
        for val in value:
            all_values.append(val)
    child_nodes = list(set(all_values))

    for node in user_dag:
        # test if node is a root node, else skip
        if node not in child_nodes:
            find_all_paths(user_dag, [node])

    if all_paths:
        for path in all_paths:
            print_path(path)


def print_path(path):
    if path:
        print(' >> '.join(map(str, path)))


def build_dag():
    """
    Builds a Directed Acyclic Graph based on user input
    Args:
        STDIN
        Expects STDIN first input to be number of nodes in graph 1- N, where N is number of nodes
        Each line in the next set of STDINs will be recorded as start and end nodes in graph : a,b
        Example  input:
        7
        0,1
        0,2
        1,3
        1,5
        2,5
        6,2
    :return: DAG as a dict
    """
    nodes_in_graph = int(input())
    user_dag = {}
    nodes = []
    for entry in range(1, nodes_in_graph):
        path = input()
        if path:
            path_values = path.split(",")
            start_node = int(path_values[0].strip())
            end_node = int(path_values[1].strip())

            if start_node not in nodes:
                nodes.append(start_node)

            if end_node not in nodes:
                nodes.append(end_node)

            if start_node in user_dag:
                user_dag[start_node].append(end_node)
            else:
                user_dag[start_node] = [end_node]
    for i in range(0,nodes_in_graph):
        if i not in nodes:
            user_dag[i] = []
    print("Generated a DAG stored as dict :>> \n {}".format(user_dag))
    return user_dag


if __name__== "__main__":
    user_intructions = "First Enter number of nodes in graph \n" \
                       "Then enter the graph nodes, with 'start_node, end_node' \n" \
        "Example  input: \n" \
        "7 \n"  \
        "0,1 \n"  \
        "0,2 \n"  \
        "1,3 \n"  \
        "1,5 \n"  \
        "2,5 \n"  \
        "6,2 \n"  \
        "================="
    print(user_intructions)
    user_dag = build_dag()
    get_all_paths(user_dag)



