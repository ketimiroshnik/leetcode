# 146. LRU Cache


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


def show(head):
    print("printing list")
    node = head
    while node is not None:
        print(f"({node.key} {node.value}), prev = {None if node.prev is None else node.prev.key}, "
              f"next = {None if node.next is None else node.next.key}")
        print(node.key, node.value)
        node = node.next




class LRUCache(object):

    def __init__(self, capacity):
        """
                :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.d = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # наиболее используемый около головы, самый старый - около хвоста

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def remove_from_tail(self):
        node = self.tail.prev
        prev_node = node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        del self.d[node.key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            node = self.d[key]
            self.remove_node(node)
            self.add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            node = self.d[key]
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)
            return

        if self.size >= self.capacity:
            # нужно вытеснить
            self.remove_from_tail()
            self.size -= 1

        self.size += 1
        node = Node(key, value)
        self.add_to_head(node)
        self.d[key] = node




lru = LRUCache(2)
print(lru.put(1, 1)) # cache is {1=1}
print()
print(lru.put(2, 2)) # cache is {1=1, 2=2}
print()
print(lru.get(1))    # return 1
print()
print(lru.put(3, 3)) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lru.get(2) )   # returns -1 (not found)
print(lru.put(4, 4)) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lru.get(1))    # return -1 (not found)
print(lru.get(3))    # return 3
print(lru.get(4))    # return 4