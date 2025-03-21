class LinkedListItem:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item: LinkedListItem):
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item
    
    def search(self, value):
        actual = self.head
        while actual:
            if actual.value == value:
                return actual
            actual = actual.next
        return None
    
    def delete_duplicates(self):
        actual = self.head
        while actual:
            runner = actual.next
            while runner:
                if runner.value == actual.value:
                    # Guardamos el siguiente nodo antes de eliminar
                    next_node = runner.next
                    # Ajustamos el puntero del nodo anterior
                    if runner.prev:
                        runner.prev.next = runner.next
                    # Ajustamos el puntero prev del nodo siguiente, si existe
                    if runner.next:
                        runner.next.prev = runner.prev
                    # Si runner es la cola, actualizamos self.tail
                    if runner == self.tail:
                        self.tail = runner.prev
                    runner = next_node
                else:
                    runner = runner.next
            actual = actual.next

    def print(self):
        if self.head is None:
            print("No hay elementos en la lista enlazada")
            return
        actual = self.head
        while actual:
            print(actual.value)
            actual = actual.next

linked = LinkedList()
items = [LinkedListItem("Ariel"),
 LinkedListItem("Jenniffer"),
 LinkedListItem("Jano"),
 LinkedListItem("Kevin"),
 LinkedListItem("Mattias"),
 LinkedListItem("Ariel")]
for item in items:
    linked.append(item)
linked.print()