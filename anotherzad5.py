
from __future__ import annotations
from typing import Dict
import sys

class _Node:
    value: int
    next: _Node
    prev: _Node

    def __init__(self, value: int, next_elem: _Node = None, prev_elem: _Node = None):
        self.value: int = value
        self.next: _Node = next_elem
        self.prev: _Node = prev_elem
    
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __str__(self):
        return f"value: {self.value}, next: {self.next}, prev: {self.prev}"

class very_cool_hashmap:
    def __init__(self):
        self.size = 16
        self.map: Dict[int, _Node] = {}

    def _resize(self):
        self.size *= 2
        old_map = self.map
        new_map: Dict[int, _Node] = {}

        for node in old_map.values():
            new_map[self._hash(node.value)] = node
        self.map = new_map

    def _hash(self, key: int) -> int:
        return hash(key) % self.size
        
    def add(self, value: int, *args):
        if len(args) > 1:
            raise ValueError("Too many arguments")
        
        if self.get_node(value) is not None:
            while True:
                self._resize()
                if self.get_node(value) is None:
                    break
        
        if len(args) == 0:
            if not self.map:
                self.map[self._hash(value)] = _Node(value)
                return
            
            keys = list(self.map.keys())

            prev_elem = sys.maxsize
            next_elem = -sys.maxsize

            for key in keys:
                if (self.map[key].value < value) and (self.map[key].value > prev_elem):
                    prev_elem = self.map[key]
            for key in reversed(keys):
                if (self.map[key].value > value) and (self.map[key].value < next_elem):
                    next_elem = self.map[key]
            if (prev_elem == sys.maxsize):
                prev_elem = None
            if (next_elem == -sys.maxsize):
                next_elem = None
            self.map[self._hash(value)] = _Node(value, _Node(next_elem), _Node(prev_elem))
            if prev_elem is not None:   
                self.map[self._hash(prev_elem)].next = value
            if next_elem is not None:
                self.map[self._hash(next_elem)].prev = value
        
        if len(args) == 1:
            nearest_value = args[0]
            if (nearest_value > value):
                prev_elem = self.map[self._hash(nearest_value)].prev
                next_elem = _Node(nearest_value)
                elem = _Node(value, next_elem, prev_elem)
                self.map[self._hash(elem)] = elem
                if prev_elem is not None:
                    self.map[self._hash(prev_elem)].next = elem
                self.map[self._hash(next_elem)].prev = elem
            else:
                prev_elem = _Node(nearest_value)
                next_elem = self.map[self._hash(nearest_value)].next
                elem = _Node(value, next_elem, prev_elem)
                self.map[self._hash(elem)] = elem
                self.map[self._hash(prev_elem)].next = elem
                if next_elem is not None:
                    self.map[self._hash(next_elem)].prev = elem

    def get_value_by_key(self, key: int) -> int:
        current = self.map.get(self._hash(key))
        
        if current is not None:
            return current.value
        return None
    def get_node(self, key: int) -> _Node:
       return self.map.get(self._hash(key))
    
    def delete(self, key: int):
        key_hash = self._hash(key)

        if self.map[key_hash] is None:
            return False
        
        if self.map[key_hash].next is not None:
            self.map[key_hash].next.prev = self.map[key_hash].prev
        if self.map[key_hash].prev is not None:
            self.map[key_hash].prev.next = self.map[key_hash].next
        del self.map[key_hash]
    
    def get_next(self, key: int) -> int:
        if self.get_node(key) is not None:
            return self.get_node(self._hash(key)).next
        return None

    def get_prev(self, key: int) -> int:
        if self.get_node(key) is not None:
            return self.get_node(self._hash(key)).prev
        return None

my_map: very_cool_hashmap = very_cool_hashmap()
my_map.add(1)
my_map.add(2)
my_map.add(3, 2)
print(my_map.get_next(1))
print(my_map.get_next(3))
print(my_map.get_prev(1))
