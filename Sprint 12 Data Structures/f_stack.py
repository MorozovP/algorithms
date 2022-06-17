# 12 F. Стек - Max

class StackMax():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')


def main() -> None:
    stack = StackMax()
    stack_methods = {
        'push': StackMax.push,
        'pop': StackMax.pop,
        'get_max': StackMax.get_max
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
