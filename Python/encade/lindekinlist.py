from ctypes import pointer
from platform import node
from re import I
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)      
        else:
            self.head = Node(elem)
        self._size += 1
        
    def __len__ (self):
        return self._size      
    
    def get(self, index):
        pass
    
    def set (self, index, elem):
        pass
    
    def __getintem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of range")
                
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer
            else:
                raise IndexError("List index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range") 
    
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            else:
                i += 1