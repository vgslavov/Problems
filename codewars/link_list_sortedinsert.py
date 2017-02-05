# mine
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)

    # empty list
    if not head:
        return new_node

    # head of list
    if data < head.data:
        new_node.next = head
        return new_node

    ptr = head
    while ptr:
        # tail of list
        if not ptr.next:
            ptr.next = new_node
            return head
        elif data >= ptr.data and data < ptr.next.data:
            new_node.next = ptr.next
            ptr.next = new_node
            return head
        else:
            ptr = ptr.next

    # not reached
    return head

# others
class Node(object):
  def __init__(self, data, nxt = None):
    self.data = data
    self.next = nxt

def sorted_insert(head, data):
  if not head or data < head.data: return Node(data, head)
  else:
    head.next = sorted_insert(head.next, data)
    return head
