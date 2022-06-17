# 12 G. Стек - MaxEffective

class StackMaxEffective():
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            last_max = self.items[-1][1]
            if last_max > item:
                self.items.append((item, last_max))
            else:
                self.items.append((item, item))
        else:
            self.items.append((item, item))

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(self.items[-1][1])
        else:
            print('None')


def main() -> None:
    stack = StackMaxEffective()
    stack_methods = {
        'push': StackMaxEffective.push,
        'pop': StackMaxEffective.pop,
        'get_max': StackMaxEffective.get_max
    }
    n = int(input())
    for _ in range(n):
        data = input().split()
        if len(data) > 1:
            method = data[0]
            arg = int(data[1])
            stack_methods[method](stack, arg)
        else:
            method = data[0]
            stack_methods[method](stack)


if __name__ == '__main__':
    main()
