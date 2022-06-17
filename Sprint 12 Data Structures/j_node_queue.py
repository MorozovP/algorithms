# 12 J. Списочная очередь

# Comment it before submitting
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get(node):
    if not node.next:
        print('error')
    else:
        next_node = node.next
        x = next_node.value
        node.next = next_node.next
        print(x)


def put(node, x):
    if not node.next:
        node.next = Node(x)
    else:
        while node.next:
            node = node.next
        node.next = Node(x)


def size(node):
    idx = 0
    while node.next:
        idx += 1
        node = node.next
    print(idx)


def main() -> None:
    n = int(input())
    node = Node(0)
    node_queue_methods = {
        'get': get,
        'put': put,
        'size': size
    }

    for _ in range(n):
        data = input().split()
        if len(data) > 1:
            method = data[0]
            arg = int(data[1])

            node_queue_methods[method](node, arg)
        else:
            method = data[0]
            node_queue_methods[method](node)


if __name__ == '__main__':
    main()
