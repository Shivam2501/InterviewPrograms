from LinkedList import LinkedList

class KPCBMap:
    
    def __init__(self, size):
        self.size = 0
        self.mapSize = size
        self.kpcbMap = [LinkedList()] * size
        
    def set(self, key, value):
        mapIndex = hash(key) % self.mapSize
        if self.size == self.mapSize and self.kpcbMap[mapIndex].searchNode(key) is None:
            return False
        
        insertNode = self.kpcbMap[mapIndex].updateOrInsertNode(key, value)
        if insertNode:
            self.size += 1
        return True
    
    def get(self, key):
        mapIndex = hash(key) % self.mapSize
        return self.kpcbMap[mapIndex].searchNode(key)
    
    def delete(self, key):
        mapIndex = hash(key) % self.mapSize
        value = self.kpcbMap[mapIndex].deleteNode(key)
        if value is not None:
            self.size -= 1
        return value
    
    def load(self):
        return self.size / self.mapSize
        