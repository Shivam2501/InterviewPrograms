# This class creates a node object for each (key, value)
# pair. These node objects can be inserted into the linked
# list.
class Node:
    def __init__(self, key, value):
        # TO-DO: Check key, value type
        self.key = key
        self.value = value
        self.next = None
    
    def setNext(self, nextNode):
        self.next = nextNode
    
    def __str__(self):
        return str(self.key)

# This class creates a linked list which stores
# (key, value) nodes.
class LinkedList:
    def __init__(self):
        self.head = None
        
    def searchNode(self, key):
        currentHead = self.head
        while currentHead is not None:
            if currentHead.key == key:
                return currentHead.value
            else:
                currentHead = currentHead.next
        return None
          
    # Insert the (key, value) pair if the key is not present in the list.
    # Otherwise, update the value of the existing key.
    # Return value: True on insertion and False on updating an existing value
    def updateOrInsertNode(self, key, value):
        if self.head is None:
            newNode = Node(key, value)
            self.head = newNode
            return True
        if self.head.key == key:
            self.head.value = value
            return False
        
        currentHead = self.head
        while currentHead.next is not None:
            if currentHead.next.key == key:
                currentHead.next.value = value
                return False
            else:
                currentHead = currentHead.next
        
        newNode = Node(key, value)
        currentHead.setNext(newNode)
        return True
        
    def deleteNode(self, key):
        currentHead = self.head
        if currentHead is None:
            return currentHead
        if currentHead.key == key:
            self.head = currentHead.next
            return currentHead.value
        
        while currentHead.next is not None:
            if currentHead.next.key == key:
                value = currentHead.next.value
                currentHead.setNext(currentHead.next.next)
                return value
            else:
                currentHead = currentHead.next
        return None
