import pytest
from Structures import Stack, Node, DL_List, Queue, Vector, BinaryHeap

# region [Stack tester]
class TestStack:
       def test_init(self):
        """Тест инициализации стека."""

        stack = Stack()
        assert len(stack) == 0

        def test_push_single(self):
            """Тест добавления одного элемента."""

            stack = Stack()
            stack.push(99)
            assert len(stack) == 1
            assert stack.top() == 99

        def test_top_empty_raises(self):
            """Тест вызова топ у пустого стэка"""

            stack = Stack()
            with pytest.raises(IndexError, match="Нечего топать"):
                stack.top()

        def test_pop_single(self):
            """Тест удаления одного элемента."""

            stack = Stack()
            stack.push(7)
            result = stack.pop()
            assert result == 7
            assert len(stack) == 0

# endregion

# region [Node tester]
class TestNode:
    def test_node_init(self):
        """Тест создания ноды."""

        node = Node(88)
        assert node.value == 88
        assert node.next is None
        assert node.prev is None
    
    def test_node_types(self):
        """Тест ноды с различными типами данных."""

        node1 = Node("string")
        assert node1.value == "string"
        
        node2 = Node([1, 2, 3])
        assert node2.value == [1, 2, 3]
        
        node3 = Node(None)
        assert node3.value is None

# endregion

# region [DLL tester]
class TestDLL:
    def test_init_empty_list(self):
        """Тест инициализации списка."""

        dll = DL_List()
        assert dll.head() is None
        assert dll.tail() is None
        assert len(dll) == 0
    
    def test_push_front_single_element(self):
        """Тест добавления одного элемента в начало."""

        dll = DL_List()
        node = dll.push_front(99)
        
        assert dll.head() is node
        assert dll.tail() is node
        assert node.value == 99
        assert node.next is None
        assert node.prev is None
        assert len(dll) == 1

    def test_push_back_single_element(self):
        """Тест добавления одного элемента в конец."""

        dll = DL_List()
        node = dll.push_back(99)
        
        assert dll.head() is node
        assert dll.tail() is node
        assert len(dll) == 1

    def test_pop_front_single_element(self):
        """Тест удаления единственного элемента с начала."""

        dll = DL_List()
        dll.push_front(999)
        result = dll.pop_front()
        
        assert result == 999
        assert dll.head() is None
        assert dll.tail() is None
        assert len(dll) == 0

    def test_insert_not_in_list_raises_error(self):
        """Тест вставки ноды, не принадлежащей списку."""

        dll1 = DL_List()
        dll2 = DL_List()
        
        node_external = dll2.push_back(999)
        
        with pytest.raises(ValueError, match="Нет нода в списке"):
            dll1.insert(1, node_external)

# endregion

# region [queueue tester]
class TestQueue:
    def test_init_empty_queue(self):
        """Тест инициализации очереди."""

        queue = Queue()
        assert len(queue) == 0
    
    def test_enqueue_single_element(self):
        """Тест добавления элемента."""

        queue = Queue()
        queue.enqueue(99)
        assert len(queue) == 1
        assert queue.peek() == 99
    
    def test_dequeue_single_element(self):
        """Тест удаления единственного элемента."""

        queue = Queue()
        queue.enqueue(99)
        result = queue.dequeue()
        
        assert result == 99
        assert len(queue) == 0
    
    def test_dequeue_fifo_order(self):
        """Тест FIFO."""

        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert len(queue) == 0

    def test_dequeue_empty_raises_error(self):
        """Тест исключения при удалении из пустой очереди."""

        queue = Queue()
        with pytest.raises(IndexError, match="Нечего попать"):
            queue.dequeue()

# endregion

# region [Vector tester]
class TestVector:
    def test_init_default_capacity(self):
        """Тест инициализации с емкостью по умолчанию."""

        vec = Vector()
        assert len(vec) == 0
        assert vec.capacity == 10
    
    def test_init_custom_capacity(self):
        """Тест инициализации с пользовательской емкостью."""

        vec = Vector(capacity=20)
        assert len(vec) == 0
        assert vec.capacity == 20

    def test_init_invalid_capacity(self):
        """Тест исключения при неверной емкости."""

        with pytest.raises(ValueError, match="Вместимость маленькая"):
            Vector(capacity=0)

# endregion

# region [Heap tester]
class TestHeap:
    def test_init_empty(self):
        """Тест инициализации кучи."""

        heap = BinaryHeap()
        assert len(heap) == 0
    
    def test_push_single(self):
        """Тест добавления одного элемента."""

        heap = BinaryHeap()
        heap.push(999)
        assert len(heap) == 1
        assert heap.peek_min() == 999

    def test_push_preserves_heap_property(self):
        """Тест что push сохраняет heap свойство."""

        heap = BinaryHeap()
        values = [10, 55, 15, 43, 27, 20, 1]
        
        for val in values:
            heap.push(val)
        
        assert heap.peek_min() == 1

    def test_pop_min_single(self):
        """Тест удаления минимума из одного элемента."""

        heap = BinaryHeap()
        heap.push(99)
        
        result = heap.pop_min()
        assert result == 99
        assert len(heap) == 0

    def test_pop_min_empty(self):
        """Тест исключения при удалении из пустой кучи."""

        heap = BinaryHeap()
        with pytest.raises(IndexError, match="Нечего  попать"):
            heap.pop_min()

# endregion

