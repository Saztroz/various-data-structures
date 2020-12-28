class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_position(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            print('Position is greater than one inputed')
            return

        prev.next = cur_node.next
        cur_node = None

    def insert_at_pos(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        cur_node = self.head
        count = 0
        prev = None

        while count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        new_node.next = cur_node
        prev.next = new_node

    def is_cycle(self):
        cur_node = self.head
        while cur_node:
            return True
        return False

    def reverse_list(self):
        cur_node = self.head
        prev = None
        while cur_node:
            next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next
        self.head = prev

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        prev_1 = None
        cur_1 = self.head

        while cur_1 and cur_1.data != key1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head

        while cur_2 and cur_2.data != key2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next


linked_list = LinkedList()
linked_list = LinkedList()
#linked_list.delete_node_at_position(2)
#linked_list.insert_at_pos(1, "E")
#linked_list.append('C')
linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.append('D')
linked_list.swap_nodes("A", "B")
linked_list.print_list()
