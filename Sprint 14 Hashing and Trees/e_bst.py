# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    res = []

    def lmr(root, res):
        if root.left != None:
            lmr(root.left, res)
        if res and root.value <= res[-1]:
            res.append(None)
        res.append(root.value)
        if root.right != None:
            lmr(root.right, res)
        return None not in res
    return lmr(root, res)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)