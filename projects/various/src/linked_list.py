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

    @property
    def is_empty(self):
        return not self.head

    def clear(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not isinstance(node, Node):
            raise TypeError("You must provide a Node object")

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def find(self, data, start_node=None):
        current = self.head if not start_node else start_node
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def find_all(self, data):
        res = []
        current = self.head
        while current:
            if current.data == data:
                res += [current]
            current = current.next
        return res

    def remove_head(self):
        node = self.head
        if node is self.tail:
            node.data = None
            node.next = None
            self.head = self.tail = None
            return

        self.head = self.head.next

    def remove_tail(self):
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
            raise TypeError("You must provide a Node object")

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

    def __len__(self):
        if self.is_empty:
            return 0
        return self.count_nodes()

    def __str__(self):
        str_ = ', '.join(str(node) for node in self.__class__.to_list(self))
        return f"LinkedList([{str_}])"

    __repr__ = __str__


def main():
    nums = LinkedList()
    nums.from_list([1, 3, 5, 7, 9])
    print(f"\nCreate Linked List: {nums}\n"
          f"count: {len(nums)}")

    nums.reverse()
    print(f"\nReverse: {nums}\n"
          f"count: {len(nums)}")

    nums.reverse()
    print(f"\nReverse: {nums}\n"
          f"count: {len(nums)}")

    nums.append(Node(11))
    print(f"\nAppend 11: {nums}\n"
          f"count: {len(nums)}")

    nums.append(Node(13))
    print(f"\nAppend 13: {nums}\n"
          f"count: {len(nums)}")

    nums.remove(nums.head.next.next)
    print(f"\nRemove 3rt node: {nums}\n"
          f"count: {len(nums)}")

    nums.remove(nums.head)
    print(f"\nRemove head: {nums}\n"
          f"count: {len(nums)}")

    nums.remove_head()
    print(f"\nRemove head: {nums}\n"
          f"count: {len(nums)}")

    nums.remove_tail()
    print(f"\nRemove tail: {nums}\n"
          f"count: {len(nums)}")

    nums.remove(nums.head)
    print(f"\nRemove head: {nums}\n"
          f"count: {len(nums)}")

    nums.remove(nums.head)
    print(f"\nRemove head: {nums}\n"
          f"count: {len(nums)}")

    nums.remove(nums.head)
    print(f"\nRemove head: {nums}\n"
          f"count: {len(nums)}")


if __name__ == '__main__':
    main()
