class Node:
    def __init__(self , value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print(f'Length of LinkedList is {self.length}')

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        pre.next = None
        self.length -=1
        if self.length ==0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node
        self.length +=1

    def popfirst(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -=1
        return temp.value

    def get(self,index):
        if index < 0 or index >=self.length:
            print('Index out of range : Please check it once')
            return None

        temp =self.head
        for _ in range(index):
            temp = temp.next

        print(f'Current Indexed Value is - > {temp.value}')
        return temp
        

    def set(self,value,index):
        if index < 0 or index >=self.length:
            print('Index out of range : Please check it once')
            return None
        Indexed_node = self.get(index)
        Indexed_node.value = value

    def insert(self,value,index):
        new_node = Node(value)
        if index < 0 or index >=self.length:
            print('Index out of range : Please check it once')
            return None
        if index == 0:
            self.prepend(value)
        if index == self.length-1:
            self.append(value)
        else:
            prev_node = self.get(index-1)
            temp =prev_node.next
            prev_node.next = new_node
            new_node.next = temp
        self.length+=1    
        return True    
    
    def remove(self,index):
        if index < 0 or index >=self.length:
            print('Index out of range : Please check it once')
            return None
        if index == self.length-1:
            self.pop()
        if index == 0 :
            self.popfirst()
        else:
            prev = self.get(index-1)
            temp = prev.next.next
            indexed_value = prev.next
            indexed_value.next = None
            prev.next = temp
            return indexed_value.value

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

My_linkedlist = LinkedList(1)
My_linkedlist.append(2)
My_linkedlist.append(3)
My_linkedlist.append(4)  
My_linkedlist.append(5)
My_linkedlist.reverse()
My_linkedlist.printlist()
