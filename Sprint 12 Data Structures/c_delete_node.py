# 12 C. Нелюбимое дело

# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    def get_node_by_index(node, index):
        while index:
                node = node.next_item
                index -= 1
        return node
    head = node
    if idx == 0:
        head = node.next_item
        return head
    prev_node = get_node_by_index(node, idx-1)
    del_node = prev_node.next_item
    prev_node.next_item = del_node.next_item
    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 2)
    return new_head


def print_linked_list(vertex):
        while vertex:
                print(vertex.value, end=" -> ")
                vertex = vertex.next_item
        print("None")


print_linked_list(test())
