
# coding: utf-8

# In[1]:

import random


# In[2]:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.up = None
        self.down = None
    
    def __str__(self):
        return str(self.data)


# In[3]:

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def appendToHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        newNode.prev = None
        if self.head != None:
            self.head.prev = newNode
        self.head = newNode
        return newNode
            
    def deleteNode(self, node):
        if node == self.head:
            nextNode = node.next
            if nextNode is not None:
                nextNode.prev = None
            self.head = nextNode
        else:
            prevNode = node.prev
            nextNode = node.next
            if prevNode is not None:
                prevNode.next = nextNode
            if nextNode is not None:
                nextNode.prev = prevNode


# In[4]:

class SkipList:
    
    def __init__(self):
        self.maxLayers = 32
        self.layers = 1
        self.head = [DoublyLinkedList()]*self.layers
        
    def probability(self):
        return random.choice([True, False])
            
    def insert(self, value):
        level = 0
        if self.head[level].head == None:
            self.head[level].appendToHead(value)
            while self.probability() !=  False:
                level += 1
                self.layers += 1
                #create a new level and add the value
                self.head.append(DoublyLinkedList())
                self.head[level].appendToHead(value)
                #set the up and down pointers
                self.head[level].head.down = self.head[level - 1].head
                self.head[level - 1].head.up = self.head[level].head
                if self.layers == self.maxLayers:
                    break
        else:
            level = self.layers - 1
            top = self.head[level].head
            while top == None and level > 0:
                level -= 1
                top = self.head[level].head
            #find the position to insert the element
            while True:
                while top.prev != None and top.data > value:
                    top = top.prev
                while top.next != None and top.next.data <= value:
                    top = top.next
                if level == 0:
                    break
                level -= 1
                top = top.down
            #insert the element
            if top.data != value:
                while top.prev != None and top.data > value:
                    top = top.prev
                #insert at head
                if top.data > value:
                    temp = self.head[level].head
                    self.head[level].head = Node(value)
                    self.head[level].head.next = temp
                    temp.prev = self.head[level].head
                    
                    top = self.head[level].head
                else:
                    temp = top.next
                    top.next = Node(value)
                    top.next.next = temp
                    if temp != None:
                        temp.prev = top.next
                    top.next.prev = top

                    top = top.next
            else:
                #if element already exists
                while top.up != None:
                    top = top.up
                    level += 1
            
            while self.probability() != False:
                level += 1
                if level == self.maxLayers:
                    break
                #create a new level with new node as the head
                if level > self.layers - 1 or self.head[level].head == None:
                    self.layers += 1
                    #create a new level and add the value
                    self.head.append(DoublyLinkedList())
                    self.head[level].appendToHead(value)
                    #set the up and down pointers
                    self.head[level].head.down = top
                    top.up = self.head[level].head
                    
                    top = self.head[level].head
                else:
                    #find the node to insert after
                    previous = top.prev
                    if previous == None:
                        temp = self.head[level].head
                        self.head[level].head = Node(value)
                        self.head[level].head.next = temp
                        temp.prev = self.head[level].head
                        #set the up and down pointers
                        self.head[level].head.down = top
                        top.up = self.head[level].head
                            
                        top = self.head[level].head
                    else:
                        while previous.prev != None and previous.up == None:
                            previous = previous.prev
                        if previous.up == None:
                            temp = self.head[level].head
                            self.head[level].head = Node(value)
                            self.head[level].head.next = temp
                            temp.prev = self.head[level].head
                            #set the up and down pointers
                            self.head[level].head.down = top
                            top.up = self.head[level].head
                            
                            top = self.head[level].head
                        else:
                            #insert the node
                            previous = previous.up
                            temp = previous.next
                            previous.next = Node(value)
                            previous.next.next = temp
                            if temp != None:
                                temp.prev = previous.next
                            previous.next.prev = previous
                            #set the up and down pointers
                            previous.next.down = top
                            top.up = previous.next
                            top = previous.next

    def lookup(self, value):
        level = self.layers - 1
        top = self.head[level].head
        if top == None:
            return False
        else:
            while True:
                while top.prev != None and top.data > value:
                    top = top.prev
                while top.next != None and top.next.data <= value:
                    top = top.next
                if level == 0 or top.data == value:
                    break
                level -= 1
                top = top.down
            if top.data == value:
                return True
            else:
                return False
    
    def delete(self, value):
        level = self.layers - 1
        top = self.head[level].head
        while top == None and level > 0:
            level -= 1
            top = self.head[level].head
        if top == None:
            print("Element is not Present")
            return
        else:
            while True:
                while top.prev != None and top.data > value:
                    top = top.prev
                while top.next != None and top.next.data <= value:
                    top = top.next
                if level == 0:
                    break
                level -= 1
                top = top.down
            if top.data == value:
                while True:
                    self.head[level].deleteNode(top)
                    if top.up != None:
                        top = top.up
                        level += 1
                    else:
                        break
            else:
                print("Element is not Present")
                return


# In[5]:

skip_list = SkipList()


# In[6]:

skip_list.insert(4)
skip_list.insert(2)
skip_list.insert(3)
skip_list.insert(9)
skip_list.insert(8)
skip_list.insert(7)
skip_list.insert(12)
skip_list.insert(10)
skip_list.insert(7.5)


# In[7]:

print(skip_list.lookup(1))
print(skip_list.lookup(7))


# In[8]:

skip_list.delete(1)


# In[9]:

skip_list.delete(4)


# In[10]:

skip_list.lookup(4)


# In[11]:

print(skip_list.head[0].head)


# In[12]:

skip_list.delete(2)


# In[13]:

skip_list.lookup(2)


# In[14]:

skip_list.delete(2)


# In[15]:

skip_list.delete(3)


# In[16]:

skip_list.lookup(3)


# In[17]:

print(skip_list.head[1].head)


# In[18]:

#skip_list.insert(2)


# In[19]:

print(skip_list.head[0].head)


# In[20]:

skip_list.insert(2)


# In[21]:

print(skip_list.head[0].head)


# In[22]:

skip_list.insert(1)
skip_list.insert(3)


# In[ ]:



