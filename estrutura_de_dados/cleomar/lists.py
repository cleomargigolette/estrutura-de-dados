class Stack:
    list = []

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def push(self, new_atribute):
        self.list.append(new_atribute)
        return new_atribute

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            atribute_remove  = self.list[-1]
            del(self.list[-1])
            return atribute_remove
stack = Stack()      

class Queue:
    list = []

    def tail_queue(self):
        return self.list[-1]

    def head_queue(self):
        return self.list[0]    

    def enqueue(self, new_atribute):
        self.list.append(new_atribute)
        return new_atribute

    def dequeue(self):
        atribute_remove = self.list[0]
        del(self.list[0])
        return atribute_remove

    def clear_queue(self):
        return self.list.clear()  

    def is_empty(self):
        return len(self.list) == 0  

if __name__ == "__main__":
    stack = Stack()
    stack.push("teste1")
    stack.push("teste2")
    stack.push("teste3")
    stack.push("teste4")
    
    for atribute in stack.list:
        print(atribute)
        print("O top é: " + str(stack.top()))
        stack.pop()

    queue = Queue()
    queue.enqueue("teste1")
    queue.enqueue("teste2")
    queue.enqueue("teste3")
    queue.enqueue("teste4")
    queue.enqueue("teste5")
    queue.enqueue("teste6")
    queue.enqueue("teste7")
    queue.enqueue("teste8")
    queue.enqueue("teste9")
    queue.enqueue("teste10")
    queue.enqueue("teste11")

    for atribute in queue.list:
        print(atribute)
        print("O head é: " + str(queue.head_queue()))
        print("O tail é: " + str(queue.tail_queue()))
        queue.dequeue()  