"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# class Stack:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.next = next

#     def __len__(self):
#         return 0 if self.is_empty() else len(self.list)

#     def push(self, value):
#         return self.list.append(value)

#     def pop(self):
#         if self.__len__() > 0:
#             return self.list.pop()


"""
3) The difference is that a with a linked list 
you would have to loop through the list to 
find the tail when adding or deleting from the stack
"""


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.list = []

    def is_empty(self):
        self.list == []

    def __len__(self):
        return 0 if self.is_empty() else len(self.list)

    def push(self, value):
        return self.list.append(value)

    def pop(self):
        if self.__len__() > 0:
            return self.list.pop()
