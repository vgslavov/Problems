# mine
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_nth(head, index, data):
    new_node = Node(data)
    if not head:
        return new_node

    if not index:
        new_node.next = head
        return new_node

    i = 0
    ptr = head
    while ptr:
        if i == index - 1:
            new_node.next = ptr.next
            ptr.next = new_node
            return head
        ptr = ptr.next
        i += 1

    raise IndexError

# others
class Node(object):
    def __init__(self, data, nxt = None):
        self.data = data
        self.next = nxt

def insert_nth(head, index, data):
  if index == 0: return Node(data, head)
  if head and index > 0:
    head.next = insert_nth(head.next, index - 1, data)
    return head
  raise ValueError
