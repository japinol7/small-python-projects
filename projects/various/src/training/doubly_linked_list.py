APP_NAME = 'Doubly Linked List'
APP_VERSION = '0_01_0'


class _Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def get_first(self):
        return self._head.data

    @property
    def get_last(self):
        return self._tail.data

    def is_empty(self):
        return self._size < 1

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.data
            node = node.next

    def to_list(self):
        if self.is_empty():
            return []

        node = self._head
        list_ = []
        while node is not None:
            list_.append(node.data)
            node = node.next

        return list_

    def _add_first_node(self, node):
        self._head = node
        self._tail = node
        node.prev = None
        node.next = None
        self._size += 1

    def add_first(self, data):
        node = _Node(data)

        if self.is_empty():
            self._add_first_node(node)
            return

        head_old = self._head
        self._head = node
        node.prev = None
        node.next = head_old
        head_old.prev = node

        self._size += 1

    def add_last(self, data):
        node = _Node(data)

        if self.is_empty():
            self._add_first_node(node)
            return

        tail_old = self._tail
        self._tail = node
        node.prev = tail_old
        node.next = None
        tail_old.next = node

        self._size += 1

    def _find_node(self, data):
        if self.is_empty():
            return None

        node = self._head
        while node is not None:
            if node.data == data:
                return node
            node = node.next

        return None

    def exist(self, data):
        return True if self._find_node(data) else False

    def _insert_node_between_nodes(self, node, node_prev, node_next):
        node.prev = node_prev
        node.next = node_next
        node_prev.next = node
        node_next.prev = node
        self._size += 1

    def add_before(self, data, data_next):
        node = _Node(data)

        if self.is_empty():
            self._add_first_node(node)
            return

        node_next = self._find_node(data_next)
        node_prev = node_next.prev

        self._insert_node_between_nodes(node, node_prev, node_next)

    def add_after(self, data, data_prev):
        node = _Node(data)

        if self.is_empty():
            self._add_first_node(node)
            return

        node_prev = self._find_node(data_prev)
        node_next = node_prev.next

        self._insert_node_between_nodes(node, node_prev, node_next)

    def remove(self, data):
        node = self._find_node(data)

        if not node:
            raise Exception(f"Item not found: {data}")

        if self._size == 1:
            self._head = self._tail = None
            self._size = 0
            return

        if node == self._head:
            self._head = self._head.next
            self._head.prev = None
            self._size -= 1
            return

        if node == self._tail:
            self._tail = self._tail.prev
            self._tail.next = None
            self._size -= 1
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def pop_first(self):
        res = self._head.data
        self.remove(self._head.data)
        return res

    def pop_last(self):
        res = self._tail.data
        self.remove(self._tail.data)
        return res


def main():
    print(f"-- Start program {APP_NAME} {APP_VERSION} --")

    print("\n-- Add items at the end from 10 to 150 in steps of 10")
    linked_list = LinkedList()
    for i in range(10, 160, 10):
        linked_list.add_last(i)

    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130,
        140, 150]
    assert linked_list.size == 15
    assert linked_list.get_first == 10
    assert linked_list.get_last == 150

    print("\n-- Add items at the start: 7, 5")
    for i in [7, 5]:
        linked_list.add_first(i)

    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        5, 7, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,
        120, 130, 140, 150]
    assert linked_list.size == 17
    assert linked_list.get_first == 5
    assert linked_list.get_last == 150

    print("\n-- Add items after 80: 87, 85")
    for i in [87, 85]:
        linked_list.add_after(i, data_prev=80)

    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        5, 7, 10, 20, 30, 40, 50, 60, 70, 80, 85, 87, 90, 100, 110,
        120, 130, 140, 150]
    assert linked_list.size == 19

    print("\n-- Add items before 50: 45, 47")
    for i in [45, 47]:
        linked_list.add_before(i, data_next=50)

    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        5, 7, 10, 20, 30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100,
        110, 120, 130, 140, 150]
    assert linked_list.size == 21

    print("\n-- Exists item 100 should be True:  --> ", end='')
    res = linked_list.exist(100)
    print(res)
    assert linked_list.exist(100) is True

    print("\n-- Exists first item 5 should be True: --> ", end='')
    res = linked_list.exist(5)
    print(res)
    assert linked_list.exist(5) is True

    print("\n-- Exists last item 150 should be True: --> ", end='')
    res = linked_list.exist(150)
    print(res)
    assert linked_list.exist(150) is True

    print("\n-- Exists item 105 should be False: --> ", end='')
    res = linked_list.exist(105)
    print(res)
    assert linked_list.exist(105) is False

    print("\n-- Check iteration: ")
    iter_list = [i for i in linked_list]
    print(iter_list)
    assert iter_list == linked_list.to_list()

    print("\n-- Remove item 20")
    linked_list.remove(20)
    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        5, 7, 10, 30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100,
        110, 120, 130, 140, 150]
    assert linked_list.size == 20

    print("\n-- Remove second item 7")
    linked_list.remove(7)
    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        5, 10, 30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100, 110,
        120, 130, 140, 150]
    assert linked_list.size == 19

    print("\n-- Remove first item 5")
    linked_list.remove(5)
    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        10, 30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100, 110,
        120, 130, 140, 150]
    assert linked_list.size == 18

    print("\n-- Remove pre-last item 140")
    linked_list.remove(140)
    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        10, 30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100, 110,
        120, 130, 150]
    assert linked_list.size == 17

    print("\n-- Remove last item 150")
    linked_list.remove(150)
    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        10, 30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100, 110,
        120, 130]
    assert linked_list.size == 16

    print("\n-- Pop first item")
    item = linked_list.pop_first()
    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100, 110,
        120, 130]
    assert item == 10
    assert linked_list.size == 15
    assert linked_list.get_first == 30
    assert linked_list.get_last == 130

    print("\n-- Pop last item")
    item = linked_list.pop_last()
    list_ = linked_list.to_list()
    print(list_)
    assert list_ == [
        30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100, 110, 120]
    assert item == 130
    assert linked_list.size == 14
    assert linked_list.get_first == 30
    assert linked_list.get_last == 120

    print("\n-- Remove all the remaining items")
    for i in [30, 40, 45, 47, 50, 60, 70, 80, 85, 87, 90, 100, 110, 120]:
        linked_list.remove(i)
    print(linked_list.to_list())
    assert linked_list.is_empty() is True
    assert linked_list.to_list() == []
    assert linked_list.size == 0

    print("\n-- Check iteration over an empty linked list: ")
    iter_list = [i for i in linked_list]
    print(iter_list)
    assert iter_list == []

    print(f"\n-- End of program {APP_NAME} {APP_VERSION} --\n")


if __name__ == '__main__':
    main()
