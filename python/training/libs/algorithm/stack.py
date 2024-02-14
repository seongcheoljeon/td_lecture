import typing


class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, data) -> None:
        if self.top is None:
            self.top = Stack.Node(data)
        else:
            node = Stack.Node(data)
            node.next = self.top
            self.top = node

    def pop(self) -> typing.Any:
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self) -> typing.Any:
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None

