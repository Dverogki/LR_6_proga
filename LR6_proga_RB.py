class RBNode:
    def __init__(self, key, color='R'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

class RBTree:
    def __init__(self):
        self.NIL = RBNode(None, 'B')
        self.root = self.NIL

    def _rotate_left(self, node):
        child = node.right
        node.right = child.left
        if child.left != self.NIL:
            child.left.parent = node
        child.parent = node.parent
        if node.parent == self.NIL:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.left = node
        node.parent = child

    def _rotate_right(self, node):
        child = node.left
        node.left = child.right
        if child.right != self.NIL:
            child.right.parent = node
        child.parent = node.parent
        if node.parent == self.NIL:
            self.root = child
        elif node == node.parent.right:
            node.parent.right = child
        else:
            node.parent.left = child
        child.right = node
        node.parent = child

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = self.NIL
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent == self.NIL:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'R'
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._rotate_left(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 'B'

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        if node == self.NIL:
            print("  " * level + prefix + "NIL (B)")
            return

        print("  " * level + prefix + str(node.key) + " (" + node.color + ")")

        if node.left != self.NIL or node.right != self.NIL:
            self.print_tree(node.left, level + 1, "L - ")
            self.print_tree(node.right, level + 1, "R - ")
        else:
            self.print_tree(node.left, level + 1, "L - ")
            self.print_tree(node.right, level + 1, "R - ")


rbt = RBTree()
numbers = [5, 3, 7, 2, 4, 6, 8]

print("Числа:", numbers)
for num in numbers:
    rbt.insert(num)

print("\nКрасно-черное дерево:")
rbt.print_tree()