class Stack:
    def __init__(self, limit):
        self.st = []
        self.lim = limit

    def push(self, x):
        if len(self.st) >= self.lim:
            print("Stack is full")
            return -1
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            print("Stack is empty")
            return -1
        return self.st.pop()

    def peek(self):
        if len(self.st) == 0:
            print("Stack is empty")
            return -1
        return self.st[-1]

    def find(self, x):
        # Search from top (reverse order)
        for i in range(len(self.st) - 1, -1, -1):
            if self.st[i] == x:
                print(f"Found {x} at index {i} (from top)")
                return
        print("Not found")

    def find1(self, x):
        # print all indices
        for i in range(len(self.st)):
            print(i)
        return

    def find2(self, x):
        lst = []
        for i in range(len(self.st)):
            if self.st[i] == x:
                print(i)
                lst.append(i)
        if len(lst) == 0:
            print("Not found")
            return
        mid_index = len(lst) // 2
        return self.st[lst[mid_index]]

    def replace(self, x, y):
        for i in range(len(self.st)):
            if self.st[i] == x:
                self.st[i] = y
                print(f"Replaced {x} with {y} at index {i}")
