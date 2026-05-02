class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0
def update_height(node):
    if node:
        node.height = max(height(node.left), height(node.right)) + 1
def rotate_right(k2):
    k1 = k2.left
    k2.left = k1.right
    k1.right = k2

    update_height(k2)
    update_height(k1)
    return k1
def rotate_left(k1):
    k2 = k1.right
    k1.right = k2.left
    k2.left = k1

    update_height(k1)
    update_height(k2)
    return k2
def double_rotate_left(k3):
    k3.left = rotate_left(k3.left)
    return rotate_right(k3)
def double_rotate_right(k3):
    k3.right = rotate_right(k3.right)
    return rotate_left(k3)

def insert(root, key):
    if root is None:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    update_height(root)

    balance = height(root.left) - height(root.right)

    if balance == 2:
        if key < root.left.key:
            return rotate_right(root)
        else:
            return double_rotate_left(root)

    if balance == -2:
        if key > root.right.key:
            return rotate_left(root)
        else:
            return double_rotate_right(root)

    return root


tree = None
for x in [4, 5, 7, 2, 1, 3, 6]:
    tree = insert(tree, x)

print('Дерево построено')

if tree:
    print(f"\nКорень: {tree.key}")
    if tree.left:
        print(f"Левый ребенок корня: {tree.left.key}")
    if tree.right:
        print(f"Правый ребенок корня: {tree.right.key}")

    print(f"\nВысота дерева: {tree.height}")
    print(f"Баланс корня: {height(tree.left) - height(tree.right)}")