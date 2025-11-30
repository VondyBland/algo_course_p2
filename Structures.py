from typing import Any, Optional, Iterable

# region [Stack]
class Stack:
    def __init__(self) -> None:
        self._items: list(Any) = []

    def push(self, x: Any) -> None:
        self._items.append(x)

    def pop(self) -> Any:
        if not self._items:
            raise IndexError ("Нечего попать")
        return self._items.pop()
    
    def top(self) -> Any:
        if not self._items:
            raise IndexError ("Нечего топать")
        return self._items[-1]
    
    def __len__(self) -> int:
        return len(self._items)
    
# endregion

# region [Double_Linked_List]
class Node:
    def __init__(self, value:Any)->None:
        self.value: Any = value
        self.next: Optional['Node'] = None
        self.prev: Optional['Node'] = None

class DL_List:
    def __init__(self) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0
    
    def head(self) -> Optional[Node]:
        return self._head

    def tail(self) -> Optional[Node]:
        return self._tail

    def find(self, x:Any) -> Optional[Node]:
        current = self._head
        while current is not None:
            if current.value == x:
                return current
            current = current.next
        return None
    
    def push_front(self,x:Any) -> Node:
        new_node = Node(x)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._size += 1
        return new_node

    def push_back(self,x:Any) -> Node:
        new_node = Node(x)
        
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        
        self._size += 1
        return new_node

    def pop_front(self) -> Any:

        if self._head is None:
            raise IndexError("Нечего попать")
        
        value = self._head.value
        
        if self._head.next is None:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        
        self._size -= 1
        return value

    def pop_back(self) -> Any:
        if self._tail is None:
            raise IndexError("pop_back from empty list")
        
        value = self._tail.value
        
        if self._tail.prev is None:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        
        self._size -= 1
        return value

    def insert(self, x:Any, node:Node)->Node:
        current = self._head
        while current is not None:
            if current is node:
                break
            current = current.next
        else:
            raise ValueError("Нет нода в списке")
        
        new_node = Node(x)
        
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        
        if new_node.next is not None:
            new_node.next.prev = new_node
        else:
            self._tail = new_node
        
        self._size += 1
        return new_node

    def remove(self, x:Any) -> None:
        node = self.find(x)
        if node is None:
            raise ValueError(f"Такого элемента, как {x} - нет в списке")
        
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self._head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        
        self._size -= 1
    
    def __len__(self) ->int:
        return self._size
    
# endregion

# region [queue]
class Queue:
    '''кувеве'''

    def __init__(self)->None:
        self._list = DL_List()

    def enqueue(self, x: Any) ->None:
        self._list.push_back(x)

    def dequeue(self) -> Any:
        if self._list is None:
            raise IndexError("очередь пуста")
        return self._list.pop_front()

    def peek(self)-> Any:
        head = self._list.head()
        if head is None:
            raise IndexError("очередь пуста")
        return head.value

    def __len__(self) -> int:
        return len(self._list)

# endregion


# region [Vector]
class Vector:
    def __init__(self, capacity:int=10)->None:
        if capacity <1:
            raise ValueError("Вместимость маленькая")
        
        self._capacity: int=capacity
        self._size: int = 0
        self._buffer: list[Any] = [None] * capacity

    def _reallocate(self, new_capacity: int) -> None:

        if new_capacity < self._size:
            raise ValueError("Новая капасити должна быть не менее размера")
        
        new_buffer: list[Any] = [None] * new_capacity
        
        for i in range(self._size):
            new_buffer[i] = self._buffer[i]
        
        self._buffer = new_buffer
        self._capacity = new_capacity
    
    def push_back(self, x: Any) -> None:

        if self._size >= self._capacity:
            self._reallocate(self._capacity * 2)
        
        self._buffer[self._size] = x
        self._size += 1
    
    def push_front(self, x: Any) -> None:

        if self._size >= self._capacity:
            self._reallocate(self._capacity * 2)
        
        for i in range(self._size, 0, -1):
            self._buffer[i] = self._buffer[i - 1]
        
        self._buffer[0] = x
        self._size += 1
    
    def pop_back(self) -> Any:

        if self._size == 0:
            raise IndexError("нечего попать")
        
        self._size -= 1
        value = self._buffer[self._size]
        self._buffer[self._size] = None
        
        return value
    
    def pop_front(self) -> Any:

        if self._size == 0:
            raise IndexError("Нечего попать")
        
        value = self._buffer[0]
        
        for i in range(self._size - 1):
            self._buffer[i] = self._buffer[i + 1]
        
        self._size -= 1
        self._buffer[self._size] = None
        
        return value
    
    def remove(self, idx: int) -> Any:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} в рендже [0, {self._size})")
        
        value = self._buffer[idx]
        
        for i in range(idx, self._size - 1):
            self._buffer[i] = self._buffer[i + 1]
        
        self._size -= 1
        self._buffer[self._size] = None
        
        return value
    
    def swap_remove(self, idx: int) -> Any:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} в рендже [0, {self._size})")
        
        value = self._buffer[idx]
        
        if idx != self._size - 1:
            self._buffer[idx] = self._buffer[self._size - 1]
        
        self._size -= 1
        self._buffer[self._size] = None
        
        return value
    
    def clear(self) -> None:

        self._size = 0
        self._buffer = [None] * self._capacity
    
    def __setitem__(self, idx: int, x: Any) -> None:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} в рендже [0, {self._size})")
        
        self._buffer[idx] = x
    
    def __getitem__(self, idx: int) -> Any:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} в рендже [0, {self._size})")
        
        return self._buffer[idx]
    
    def __len__(self) -> int:
        return self._size
    
    @property
    def capacity(self) -> int:
        return self._capacity
    
# endregion

# region [binar_kucha]
class BinaryHeap:
    
    def __init__(self) -> None:
        self._heap: list[Any] = []
    
    @classmethod
    def heapify(cls, iterable: Iterable) -> 'BinaryHeap':

        heap = cls()
        items = list(iterable)
        heap._heap = items.copy()

        for i in range(len(heap._heap) // 2 - 1, -1, -1):
            heap._sift_down(i)
        
        return heap
    
    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2
    
    def _left_child(self, idx: int) -> int:
        return 2 * idx + 1
    
    def _right_child(self, idx: int) -> int:
        return 2 * idx + 2
    
    def _sift_up(self, idx: int) -> None:

        while idx > 0:
            parent_idx = self._parent(idx)
            if self._heap[idx] < self._heap[parent_idx]:
                self._heap[idx], self._heap[parent_idx] = (
                    self._heap[parent_idx], self._heap[idx]
                )
                idx = parent_idx
            else:
                break
    
    def _sift_down(self, idx: int) -> None:

        while True:
            smallest = idx
            left = self._left_child(idx)
            right = self._right_child(idx)
            
            if left < len(self._heap) and self._heap[left] < self._heap[smallest]:
                smallest = left
            
            if right < len(self._heap) and self._heap[right] < self._heap[smallest]:
                smallest = right
            
            if smallest != idx:
                self._heap[idx], self._heap[smallest] = (
                    self._heap[smallest], self._heap[idx]
                )
                idx = smallest
            else:
                break
    
    def push(self, x: Any) -> None:
        self._heap.append(x)
        self._sift_up(len(self._heap) - 1)
    
    def pop_min(self) -> Any:

        if len(self._heap) == 0:
            raise IndexError("Нечего  попать")
        
        min_value = self._heap[0]
        
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        
        if len(self._heap) > 0:
            self._sift_down(0)
        
        return min_value
    
    def peek_min(self) -> Any:

        if len(self._heap) == 0:
            raise IndexError("Нечего  попать")
        
        return self._heap[0]
    
    def __len__(self) -> int:
        return len(self._heap)
    
# endregion