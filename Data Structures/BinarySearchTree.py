class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        return self._insert(value, self.root)
    
    def _insert(self, value, actual: Node):
        if value < actual.value:
            if actual.left is None:
                actual.left = Node(value)
            else:
                self._insert(value, actual.left)
        else:
            if actual.right is None:
                actual.right = Node(value)
            else:
                self._insert(value, actual.right)
    
    def search(self, value):
        return self._search(value, self.root)
    
    def _search(self, value, actual: Node):
        if actual is None:
            return None
        if value == actual.value:
            return actual
        if value < actual.value:
            return self._search(value, actual.left)
        if value > actual.value:
            return self._search(value, actual.right)
        
    def delete(self, value):
        self._delete(value, self.root)
    
    def _delete(self, value, actual: Node):
        if actual is None:
            return
        
        if value < actual.value:
            actual.left = self._delete(value, actual.left)
        elif value > actual.value:
            actual.right = self._delete(value, actual.right)
        else:
            # Revisamos los casos. Primer caso nodo sin hijos o con uno solo.
            if actual.left is None:
                return actual.right
            elif actual.right is None:
                return actual.left
            
            # Caso 2: Nodo con Hijos
            temp = self._min_value_in_order(actual.right)
            actual.value = temp.value
            actual.right = self._delete(temp.value, actual.right)
        
    def _min_value_in_order(self, node: Node):
        current = node
        while current:
            current = current.left
        return current

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, actual: Node):
        if actual is None:
            return []
        return self._in_order(actual.left) + [actual.value] + self._in_order(actual.right)