from stack import Stack


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        
        while node is not None:
            next = node.next_node
            node.next = prev
            prev = node
            node = next
        self.head = prev
        
        # stack = Stack()
        
        # if self.head:
        #     if node is not None:
        #         self.head = prev
        #         self.reverse_list(node.next_node, node)

                

            # if node.next_node is not None:
            #     stack.push(node)
            #     self.reverse_list(node.next_node, node)
            # else:
            #     current = stack.pop()
            #     while current != starting_head:
            #         self.head = current
            #         prev.next_node = None
            #         current = prev
                # self.head = node
                # self.head.next_node = prev
            
# test = LinkedList()

# test.add_to_head(1)
# test.add_to_head(2)
# test.add_to_head(3)
# test.add_to_head(4)
# test.add_to_head(5)

# test.reverse_list(test.head, None)

# print(test.head.value)

# print(test.head.get_next().get_value)