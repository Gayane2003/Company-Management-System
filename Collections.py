from abc import ABC, abstractmethod


class Collection(ABC):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def print(self):
        pass


class List(Collection):
    @abstractmethod
    def addFirst(self, e):
        pass

    @abstractmethod
    def removeFirst(self):
        pass

    @abstractmethod
    def addLast(self, e):
        pass

    @abstractmethod
    def removeLast(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def last(self):
        pass

    @abstractmethod
    def replace(self, e, r):
        pass


class Stack(Collection):
    @abstractmethod
    def push(self, e):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

class Queue(Collection):
    @abstractmethod
    def enqueue(self, value):
        pass
    
    @abstractmethod
    def dequeue(self):
        pass
    
    @abstractmethod
    def front(self):
        pass
    
    @abstractmethod
    def back(self):
        pass
    
    @abstractmethod
    def swap(self, v1, v2):
        pass
    

class Deque(Queue):
    @abstractmethod
    def left_enqueue(value):
        pass
    
    @abstractmethod
    def right_dequeue():
        pass


class Set(Collection):
    @abstractmethod
    def add(self, value):
        pass
    
    @abstractmethod
    def remove(self, value):
        pass
    
    @abstractmethod
    def contains(self, value):
        pass
    
    @abstractmethod
    def equals(self, s):
        pass
    
    @abstractmethod
    def get_element_at(self, index):
        pass
    
    
class Map(Collection):
    @abstractmethod
    def put(self, key, value):
        pass
    
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def remove(self, key):
        pass
    
    @abstractmethod
    def keySet(self):
        pass


class SortedSet(Collection):
    @abstractmethod
    def add(self, value: object)-> bool:
        pass
    
    @abstractmethod
    def remove(self, value: object)-> bool:
        pass
    
    @abstractmethod
    def contains(self, value: object)-> bool:
        pass
    
    @abstractmethod
    def equals(self, s: set)->bool:
        pass
    
    @abstractmethod
    def get_element_at(self, index: int)-> object:
        pass
    
    @abstractmethod
    def get_smallest_element(self) -> object:
        pass
    
    @abstractmethod
    def get_largest_element(self) -> object:
        pass


class SortedMap(Collection):
    @abstractmethod
    def put(self, key: object, value: object)-> object:
        pass
    
    @abstractmethod
    def get(self, key: object)-> object:
        pass
    
    @abstractmethod
    def remove(self, key: object)-> object:
        pass
    
    @abstractmethod
    def keySet(self):
        pass
    
    @abstractmethod
    def sub_map(self, k1, k2):
        pass


class PriorityQueueADT(Collection):
    @abstractmethod
    def enqueue(self, value: object):
        pass

    @abstractmethod
    def deque(self) -> object:
        pass

    @abstractmethod
    def head(self) -> object:
        pass


class LinkedList(List):
    class Node:
        def __init__(self, d, n=None):
            self._data = d
            self._next = n

    def __init__(self):
        self._first = None
        self._last = None
        self._length = 0

    def is_empty(self):
        return self._length == 0

    def empty(self):
        if self.is_empty():
            return None
        self._first = None
        self._last = None
        self._length = 0

    def print(self):
        if self.is_empty():
            return None
        n = self._first
        while n != None:
            print(n._data)
            n = n._next

    def addFirst(self, e):
        n = self.Node(e, self._first)
        self._first = n

        if self.is_empty():
            self._last = n

        self._length += 1

    def removeFirst(self):
        if self.is_empty():
            return None

        if self._length == 1:
            self._last = None
            self._first = None
            self._length -= 1
            return None

        self._first = self._first._next
        self._length -= 1
        return True

    def addLast(self, e):
        n = self.Node(e)

        if self.is_empty():
            self._last = n
            self._first = n
            self._length += 1
            return None

        self._last._next = n
        self._last = n
        self._length += 1

    def removeLast(self):
        if self.is_empty():
            return None

        if self._length == 1:
            self._last = None
            self._first = None
            self._length -= 1
            return True

        n = self._first
        while n._next != self._last:
            n = n._next

        self._last = n
        self._last._next = None
        self._length -= 1
        return True

    def first(self):
        if self.is_empty():
            return None
        return self._first._data

    def last(self):
        if self.is_empty():
            return None
        return self._last._data

    def replace(self, e, r):
        n = self._first

        while n != None:
            if n._data == e:
                n._data = r
                return True

            n = n._next
        print("We don't have provided data in our list")
    

    class ForwardIterator:
        def __init__(self, sll):
            self.current = sll._first

        def __next__(self):
            if self.current == None:
                raise StopIteration

            z = self.current._data
            self.current = self.current._next
            return z

    class OddPosIterator:
        def __init__(self, sll):
            self.id = 0
            self.current = sll._first


        def __next__(self):
            if self.current._next == None or self.current._next._next == None:
                raise StopIteration

            elif self.id % 2 != 0:
                self.id += 2
                self.current = self.current._next._next

            elif self.id % 2 == 0:
                self.id += 1
                self.current = self.current._next
                
            return self.current._data

        def __iter__(self):
            return self


    def __iter__(self):
        return self.ForwardIterator(self)


    def odd_iterator(self):
        return self.OddPosIterator(self)

    def private_reverse_rec(self, obj, Node):
        if self.is_empty():
            return None

        if obj._first._data == obj._last._data:
            for i in range(0, obj._length, 2):
                self.removeLast()
            return None

        obj.addFirst(Node._data)
        Node = Node._next
        self.private_reverse_rec(obj, Node)

    def reverse(self):
        self.private_reverse_rec(self, self._first)


                
class DoubleLinkedList(List):
    class Node:
        def __init__(self, d, n, p):
            self._data = d
            self._next = n
            self._prev = p

    def __init__(self):
        self._first = None
        self._last = None
        self._length = 0

    def is_empty(self):
        return self._length == 0

    def empty(self):
        if self.is_empty():
            return None
        self._first = None
        self._last = None
        self._length = 0
        print("The Double linked list es empty")

    def print(self):
        if self.is_empty():
            return None
        n = self._first
        while n != None:
            print(n._data)
            n = n._next

    def addFirst(self, e):
        n = self.Node(e, self._first, None)

        if self.is_empty():
            self._last = n
        else:
            self._first._prev = n

        self._first = n
        self._length += 1

    def removeFirst(self):
        if self.is_empty():
            return None
        if self._length == 1:
            self._last = None
            self._first = None
            self._length -= 1
            return None

        self._first = self._first._next
        self._first._prev = None
        self._length -= 1
        return True
    
    def addLast(self, e):
        n = self.Node(e, None, self._last)

        if self.is_empty():
            self._first = n
        else:
            self._last._next = n

        self._last = n
        self._length += 1

    def removeLast(self):
        if self.is_empty():
            return None

        if self._length == 1:
            self._last = None
            self._first = None
            self._length -= 1
            return True

        self._last = self._last._prev
        self._last._next = None
        self._length -= 1
        return True

    def first(self):
        if self.is_empty():
            return None
        return self._first._data

    def last(self):
        if self.is_empty():
            return None
        return self._last._data

    def replace(self, e, r):
        n = self._first

        while n != None:
            if n._data == e:
                n._data = r
                return True

            n = n._next
        print("We don't have provided data in our list")
    


class LinkedListStack(Stack):
    class Node:
        def __init__(self, d, n=None):
            self._data = d
            self._next = n

    def __init__(self):
        self._first = None
        self._length = 0

    def is_empty(self):
        return self._length == 0

    def empty(self):
        if self.is_empty():
            return None
        self._first = None
        self._length = 0
        print("The Stack is empty")

    def print(self):
        n = self._first
        while n != None:
            print(n._data)
            n = n._next

    def push(self, e):
        n = self.Node(e, self._first)
        self._first = n
        self._length += 1

    def pop(self):
        if self.is_empty():
            return None
        self._popped = self._first
        self._first = self._first._next
        self._length -= 1
        return self._popped

    def top(self):
        return self._first._data

    class ForwardIterator:
        def __init__(self, l_stack):
            self.current = l_stack._first

        def __next__(self):
            if self.current == None:
                raise StopIteration

            z = self.current._data
            self.current = self.current._next
            return z

    def __iter__(self):
        return self.ForwardIterator(self)



class DoubleLinkedListDeque(Deque):
    class Node():
        def __init__(self, d):
            self._data = d
            self._next = None
            self._prev = None
    
    def __init__(self):
        self._size = 0
        self._front = None
        self._back = None
    
    def is_empty(self):
        return self._size == 0

    def empty(self):
        self._front = None
        self._back = None
        self._size = 0

    def print(self):
        current = self._front
        
        while current:
            print(current._data)
            current = current._next
            
    def enqueue(self, value):
        #Adds element at the back
        n = self.Node(value)
        
        if self.is_empty():
            self._front = n
            self._back = n
            
        else:
            self._back._next = n
            n._prev = self._back 
            self._back = n
        
        self._size +=1
        return True
    
    def dequeue(self):
        #Removes element from beginning 

        if self.is_empty():
            return None
        
        removed = self._front._data
        if self._size == 1:
            self.empty()
            
        else: 
            self._front = self._front._next
            self._front._prev = None
            self._size -=1 
            
        return removed

    def front(self):
        if self.is_empty():
            return False
        return self._front._data

    def back(self):
        if self.is_empty():
            return False
        return self._back._data

    def swap(self, v1, v2):
        if self.is_empty():
            return False
        current = self._front
        while current:
            if current._data == v1:
                current2 = self._front
                while current2:
                    if current2._data == v2:
                        current2._data = v1
                        current._data = v2
                        return True
                    current2 = current2._next
                
                
            current = current._next
            
        return False
            
    def left_enqueue(self, value):
        #Adds element at the beginning
        n = self.Node(value)
        
        if self.is_empty():
            self._front = n
            self._back = n
        
        else:
            n._next = self._front
            self._front._prev = n
            self._front = n
            
        self._size += 1
        return True

    def right_dequeue(self):
        #Removes element from back
        if self.is_empty():
            return None
        
        removed = self._back._data
        if self._size == 1:
            self.empty()
            
        else: 
            self._back._prev._next = None
            self._back = self._back._prev
            self._size -=1 
            
        return removed

    class ForwardIterator():
        def __init__(self, obj):
            self._current = obj._front
        
        def __next__(self):
            if self._current == None:
                raise StopIteration
            
            z = self._current._data
            self._current = self._current._next
            return z
        
    def __iter__(self):
        return self.ForwardIterator(self)


class ArrayDeque(Deque):
    def __init__(self):
        self._arr = [None] * 10
        self._size = 0
        self._first = 0
        
    def is_empty(self):
        return self._size == 0

    def empty(self):
        self.__init__() 

    def print(self):
        for i in self._arr:
            print(i)
            
    def enqueue(self, value):
        if self._size == len(self._arr):
            return False
        self._arr[(self._first + self._size) % len(self._arr)] = value
        self._size += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        removed = self._arr[self._first % len(self._arr)]
        self._arr[self._first % len(self._arr)] = None
        self._first = (self._first + 1) % len(self._arr)
        self._size-=1
        return removed
        
    def front(self):
        if self.is_empty():
            return None
        return self._arr[self._first % len(self._arr)]

    def back(self): 
        if self.is_empty():
            return None
        return self._arr[(self._first + self._size -1) % len(self._arr)]

    def swap(self, v1, v2):
        if self.is_empty():
            return False
        
        for i in range(len(self._arr)):
            if self._arr[i] == v1:
                for z in range(len(self._arr)):
                    if self._arr[z] == v2:
                        self._arr[i] = v2
                        self._arr[z] = v1
                        return True
        return False 
                        

    def left_enqueue(self, value):
        if self._size == len(self._arr):
            return False
        self._arr[(self._first - 1) % len(self._arr)] = value
        self._first = (self._first - 1) % len(self._arr)
        self._size += 1
        return True

    def right_dequeue(self):
        if self.is_empty():
            return None
        
        if self._size == 1:
            removed = self._arr[self._first % len(self._arr)]
            self._arr[self._first] = None
            self._first = 0
        
        else:
            removed = self._arr[(self._first + self._size -1) % len(self._arr)]
            self._arr[(self._first + self._size-1) % len(self._arr)] = None
            
        self._size-=1
        return removed
        

    class ForwardIterator():
        def __init__(self, obj):
            self._current = obj._first    
            self._array = obj._arr
            self.first = obj._first
            
        def __next__(self):
            if self._array[self._current]==None:
                raise StopIteration
                
            z = self._array[self._current]
            self._current = (self._current + 1) % len(self._array)

            return z

    def __iter__(self):
        return self.ForwardIterator(self)



class HashSet(Set):
    class Node:
        def __init__(self, d, n = None):
            self._data = d
            self._next = n
            
    def __init__(self):
        self._hash_table = [None] * 10
        self._size = 0

    def add(self, value):
        if self.contains(value):
            return False 
        
        hash_index = self.hash(value)
        temp = self._hash_table[hash_index]
        node = self.Node(value, temp)
        self._hash_table[hash_index] = node
        self._size +=1
        return True
         
    def remove(self, value):
        if self.contains(value) == False:
            return False
        
        hash_index = self.hash(value)
        current = self._hash_table[hash_index]
        prev = None
        
        if current._data == value:
            current = current._next
            self._hash_table[hash_index] = current
        
        else:
            while current:
                if current._data == value:
                    prev._next = current._next
                
                prev = current
                current = current._next
                
        self._size-=1
        return True
    
    def contains(self, value):
        hash_index = self.hash(value)
        current = self._hash_table[hash_index]
        while current:
            if current._data == value:
                return True
            current = current._next
        return False
        
    def equals(self, s):
        if self._size != s._size:
            return False
        
        for i in s._hash_table:
            current = i
            while current:
                result = self.contains(current._data)
                if result == False:
                    return False
                current = current._next
        return True
        

    def get_element_at(self, index):
        if index >= self._size:
            return False
        elif index < 0:
            return False
        element_list = list()
        for i in self._hash_table:
            current = i
            while current:
                element_list.append(current._data)
                current = current._next
                
        return element_list[index]
    
    def hash(self, o):
        return hash(o) % len(self._hash_table)

    
    def print(self):
        for i in self._hash_table:
            current = i
            while current:
                print(current._data)
                current = current._next
                
    def is_empty(self):
        if self._size == 0:
            return True

    def empty(self):
        for i in range(len(self._hash_table)):
            self._hash_table[i] = None
        self._size = 0
     

class HashMap(Map):
    class Entry:
        def __init__(self, v = None, k = None, n = None):
            self._value = v
            self._key = k
            self._next = n
            
    def __init__(self):
        self._hash_table = [None] * 10
        self._size = 0
    
    def hash(self, key):
        return hash(key) % len(self._hash_table)
        
    def is_empty(self):
        if self._size == 0:
            return True

    def empty(self):
        for i in range(len(self._hash_table)):
            self._hash_table[i] = None
        self._size = 0

    def print(self):
        for i in range(len(self._hash_table)):
            if self._hash_table[i] != None:
                current = self._hash_table[i] 
                while current:
                    print(f"{current._key} : {current._value}")
                    current = current._next
                    
    def put(self, key, value):
        hash_index = self.hash(key)
        current = self._hash_table[hash_index]
        
        while current:
            if current._key == key:
                old_val = current._value
                current._value = value
                return old_val
            current = current._next

        temp = self._hash_table[hash_index]
        e = self.Entry(value, key, temp)
        self._hash_table[hash_index] = e
        self._size +=1
        return e._value

    def get(self, key):
        hash_index = self.hash(key)
        current = self._hash_table[hash_index]
        
        while current:
            if current._key == key:
                result = current._value
                return result
            current = current._next
        
        return False
    
    def remove(self, key):
        if self.is_empty():
            return False
        hash_index = self.hash(key)
        current = self._hash_table[hash_index]
        prev = None
        
        if current._key == key:
            temp = current._value 
            self._hash_table[hash_index] = current._next
            self._size -=1
            return temp            
        
        else:
            while current:
                if current._key == key:
                    temp = current._value 
                    prev._next = current._next
                    self._size -=1
                    return temp
                
                prev = current
                current = current._next
 
        return False 
        
    def keySet(self):
        key_set = set()
        for i in self._hash_table:
            if i != None:
                current = i
                while current:
                    key_set.add(current._key)
                    current = current._next
        return key_set
    
    
    class EntryIterator:
        def __init__(self, obj):
            self.obj = obj
            self.current = None
            for i in obj._hash_table:
                if i != None:
                    self.current = i
                    break
        
        def __next__(self):
            if self.current == None:
                raise StopIteration
                
            k, z = self.current._key, self.current._value
            
            while self.current:
                v = self.current
                self.current = self.current._next
                break
            
            if self.current == None:
                hash_index = self.obj.hash(v._key) + 1
                for i in self.obj._hash_table[hash_index:len(self.obj._hash_table)]:
                    if i != None:
                        self.current = i
                        break
            return k, z
    
    def __iter__(self):
        return self.EntryIterator(self)
    

# Sorry, for late submission and thank you for considering my homework! :) 

class TreeSet(SortedSet):
    class Node:
        def __init__(self, d = None, p = None):
            self._data = d
            self._left = None
            self._right = None
            self._parent = p
            self._color = "R"
    
        def set_parent(self, p):
            self._parent = p
        
        def get_left(self):
            return self._left
        
        def get_right(self):
            return self._right
        
        def get_data(self):
            return self._data
        
        def color_red(self):
            self._color = "R"
        
        def color_black(self):
            self._color = "B"
        
        def color_deficit(self):
            self._color = "D"
        
        def is_red(self):
            return self._color == "R"
        
        def is_black(self):
            return self._color == "B"
        
        def is_deficit(self):
            return self._color == "D"
        
    def __init__(self):
        self._root = None
        self._size = 0
    
    def add(self, value: object)-> bool:
        if self._root == None:
            self._root = TreeSet.Node(value)
            self._root.color_black()
            self._size += 1
            return True 
        else:
            return self.add_rec(self._root, value)
    
    def add_rec(self, node, v):
        if v > node._data:
            if node._right != None:
                res = self.add_rec(node._right, v)
                self.restructure(node)
                return res
            else:
                node._right = TreeSet.Node(v, node)
                self._size +=1
                self.restructure(node._right)
                return True
            
        elif v < node._data:
            if node._left != None:
                res = self.add_rec(node._left, v)
                self.restructure(node)
                return res
            else:
                node._left = TreeSet.Node(v, node)
                self._size +=1
                self.restructure(node._left)
                return True
        else:
            return False
        

    def right_rotate(self, node):
        p = node._parent
        x = node
        y = node._left
        T = y._right
        y._right = x
        x._parent = y
        x._left = T
        if T:
            T._parent = x
        y._parent = p
        if p == None:
            self._root = y
        else:
            if y._data < p._data:
                p._left = y
            else:
                p._right = y
        return y
    
    def left_rotate(self, node):
        p = node._parent
        x = node
        y = x._right
        T = y._left
        y._left = x
        x._parent = y
        x._right = T
        if T:
            T._parent = x
        y._parent = p
        if p == None:
            self._root = y
        else:
            if y._data < p._data:
                p._left = y
            else:
                p._right = y
        return y
    
    def get_sibling(self, node):
        if node == None or node._parent == None:
            return None
        
        if node._data > node._parent._data:
            return node._parent._left
        if node._data < node._parent._data:
            return node._parent._right
    
    def restructure(self, node):
        if not node:
            return 
        if node.is_black():
            return 
        if node._parent == None:
            node.color_black()
            return
        if node._parent.is_black():
            return 
        
        p = node._parent
        gp = p._parent
        
        if gp == None:
            p.color_black()
            return 
        
        u = self.get_sibling(p)
        if u!=None and u.is_red():
            p.color_black()
            u.color_black()
            gp.color_red()
            return 
        
        if p == gp._left:
            if node == p._right:
                p = self.left_rotate(p)
            self.right_rotate(gp)
            gp.color_red()
            p.color_black()
        
        else:
            if node == p._left:
                print("right", p._data)
                p = self.right_rotate(p)
            
            self.left_rotate(gp)
            gp.color_red()
            p.color_black()
            
        

    def remove(self, value: object)-> bool:
        self._size -=1
        return self.remove_rec(self._root, value)
    
    def remove_rec(self, node, data):
        if node == None:
            return False
        
        if node._data > data:
            res = self.remove_rec(node._left, data)
        
        if node._data < data:
            res = self.remove_rec(node._right, data)
            
        if node._data == data:
            if node._right != None:
           
                e = self.get_smallest_node(node._right)
                node._data = e._data
                res = self.remove_rec(node._right, e._data)
            elif node._left != None:
                e = self.get_largest_node(node._left)
                node._data = e._data
                res = self.remove_rec(node._left, e._data)
            else:
                res = True
                if node.is_black():
                    node.color_deficit()
                    self.resolve_deficit(node)
                p = node._parent
                
                if p != None:
                    if node == node._parent._right:
                        node._parent._right = None
                    else:
                        node._parent._left = None
                else:
                    self._root = None
                return res
        self.resolve_deficit(node)
        return res
    
    def has_only_black_children(self, node):
        if node == None:
            return True
        return (not node._left or node._left.is_black()) and (not node._right or node._right.is_black())
    
    def resolve_deficit(self, node):
        if node == None or not node.is_deficit():
            return 
        
        if node._parent == None:
            node.color_black()
            return 
        p = node._parent
        s = self.get_sibling(node)
        if s != None and s.is_red():
            if node == p._left:
                self.left_rotate(p)
            else:
                self.right_rotate(p)
            s.color_black()
            p.color_red()
        s = self.get_sibling(node)
        
        if s !=None and self.has_only_black_children(s):
            s.color_red()
            node.color_black()
            if p.is_red():
                p.color_black()
            else:
                p.color_deficit()
        else:
            if node == p._left:
                if s._right != None and s._right.is_black():
                    s.color_red()
                    s = self.right_rotate(s)
                self.left_rotate(p)
            else:
                if s._left != None and s._left.is_black():
                    s.color_red()
                    s = self.left_rotate(s)
                self.right_rotate(p)
            if p.is_red():
                s.color_red()
            else:
                s.color_black()
            p.color_black()
            s._right.color_black()
        
    def contains(self, value: object)-> bool:
        for i in self:
            if i._data ==  value:
                return True
        return False 

    def equals(self, s: set)->bool:
        if s._size != self._size:
            return False
        
        for i in self:
            if s.contains(i._data) == False:
                return False
        return True
        
    def get_element_at(self, index: int)-> object:
        if index < 0:
            return False
        if index >= self._size:
            return False
        result = list()
        l = [self._root]
        while len(l)!= 0:
            n = []
            for i in l:
                result.append(i._data)
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            l = n
        return result[index]


    def get_smallest_element(self) -> object:
        if self._root == None:
            return None
        temp = self._root
        while temp._left != None:
            temp = temp._left
        return temp
        
    def get_largest_element(self) -> object:
        if self._root == None:
            return None
        temp = self._root
        while temp._right != None:
            temp = temp._right
        return temp

    def is_empty(self):
        return self._size == 0

    def empty(self):
        self._root = None
        self._size -=1

    def print(self):
        if self._root == None:
            return
        l = [self._root]
        while len(l)!= 0:
            n = []
            for i in l:
                print(i._data, i._color, " ", end = "")
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            print("")
            l = n
    
    def height(self, n):
        if not n:
            return 0
        return 1 + max(self.height(n._left), self.height(n._right))
    
            
    def get_smallest_node(self, node):
        temp = node
        while temp._left != None:
            temp = temp._left
        return temp
    
    def get_largest_node(self, node):
        temp = node
        while temp._right != None:
            temp = temp._right
        return temp
    
    def __iter__(self):
        self._current_node = self.get_smallest_node(self._root)
        return self
    
    def __next__(self):
        if self._current_node == None:
            raise StopIteration
            
        temp = self._current_node
        
        if self._current_node._right == None:
            p = self._current_node._parent
            while p != None and self._current_node != p._left:
                self._current_node = p
                p = self._current_node._parent
            self._current_node = p
        else:
            self._current_node = self.get_smallest_node(self._current_node._right)   
        return temp
    

class TreeMap(SortedMap):
    class Entry():
        def __init__(self, k = None, v = None, p = None):
            self._key = k
            self._value = v
            self._left = None
            self._right = None
            self._parent = p
    
    def __init__(self):
        self._root = None
        self._size = 0
    
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node._left), self.height(node._right))
    
    
    def right_rotate(self, node):
        p = node._parent
        x = node
        y = node._left
        T = y._right
        y._right = x
        x._parent = y
        x._left = T
        if T:
            T._parent = x
        y._parent = p
        
        if p == None:
            self._root = y
        else:
            if y._key < p._key:
                p._left = y
            else:
                p._right = y
        return y
    
    def left_rotate(self, node):
        p = node._parent
        x = node 
        y = x._right
        T = y._left
        y._left = x
        x._parent = y
        x._right = T
        if T:
            T._parent = x
        y._parent = p
        if p == None:
            self._root = y
        else:
            if y._key < p._key:
                p._left = y
            else:
                p._right = y
        
        return y
    
    def balance(self, node):
        if not node:
            return None
            
        h = self.height(node._left) - self.height(node._right)
        if h > 1:
            lh = self.height(node._left._left) - self.height(node._left._right)
            if lh < 0:
                node._left = self.left_rotate(node._left)
         
            node = self.right_rotate(node)
        
        if h < -1:
            rh = self.height(node._right._left) - self.height(node._right._right)
            if rh > 0:
                node._right = self.right_rotate(node._right)
   
            node  = self.left_rotate(node)

        return node
    
    def put(self, key, value):
        self._root = self.put_helper(self._root, key, value)
    
    def put_helper(self, node, k, v):
        if node == None:
            self._size +=1
            return TreeMap.Entry(k, v)
        
        if k > node._key:
            node._right = self.put_helper(node._right, k, v)
            node._right._parent = node
        
        elif k < node._key:
            node._left = self.put_helper(node._left, k, v)
            node._left._parent = node
            
        return self.balance(node)
    
    
    def get(self, key: object)-> object:
        if self._size == 0:
            return None
        
        current = self._root
        while current._key != key:
            if current._key > key:
                current = current._left
            elif current._key < key:
                current = current._right
            if current == None:
                return False
        return current._value
    
    
    def _get_smallest(self, node):
        temp = node
        while temp._left:
            temp = temp._left
        return temp
    
    
    def remove(self, key: object)-> object:
        if self._size == 0:
            return False
        
        check_key = self.get(key)
        if check_key == False:
            return False
        
        return self._remove_helper(key, self._root)
    
        
    def _remove_helper(self, key, node):
        p = node._parent
        current = node

        while current._key != key:
            if current._key > key:
                p = current
                current = current._left
            elif current._key < key:
                p = current
                current = current._right

        #removing a leaf
        if current._left == None and current._right == None:
            if current._key > p._key:
                p._right = None
            elif current._key < p._key:
                p._left = None
            else:
                p._right = None
                
            self._size-=1
            return current._value 
         
        #removing a node with 1 child 
        if current._left != None and current._right == None:
            k = current._value
            
            if current._key > p._key:
                node = current._left
                p._right = node 
                node._parent = p
                
            elif current._key < p._key:
                node = current._left
                p._left = node
                node._parent = p
                
            else:
                node = current._right
                p._right = node
                node._parent = p
                
            self._size-=1
            return k
        
        elif current._right != None and current._left == None:
            k = current._value
            if current._key > p._key:
                node = current._right
                p._right = node 
                node._parent = p
                
            elif current._key < p._key:
                node = current._right
                p._left = node 
                node._parent = p
                
            else:
                node = current._right
                p._right = node
                node._parent = p
            
            self._size-=1
            return k
  
        #removing a node with 2 children
        if current._right != None and current._left != None:
            sml_node = self._get_smallest(current._right)
            current._key = sml_node._key
            current._value = sml_node._value
            return self._remove_helper(current._key, current._right)
        
        
    
    def keySet(self):
        key_set = set()
        for i in self:
            key_set.add(i._key)
    
        return key_set
    
    def sub_map(self, k1, k2):
        if self._size == 0:
            return None
        set_key = self.keySet()
        
        if k1 not in set_key or k2 not in set_key:
            return False
        
        new_tree = TreeMap()
        l = [self._root]
        while len(l)!= 0:
            n = []
            for i in l:
                new_tree.put(i._key, i._value)
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            l = n
    
        current = new_tree._root
        while current._key != k1:
            if current._key > k1:
                current = current._left
            elif current._key < k1:
                current = current._right

        new_tree._root = current
        set_key_new = new_tree.keySet()
        
        if k2 not in set_key_new:
            return False 
        
        temp = new_tree._root
        
        while temp:
            if temp._key > k2:
                temp._right = None
                temp = temp._left
            elif temp._key < k2:
                temp = temp._right
            else:
                temp._right = None
                temp._left = None
                break
        
        new_tree._size = 0
        
        for i in new_tree:
            new_tree._size+=1
        
     
        return new_tree
        

    def is_empty(self):
        return self._size == 0

    def empty(self):
        self._root = None
        self._size = 0

    def print(self):
        current = self._root
        stack = []
        while True:
            if current:
                stack.append(current)
                current = current._left
            elif len(stack) != 0:
                e = stack.pop()
                print(e._key, ":", e._value)
                current = e._right
            else:
                break
            
    def __iter__(self):
        self._current_node = self._get_smallest(self._root)
        return self
    
    def __next__(self):
        if self._current_node == None:
            raise StopIteration
            
        temp = self._current_node
        
        if self._current_node._right == None:
            p = self._current_node._parent
            while p != None and self._current_node != p._left:
                self._current_node = p
                p = self._current_node._parent
            self._current_node = p
        else:
            self._current_node = self._get_smallest(self._current_node._right)   
        return temp
    
    
    def level_order_print(self):
        if self._root == None:
            return
        l = [self._root]
        while len(l)!= 0:
            n = []
            for i in l:
                print(i._key, " ", end = "")
                if i._left:
                    n.append(i._left)
                if i._right:
                    n.append(i._right)
            print("")
            l = n
            
          
    def is_tree_left_skewed(self):
        cur = self._root
        if cur == None:
            return None 
        
        while cur:
            if cur._right != None:
                return False 
            cur = cur._left
    
        return True 
    
    
    def is_tree_complete(self):
        pass
    
    def get_set_of_unique_values(self):
        values = list()
        value_tree = TreeSet()
        for i in self:
            if i._value not in values:
                values.append(i._value)
        for i in values:
            value_tree.add(i)
    
        return value_tree


class MinPriorityQueue(PriorityQueueADT):
    def __init__(self):
        self._plist = []

    def is_empty(self):
        return len(self._plist) == 0

    def empty(self):
        self._plist = []

    def print(self):
        if len(self._plist) == 0:
            return

        levels = 1
        counter = 1
        line = ""

        for i in self._plist:
            if counter <= levels:
                line = line + " " +  str(i._perf_ind)
                counter +=1
            else:
                print(line)
                line = ""
                counter = 1
                levels = levels * 2
                line = line + " " +  str(i._perf_ind)
                counter +=1
        print(line)

    def enqueue(self, value: object):
        self._plist.append(value)
        i = len(self._plist) - 1

        if i % 2 == 0:
            p = int((i - 2) / 2)
        p = int((i - 1) / 2)

        while p >= 0:
            if self._plist[i] >= self._plist[p]:
                break
            self._plist[i], self._plist[p] = self._plist[p], self._plist[i]
            i = p

            if i % 2 == 0:
                p = int((i - 2) / 2)
            p = int((i - 1) / 2)

    def deque(self) -> object:
        if len(self._plist) == 0:
            return None

        v = self._plist[0]
        self._plist[0] = self._plist[len(self._plist) - 1]
        self._plist.pop()
        i = 0
        l = 2 * i + 1
        r = 2 * i + 2

        while i < len(self._plist):
            min_index = i
            if l < len(self._plist) and self._plist[l] < self._plist[min_index]:
                min_index = l

            if r < len(self._plist) and self._plist[r] < self._plist[min_index]:
                min_index = r

            if min_index == i:
                break

            self._plist[i], self._plist[min_index] = self._plist[min_index], self._plist[i]
            i = min_index
            l = 2 * i + 1
            r = 2 * i + 2

        return v

    def head(self):
        return self._plist[0]


    def getNumberOfEmployeesPerformingAt(self, perf_indicator):
        count = 0
        for i in self._plist:
            if i.perf_ind() == perf_indicator:
                count+=1
        return count


    def _most_left_index(self, index):
        i = index
        while True:
            new_i = 2*i + 1
            if new_i < len(self._plist):
                i = new_i
            else:
                break
        return i

    class InorderIterator:
        def __init__(self, obj):
            self.obj = obj
            self.length = len(self.obj._plist)
            self._plist = self.obj._plist
            self.index = self.obj._most_left_index(0)
            self.visited = list()

        def __next__(self):
            if self.index >= self.length or len(self.visited) >= self.length:
                raise StopIteration

            temp = self.index

            if self.index % 2 == 0:
                p = int((self.index - 2) / 2)

            else:
                p = int((self.index - 1) / 2)

            if 2*self.index + 2 < self.length and 2*self.index + 2!=temp:
                self.index = self.obj._most_left_index(2*self.index + 2)
                self.visited.append(self.index)

            elif 2*p + 1 == self.index:
                self.index = p
                self.visited.append(self.index)

            elif 2*p + 2 == self.index:
                while p in self.visited:
                    if p % 2 == 0:
                        p = int((p - 2) / 2)
                    else:
                        p = int((p - 1) / 2)
                self.index = p
                self.visited.append(self.index)

            return self._plist[temp]

    def __iter__(self):
        return self.InorderIterator(self)

        
     
        
        
     