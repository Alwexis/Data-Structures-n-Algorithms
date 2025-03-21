class Node:
    def __init__(self, value):
        self.value = value
        self.left_sibling = None
        self.right_sibling = None
    
class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def add_children(self, n1: Node, n2: Node, side: str):
        if not self.root:
            self.root = n1
        if side == "left":
            n1.left_sibling = n2
        elif side == "right":
            n1.right_sibling = n2
    
    def loop_inorder(self, nodo: Node):
        if nodo is not None:
            # Recorremos el izquierdo
            self.loop_inorder(nodo.left_sibling)
            print(nodo.value, end = ' ')
            self.loop_inorder(nodo.right_sibling)
    
    def loop_preorder(self, nodo: Node):
        if nodo is not None:
            print(nodo.value, end = ' ')
            self.loop_preorder(nodo.left_sibling)
            self.loop_preorder(nodo.right_sibling)
    
    def loop_postorder(self, nodo: Node):
        if nodo is not None:
            self.loop_postorder(nodo.left_sibling)
            self.loop_postorder(nodo.right_sibling)
            print(nodo.value, end = ' ')
    
    def count_nodes(self, actual: Node = None, count = 0):
        if actual == None:
            return 0
        left_nodes = self.count_nodes(actual.left_sibling)
        right_nodes = self.count_nodes(actual.right_sibling)
        return left_nodes + right_nodes + 1 # + 1 por el actual
    
    def count_height(self, actual: Node = None):
        if actual == None:
            return 0
        return 1 + max(self.count_height(actual.left_sibling), self.count_height(actual.right_sibling))
    
    def search(self, nodo: Node, value):
        if self.root is None:
            return False
        if nodo.value == value:
            return nodo
        return self.search(nodo.left_sibling, value) or self.search(nodo.right_sibling, value)

    def count_leafs(self, nodo: Node, leafs = None):
        if leafs is None:
            leafs = []
        if nodo is None:
            return leafs
        # Esto quiere decir que es una Hoja pues, no tiene mas "hijos"
        if nodo.left_sibling is None and nodo.right_sibling is None:
            leafs.append(nodo.value)
        # Hacemos llamada recursiva con las demas hojas. En caso de que alguna sea None, no importa, devolverá una lista vacía.
        self.count_leafs(nodo.left_sibling, leafs)
        self.count_leafs(nodo.right_sibling, leafs)
        return leafs
    
    def compare(self, nodo1: Node, nodo2: Node):
        if nodo1 is None and nodo2 is None:
            return True
        elif nodo1 is None or nodo2 is None:
            return False
        elif nodo1.value != nodo2.value:
            return False
        return self.compare(nodo1.left_sibling, nodo2.left_sibling) and self.compare(nodo1.right_sibling, nodo2.right_sibling)

    def invert(self, nodo: Node):
        if nodo is None:
            return
        # Invertimos los nodos. Cambiamos el valor del nodo left al right y viceversa.
        nodo.left_sibling, nodo.right_sibling = nodo.right_sibling, nodo.left_sibling
        self.invert(nodo.left_sibling)
        self.invert(nodo.right_sibling)