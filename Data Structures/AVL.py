class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # La altura de un nodo recién creado es 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Realiza la rotación
        y.right = z
        z.left = T3

        # Actualiza alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        # Retorna la nueva raíz
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Realiza la rotación
        y.left = z
        z.right = T2

        # Actualiza alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def _insert(self, node, key):
        # Inserción normal en BST
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        
        # Actualiza la altura del nodo actual
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        # Calcula el factor de balance
        balance = self.get_balance(node)
        
        # Caso Left Left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        
        # Caso Right Right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        
        # Caso Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Caso Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def pre_order(self):
        self._pre_order(self.root)
        print()

    def _pre_order(self, node):
        if not node:
            return
        print(node.key, end=" ")
        self._pre_order(node.left)
        self._pre_order(node.right)


tree = AVLTree()
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    tree.insert(key)

print("Recorrido pre-orden del árbol AVL:")
tree.pre_order()