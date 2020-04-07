class Stack:
    def __init__(self):
        self.content = []

    def isEmpty(self):
        if len(self.content):
            return False
        else:
            return True

    def size(self):
        return len(self.content)

    def push(self, value):
        self.content.append(value)

    def peek(self):
        if len(self.content) > 0:
            return self.content[-1]
        else:
            return None

    def pop(self):
        return self.content.pop(-1)


def check_bracets(string):
    st = Stack()
    error = False
    brackets = {")": "(", "]": "[", "}": "{"}
    for item in string:
        if item in (list(brackets.values())):
            st.push(item)
        else:
            if item in (list(brackets.keys())) and brackets[item] == st.peek():
                st.pop()
            else:
                error = True
                break
    if st.isEmpty() and not error:
        print("Сбалансированно")
    else:
        print("Небалансированно")


if __name__ == "__main__":
    string = input("Введите строку: ")
    print(check_bracets(string))