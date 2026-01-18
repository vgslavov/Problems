# mine
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_sort(head):
    if not head or not head.next:
        return head

    sorted_list = None
    while head:
        sorted_list = sorted_insert(sorted_list, head.data)
        head = head.next

    return sorted_list

# others
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def insert_sort(head):
    n, r = head, None
    while n:
        r = sorted_insert(r, n.data)
        n = n.next
    return r
