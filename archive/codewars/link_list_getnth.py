# mine
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth(node, index):
    idx = 0
    while node:
        if idx == index:
                return node
        node = node.next
        idx += 1
    raise Exception("Invalid index")

# others
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def get_nth(node, index):
  if node and index >= 0: return node if index < 1 else get_nth(node.next, index - 1)
  raise ValueError

def get_nth(node, index, i=0):
    if node is None:
        raise IndexError
    else:
        return node if index == i else get_nth(node.next, index, i + 1)
