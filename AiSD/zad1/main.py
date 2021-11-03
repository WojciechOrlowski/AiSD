class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    def node(self,data):
        a = self.head
        num = 0
        while (a!=None):
            if (num == data):
                return a.value
            num = num+1
            a = a.next

    def insert(self, prev_node, new_value):
        if prev_node is None:
            print ("Podany wcześniejszy node musi być w liście")
            return
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def pop(headRef):
        if headRef is None:
            return None
        result = headRef.value
        headRef = headRef.next
        print("Usunięta wartość: " + result)
        return headRef
    def remove_last(self):
        if(self.head !=None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next !=None):
                    temp = temp.next
                lastNode = temp.next
                result = lastNode.value
                temp.next = None
                lastNode = None
                print("Usunięta wartość: " + result)

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.value)
            temp = temp.next

    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            newnode = Node(value)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            return popnode.value


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.value)
            temp = temp.next

    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count


class Queue:
    def __init__(self):
        self.head = None
        self.last = None
    def peek(self):
        return self.head.value
    def enqueue(self, value):
        if self.last is None:
            self.head = Node(value)
            self.last = self.head
        else:
            self.last.next = Node(value)
            self.last.next.prev = self.last
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.value
            self.head = self.head.next
            self.head.prev=None
            return temp
    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.value)
            temp = temp.next


list_ = LinkedList()
stack = Stack()
queue = Queue()


list_.push(1)
list_.push(0)
list_.append(9)
list_.append(10)
print(list_.node(0))
list_.printList()

print ("Długość listy stack wynosi:",stack.getCount())
stack.push(3)
stack.push(10)
stack.push(1)
stack.pop()
print ("Długość listy stack wynosi:",stack.getCount())

print ("Długość listy queue wynosi:",queue.getCount())
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
queue.printList()
client_first = queue.dequeue()
queue.printList()
print ("Długość listy queue wynosi:",queue.getCount())