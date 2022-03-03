class Node:
    def __init__(self, name):
        self.name = name
        self.adjencency_list = []
        self.isVisited = False


### iteration

def DepthFirstSearch(start_node: Node) -> None:
    stack = [start_node]
    while stack:
        actual_node = stack.pop()
        print(actual_node.name)
        actual_node.isVisited = True
        for node in actual_node.adjencency_list:
            if not node.isVisited:
                stack.append(node)


### recursion
def dfs(stack: list) -> None:

    while stack:
        actual_node = stack.pop()
        print(actual_node.name)
        actual_node.isVisited = True
        for node in actual_node.adjencency_list:
            if not node.isVisited:
                stack.append(node)
        return dfs(stack)




def dfs_node(start_node: Node) -> None:
    print(start_node.name)
    start_node.isVisited = True
    for node in start_node.adjencency_list:
        if not node.isVisited:
            dfs_node(node)



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjencency_list.append(node2)
node1.adjencency_list.append(node3)
node2.adjencency_list.append(node4)

#print(DepthFirstSearch(node1))
print(dfs_node(node1))
vars(node1)