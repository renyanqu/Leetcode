class Node:

    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        if data > node.data:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)


    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def get_max_value(self):
        if self.root:
            return self.get_max_node(self.root)
    def get_max_node(self, node):
        traverse_node = node
        while traverse_node.rightChild:
            traverse_node = traverse_node.rightChild
        return traverse_node.data

    def get_min_value(self):
        if self.root:
            return self.get_min_node(self.root)

    def get_min_node(self, node):
        traverse_node = node
        while traverse_node.leftChild:
            traverse_node = traverse_node.leftChild
        return traverse_node.data

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if data > node.data:
            self.remove_node(data, node.rightChild)

        elif data < node.data:
            self.remove_node(data, node.leftChild)

        else:
            ### found the data in this node!
            ### leaf node   1)
            parent = node.parent
            if node.rightChild is None and node.leftChild is None:
                print("removing a leaf node...{0}".format(node.data))
                if parent is None:
                    self.root = None
                if parent.leftChild and parent.leftChild == node:
                    parent.leftChild = None
                if parent.rightChild and parent.rightChild == node:
                    parent.rightChild = None
                del node
            ### single child node with leftchild 2)

            elif node.leftChild is not None and node.rightChild is None:
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild

                else:
                    self.root = node.leftChild
                node.leftChild.parent = None
                del node

            ### single child node with rightChild 3)
            elif node.rightChild is not None and node.leftChild is None:
                if parent is not None:
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                else:
                    self.root = node.rightChild
                self.root.parent = None
                del node

            ### node with two children node 4)
            else:
                print("removing node with two children".format(node.data))
                predecessor = self.get_predecessor(node.leftChild)
                predecessor.data, node.data = node.data, predecessor.data
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        predecessor = node.leftChild
        while predecessor.rightChild:
            predecessor = predecessor.rightChild
        return predecessor




    ### preorder and postorder are kept in the order of processing of ROOT element
    ### inorder: left -> root -> right
    ### preorder: process root first, root -> left - > right
    ### postorder: left - > right -> root
    def traverse_in_order(self, node):
        ### for each node, visit left node first, then node itself, next right node
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)


    def traverse_pre_order(self, node):
        ### for reach node, vist parent node first, then left child, next right child
        print(node.data)
        if node.leftChild:
            self.traverse_pre_order(node.leftChild)

        if node.rightChild:
            self.traverse_pre_order(node.rightChild)



    def traverse_post_order(self, node):
        ### left -> right -> root
        if node.leftChild:
            self.traverse_post_order(node.leftChild)

        if node.rightChild:
            self.traverse_post_order(node.rightChild)

        print(node.data)


















bst = BinarySearchTree()
bst.insert(18)
bst.insert(5)
bst.insert(30)
bst.insert(2)
bst.insert(38)

bst.traverse()
#bst.traverse_pre_order(bst.root)
#bst.traverse_post_order(bst.root)
print(bst.get_max_value())
print(bst.get_min_value())

bst.remove(2)
bst.traverse()


bst.remove(18)
bst.traverse()