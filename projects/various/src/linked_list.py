class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node([{self.data}])"

    __repr__ = __str__


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @property
    def is_empty(self):
        return not self.head

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        if not isinstance(node, Node):
            raise TypeError("You must provide a Node object")

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def search(self, data, start_node=None):
        if start_node and not isinstance(start_node, Node):
            raise TypeError("You must provide a Node object or None.")

        current = self.head if not start_node else start_node
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def search_all(self, data):
        res = []
        current = self.head
        while current:
            if current.data == data:
                res += [current]
            current = current.next
        return res

    def remove_head(self):
        if not self.head:
            return

        node = self.head
        if node is self.tail:
            node.data = None
            node.next = None
            self.head = self.tail = None
            return

        self.head = self.head.next
        self.size -= 1

    def remove_tail(self):
        if not self.tail:
            return

        self.remove(self.tail)

    def remove(self, node):
        if not isinstance(node, Node):
            raise TypeError("You must provide a Node object")

        if node is self.head:
            self.remove_head()
            return

        previous = None
        current = self.head
        while current.next:
            previous = current
            current = current.next
            if current is node:
                previous.next = current.next
                break

        if current is self.tail:
            self.tail = previous

        self.size -= 1

    def reverse(self):
        previous = None
        current = self.tail = self.head
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        self.head = previous
        return self

    def count_nodes(self, start_node=None):
        if start_node and not isinstance(start_node, Node):
            raise TypeError("You must provide a Node object or None.")

        if self.is_empty:
            return 0

        count = 1
        current = self.head if not start_node else start_node
        while current.next:
            current = current.next
            count += 1
        return count

    def to_list(self):
        if not self.head:
            return []

        list_ = [self.head.data]
        current = self.head
        while current.next:
            list_ += [current.next.data]
            current = current.next
        return list_

    def from_list(self, list_):
        if not list_:
            return

        current = head = Node(list_[0])
        for i in range(1, len(list_)):
            next_ = Node(list_[i])
            current.next = next_
            current = current.next
        self.head = head
        self.tail = current
        self.size = len(list_)

    def __len__(self):
        if self.is_empty:
            return 0
        return self.size

    def __str__(self):
        str_ = ', '.join(str(node) for node in self.__class__.to_list(self))
        return f"LinkedList([{str_}])"

    __repr__ = __str__
