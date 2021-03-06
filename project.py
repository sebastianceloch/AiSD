from typing import Any
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    #inicjujemy glowe w liscie
      
    def push(self,new_data: Any) -> None:
        new_node = Node(new_data) #nowy node przyjmuje wartosc new_data
        new_node.next = self.head #element po tym = head
        self.head = new_node #glowa = nowy element czyli 1 element dodajemy

    def append(self,new_data: Any) -> None:
        new_node = Node(new_data)
        if self.head is None: #jak 1szy element pusty to dodajemy Node na heada
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node #dodajemy element na koniec listy

    def insert(self,prev_node: Node,new_data: Any) ->None:
        if prev_node is None: 
            print ("podany wezel musi byc w liscie")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def node(self, at: int) ->Node:
        if self.length() >= at:
            node = self.head
            for x in range(at):
                node = node.next
            return node.data

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return count

    def remove(self, key: Node) ->Any:
        temp = self.head
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None
    
    def pop(self) ->Any:
        node = self.head
        self.head = node.next
        return 'usuniety element to = '+str(node.data)

    def remove_last(self) ->Any:
        node = self.head
        for x in range(self.length()-2):
            node = node.next
        node2 = node.next
        node.next = None
        return 'usuniety element to = '+str(node2.data)

# print listy
    def printList(self):
        temp = self.head 
        while(temp):
            print (temp.data,end=" -> ")
            temp = temp.next

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data: Any) -> None:
        if self.head == None:
            self.head=Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def len(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count+=1
        return count

    def pop(self) ->Any:
        pop_node = self.head
        self.head = self.head.next
        pop_node.next = None
        return 'usuniety element to = '+str(pop_node.data)

    def print(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end = " -> ")
            temp = temp.next
        return
class Queue:
    def __init__(self):
        self.head = self.back = None

    def enqueue(self,element: Any) -> None:
        temp = Node(element)
        if self.back == None:
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp

    def dequeue(self) -> None:
        temp = self.front
        self.front = temp.next
        if(self.front == None):
            self.back = None

    def peek(self) -> Any:
        if self.front:
            return self.front.data

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=' <- ')
            temp = temp.next
        print()
    
    def len(self):
        count = 0
        node = self.front
        while node:
            node = node.next
            count+=1
        return count


llist = LinkedList()
llist.append(6)
llist.append(3)
llist.append(5)
llist.push(1)
llist.push(5)
llist.push(3)
llist.remove(1)
llist.insert(llist.head.next,5)
print(llist.pop())
print(llist.remove_last())
print('dlugosc listy = ',llist.length())
print(llist.node(0))
llist.printList()
print('\n')

Stackk = Stack()
Stackk.push(10)
Stackk.push(5)
Stackk.push(33)
print(Stackk.pop())
print(Stackk.len())
Stackk.print()
print('\n')

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(2)
q.dequeue()
print(q.peek())
q.print()
print(q.len())



