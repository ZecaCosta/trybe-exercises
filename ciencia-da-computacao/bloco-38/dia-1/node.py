class Node:
    def __init__(self, value):
        self.value = value  # 🎲 Dado a ser armazenado
        print("Node | __init_ | value: ", self.value)

        self.next = None  # 👉 Forma de apontar para outro nó
        print("Node | __init_ | next: ", self.next)

    def __str__(self):
        return f"Node(value={self.value}, next={self.next})"
