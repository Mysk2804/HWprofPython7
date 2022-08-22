class Stack():
    def __init__(self):
        self.stack = []

    def isempty(self):
        if len(self.stack) == 0:
            return False
        return True

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack[-1]
        return removed

    def size(self):
        return len(self.stack)


def tru_list(item):
    len_list = Stack()
    flveru = True

    for i in item:
        if i in "({[":
            len_list.push(i)
        elif i in ")]}":
            if len(len_list.stack) == 0:
                flveru = False
                break

            b = len_list.pop()
            if b == '(' and i == ')':
                continue
            if b == '[' and i == ']':
                continue
            if b == '{' and i == '}':
                continue
            flveru = False
            break

    if flveru and len(len_list.stack) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    len_list = Stack()
    item_1 = '(((([{}]))))'
    item_2 = '[([])((([[[]]])))]{()}'
    item_3 = '{{[()]}}'
    item_4 = '}{}'
    item_5 = '{{[(])]}}'
    item_6 = '[[{())}]'
    tru_list(item_1)
    tru_list(item_2)
    tru_list(item_3)
    tru_list(item_4)
    tru_list(item_5)
    tru_list(item_6)
