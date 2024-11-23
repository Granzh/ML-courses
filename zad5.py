from typing import Dict
import sys

class _Node:
    def __init__(self, value: int, next_elem: int = None, prev_elem: int = None):
        self.value: int = value
        self.next: int = next_elem
        self.prev: int = prev_elem
    
    def __hash__(self) -> int:
        return hash(self.value)
    def key(self):
        return self.value
    def __str__(self):
        return f"value: {self.value}, next: {self.next}, prev: {self.prev}"

class Very_cool_hashmap:
    size: int = 16

    def __init__(self):
        self.size = 16
        self.LOAD_FACTOR: float = 0.75
        self.map: Dict[int, _Node] = {}

    def _resize(self):
        self.size *= 2
        old_map = self.map.copy()
        self.map = {}
        
        for node in old_map.values():
            new_hash = self._hash(node.value)
            while new_hash in self.map:
                self.size += 1
                new_hash = self._hash(node.value)
            self.map[new_hash] = node

    def _hash(self, key: int) -> int:
        return hash(key) % self.size
    
    def _get_node(self, key: int) -> _Node:
       return self.map.get(self._hash(key))
        
    def add(self, elem: int, *args: int):
        if self._get_node(elem) is not None:
            if self._get_node(elem).value == elem:
                return
            else:
                self._resize()
    
        if len(args) > 1:
            raise ValueError("Too many arguments")

        if len(args) == 0:
            if not self.map:
                self.map[self._hash(elem)] = _Node(elem)
                return
            
            keys = list(self.map.keys())
            prev_elem: int = None
            next_elem: int = None
            min_diff_prev = sys.maxsize
            min_diff_next = sys.maxsize

            for key in keys:
                current_value = self.map[key].value
                diff = elem - current_value
                if diff > 0 and diff < min_diff_prev:
                    min_diff_prev = diff
                    prev_elem = current_value
                elif diff < 0 and -diff < min_diff_next:
                    min_diff_next = -diff
                    next_elem = current_value

            self.map[self._hash(elem)] = _Node(elem, next_elem, prev_elem)
            if prev_elem is not None:   
                self.map[self._hash(prev_elem)].next = elem
            if next_elem is not None:
                self.map[self._hash(next_elem)].prev = elem
        if len(args) == 1:
            nearest_value = args[0]
            if nearest_value > elem:
                prev_elem = self.map[self._hash(nearest_value)].prev
                next_elem = nearest_value
                self.map[self._hash(elem)] = _Node(elem, nearest_value, prev_elem)
                if prev_elem is not None:
                    self.map[self._hash(prev_elem)].next = elem
                self.map[self._hash(next_elem)].prev = elem
            else:
                prev_elem = nearest_value
                next_elem = self.map[self._hash(nearest_value)].next
                self.map[self._hash(elem)] = _Node(elem, next_elem, prev_elem)
                self.map[self._hash(prev_elem)].next = elem
                if next_elem is not None:
                    self.map[self._hash(next_elem)].prev = elem

    def get(self, value: int) -> int:
        key_hash = self._hash(value)
        current = self.map[key_hash]
        
        if current is not None:
            return current.value
        return None
    
    def delete(self, key: int):
        key_hash = self._hash(key)
        
        if key_hash not in self.map:
            return False
        
        node = self.map[key_hash]
        next_elem = node.next
        prev_elem = node.prev
        
        if next_elem is not None:
            self.map[self._hash(next_elem)].prev = prev_elem
        if prev_elem is not None:
            self.map[self._hash(prev_elem)].next = next_elem
        
        del self.map[key_hash]
    
    def get_next(self, value) -> int:
        if self._get_node(value) is not None:
            return self._get_node(value).next
        return None

    def get_prev(self, value) -> int:
        if self._get_node(value) is not None:
            return self._get_node(value).prev
        return None



my_map: Very_cool_hashmap = Very_cool_hashmap()
my_map.add(1)
my_map.add(2)
my_map.add(3, 2)
my_map.add(11)
my_map.add(4)
my_map.add(5)
my_map.add(12)
my_map.add(13)
my_map.add(14)
my_map.add(-1, 1)
my_map.add(-2, -1)
my_map.add(-3)
my_map.add(15, 14)
my_map.add(7)
my_map.add(8, 7)
my_map.add(9, 8)
my_map.add(10, 9)
for node in my_map.map.values():
    print(node)
print()
my_map.delete(1)
for node in my_map.map.values():
    print(node)
