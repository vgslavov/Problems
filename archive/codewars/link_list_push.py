# mine
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    list = None
    list = push(list, 3)
    list = push(list, 2)
    list = push(list, 1)
    return list

# others
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    return Node(data, head)

def build_one_two_three():
    return Node(1, Node(2, Node(3)))
    # or
    return push(push(Node(3), 2), 1)
