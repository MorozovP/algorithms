# 12 I. Ограниченная очередь

class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size_of = 0

    def is_empty(self):
        return self.size_of == 0

    def push(self, x):
        if self.size_of != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size_of += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            print(None)
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size_of -= 1
            print(x)

    def peek(self):
        if self.is_empty():
            print(None)
        else:
            x = self.queue[self.head]
            print(x)

    def size(self):
        x = self.size_of
        print(x)


def main() -> None:
    n = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    queue_methods = {
    'push': queue.push,
    'pop': queue.pop,
    'peek': queue.peek,
    'size': queue.size
    }

    for _ in range(n):
        data = input().split()
        if len(data) > 1:
            method = data[0]
            arg = int(data[1])

            queue_methods[method](arg)
        else:
            method = data[0]
            queue_methods[method]()


if __name__ == '__main__':
    main()
