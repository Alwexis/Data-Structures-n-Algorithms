# Definición de "colores"
RED = 'RED'
BLACK = 'BLACK'

class RBNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.TNULL = RBNode(0, color=BLACK)  # Nodo nulo (hoja)
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        # Crear el nuevo nodo
        node = RBNode(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = RED  # Se inserta como rojo
        y = None
        x = self.root

        # Búsqueda de la posición de inserción
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node  # El árbol estaba vacío
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # Si el nodo es la raíz, se marca como negro
        if node.parent is None:
            node.color = BLACK
            return

        # Si el abuelo es nulo, no es necesario arreglar
        if node.parent.parent is None:
            return

        # Arregla las propiedades del árbol
        self.insert_fixup(node)

    def insert_fixup(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right  # Tío de k
                if u.color == RED:
                    # Caso 1: recoloreado
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Caso 2: rotación izquierda
                        k = k.parent
                        self.left_rotate(k)
                    # Caso 3: rotación derecha
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left  # Tío de k (caso simétrico)
                if u.color == RED:
                    # Caso 1
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Caso 2
                        k = k.parent
                        self.right_rotate(k)
                    # Caso 3
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = BLACK

    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            print(f'{node.key}({node.color})', end=" ")
            self.in_order_helper(node.right)

    def in_order(self):
        self.in_order_helper(self.root)
        print()

# Ejemplo de uso
rbt = RBTree()
elements = [20, 15, 25, 10, 5, 1]
for elem in elements:
    rbt.insert(elem)

print("Recorrido in-order del Árbol Red-Black:")
rbt.in_order()