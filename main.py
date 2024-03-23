from Collections import *

print("Single Linked List")

l_list = LinkedList()

l_list.addFirst(-9)
l_list.addFirst(0)
l_list.addLast(3)
l_list.addFirst(2)
l_list.addFirst(1)
l_list.addLast(4)
l_list.addFirst(0)
l_list.addLast(8)
l_list.addLast(26)
l_list.addLast(0)
l_list.addLast(72)
l_list.addLast(55)
l_list.addLast(100)

l_list.removeFirst()
l_list.removeLast()
print("Forward Iterator")
for i in l_list:
    print(i)


print("Odd Position Iterator")
for i in l_list.odd_iterator():
    print(i)

print("\nDouble linked list\n")
d_list = DoubleLinkedList()
d_list.addLast(0)
d_list.addFirst(1)
d_list.addFirst(2)
d_list.addFirst(3)
d_list.addLast(8)
d_list.addLast(56)
d_list.replace(8, 9)

d_list.print()


print("\nStack\n")
l_stack = LinkedListStack()
l_stack.push(0)
l_stack.push(1)
l_stack.push(2)
l_stack.push(3)
l_stack.push(4)
l_stack.pop()

for i in l_stack:
    print(i)
l_stack.empty()
l_stack.print()

print("\n\nReverse")


def reverse(l, data=list()):
    if l.is_empty() or l.first() == l.last():
        first = l.first()
        l.removeFirst()
        for i in data:
            l.addLast(i)
        l.addLast(first)
        return l

    last = l.last()
    l.removeLast()
    data.append(last)

    reverse(l, data)


reverse(l_list)
l_list.print()




print("\nDoubleLinkedListDeque")
d_deque = DoubleLinkedListDeque()
d_deque.enqueue(1)
d_deque.enqueue(2)
d_deque.enqueue(3)
d_deque.left_enqueue(4)
d_deque.left_enqueue(5)
d_deque.left_enqueue(6)
d_deque.left_enqueue(10)
d_deque.enqueue(8)

d_deque.dequeue()
d_deque.right_dequeue()
d_deque.swap(4, 1)

for i in d_deque:
    print(i)



print("\nArrayDeque")
arr_deque = ArrayDeque()
arr_deque.enqueue(1)
arr_deque.enqueue(2)
arr_deque.enqueue(3)
arr_deque.enqueue(4)
arr_deque.enqueue(5)
arr_deque.enqueue(6)
arr_deque.enqueue(7)
arr_deque.enqueue(8)
arr_deque.enqueue(9)
arr_deque.enqueue(10)
arr_deque.dequeue()
arr_deque.dequeue()
arr_deque.dequeue()
arr_deque.enqueue(11)
arr_deque.enqueue(12)
arr_deque.dequeue()

for i in arr_deque:
    print(i)
print("\n")
arr_deque.swap(9, 11)

for i in arr_deque:
    print(i)



def queue_test(queue_list):
    print("\n______________ <Queue> ____________\n")
    d = queue_list()
    result1 = d.enqueue(1)
    result2 = d.enqueue(2)
    result3 = d.enqueue(3)
    result4 = d.enqueue(4)
    
    size = d._size
    result_enq = d.enqueue(5)
    
    print("Checking whether the element has been Added or not")
    if result_enq == True and size+1 == d._size:
        print("\t PASS: the element has been added\n")
    else:
        print("\t FAIL: there is no space. Please, wait!\n")
    
    size = d._size
    result_removing = d.dequeue()
    
    print("Checking whether the element has been Removed or not")
    if result_removing != None and size-1 == d._size:
        print("\t PASS: the element has been removed\n")
    else:
        print("\t FAIL: Something went wrong or the deque is empty!\n")
    
    
    swap_check = d.swap(4, 2)
    
    print("Checking whether the elements have been Swapped or not")
    if swap_check == True:
        print("\t PASS: the elements has been swapped\n")
    else:
        print("\t FAIL: Either the queue is empty or the stack doesn't have selected element!\n")


    print("Returning the Front an Back elements")
    front = d.front()
    back = d.back()
    if front != None and back != None:
        print(f"\t PASS: Front element: {front}\n\t\t   Back element: {back}\n")
    else:
        print("\t FAIL: The queue is empty\n")
        
   
    new_first = 6
    size = d._size
    left_enq = d.left_enqueue(new_first)
        
    print("Checking whether the element has been Added to the left or not")
    if left_enq == True and size+1 == d._size and d.front() == new_first:
        print("\t PASS: the element has been added to the left\n")
    else:
        print("\t FAIL: Something went wrong!\n")
        
 
    size = d._size
    removing_right = d.right_dequeue()
        
    print("Checking whether the element has been Removed from right or not")
    if removing_right != None and size-1 == d._size:
        print("\t PASS: the element has been removed from the right\n")
    else:
        print("\t FAIL: Something went wrong or the deque is empty!\n")
        
        
    print("Iterating over the elements")
    iter_result = iter(d)
    while True:
        try:
            if d._size != 0:
                print(next(iter_result))
            else:
                print("\t FAIL: The queue is empty and cannot be iterated\n")
                break
        except StopIteration:
            print(f"\t PASS: The Iteration has been successfully completed\n")
            break   
         
        
queue_test(ArrayDeque)
 

def hashset_test():
    print("\n______________ <Hash Set> ____________\n")
    h = HashSet()
    add = h.add(6)
    new_size = h._size
    
    print("Checking whether the element has been added")
    if add == True and new_size == 1:
        print("\t PASS: the element has been added\n")
    else:
        print("\t FAIL: Something went wrong!\n")
     
    
    h.add(16)
    h.add(17)
    h.add(7)
    h.add(9)
    h.add(0)
    h.add(10)
    h.add(20)
    h.add(3)
    h.add(13)
    h.add(4)
    h.add(5)
    
    new_size = h._size
    rem = h.remove(88)
    
    print("Checking whether the element has been removed")
    if rem == True and h._size == new_size - 1:
        print("\t PASS: the element has been removed\n")
    else:
        print("\t FAIL: Something went wrong!\n")
      
    cont = h.contains(3)
    print("Checking whether the element is in hash set")
    if cont == True:
        print("\t PASS: the element is in the Hash Set\n")
    else:
        print("\t FAIL: The element is not in the Hash Set!\n")
    
    k = HashSet()
    k.add(16)
    k.add(6)
    k.add(7)
    k.add(17)
    k.add(9)
    k.add(10)
    k.add(20)
    k.add(0)
    k.add(3)
    k.add(4)
    k.add(5)
    
    equal = h.equals(k)
    print("Checking whether the sets are equal")
    if equal == True:
        print("\t PASS: the sets are equal!\n")
    else:
        print("\t FAIL: The element are not equal!\n")
    
    index = h.get_element_at(4)
    print("Checking whether the element in the given index is returned ")
    if index ==False:
        print("\t FAIL: may be wrong index is given!\n")
    else:
        print(f"\t PASS: element at given position is {index}!\n")
    
    empt = h.empty()
    emp_check = h.is_empty()
    print("Checking whether the hash set is empty after empty() method")
    if emp_check == True and h._size == 0:
        print("\t Pass: The hash set is empty!\n")
    else:
        print("\t Fail: The hash set is not empty!\n")


hashset_test()


def hashmap_test():
    print("\n______________ <Hash Map> ____________\n")
    
    h = HashMap()
    h.put("Jane", 29)
    new_size = h._size
    
    print("Checking whether the element has been added")
    if new_size == 1:
        print("\t PASS: the element has been added!\n")
    else:
        print("\t FAIL: Either something went wrong or the old value has updated!\n")
    

    h.put("Jack", 30)
    h.put("Ann", 15)
    h.put("Lucy", 19)
    h.put("Mary", 17)
    h.put("Bob", 38)
    h.put("Tom", 20)
    h.put("Jerry", 35)
    h.put("Mike", 20)
    h.put("Kety", 46)
    h.put("Rosa", 49)
    h.put("Dina", 27)
    h.put("Lili", 55)
    h.put("Nare", 28)
    h.put("Brent", 22)
    h.put("Zayn", 36)
    
    new_size = h._size
    h.remove("Zayn")
    
    print("Checking whether the element has been Removed or not")
    if new_size-1 == h._size:
        print("\t PASS: the element has been removed!\n")
    else:
        print("\t FAIL: Either Something went wrong or wrong key is given!\n")
    
    
    get = h.get("Brent")
    
    print("Checking whether the get() method returns a value")
    if get == False:
        print("\t FAIL: Either Something went wrong or wrong key is given!\n")
    else:
        print(f"\t PASS: The value of given key is {get}!\n")
    
    
    keySet = h.keySet()
    
    print("Checking whether the keySet() method returns all keys")
    if len(keySet) == h._size:
        print(f"\t PASS: The keys are {keySet}!\n")
    else:
        print("\t FAIL: Something went wrong!\n")
    
    
    print("Checking whether the Iteration workss\n")
    hh = iter(h)
    count = 0
    
    while True:
        try:
            print(next(hh))
            count+=1
        except StopIteration:
            break
    
    
    if count == h._size:
        print(f"\n\t PASS: All the entries are returned!\n")
    else:
        print("\t FAIL: Something went wrong!\n")
    
    
    empt = h.empty()
    emp_check = h.is_empty()
    print("Checking whether the hash map is empty after empty() method")
    if emp_check == True and h._size == 0:
        print("\t Pass: The hash map is empty!\n")
    else:
        print("\t Fail: The hash map is not empty!\n")
        
    print("____________AVL_____________")

    tm = TreeMap()
    tm.put(20, "Jane")
    tm.put(17, "Bob")
    tm.put(14, "Tom")
    tm.put(12, "Jack")
    tm.put(11, "Jack")
    tm.put(13, "Nare")
    tm.put(15, "Helly") 
    tm.put(16, "Justien")
    tm.put(28, "Mary")
    tm.put(26, "Harry")
    tm.put(27, "Harry")
    tm.put(35, "Jane")
    tm.put(38, "Bob")
    tm.put(37, "Tom")
    tm.put(36, "Lucy")
    tm.put(40, "Nare")
    tm.put(39, "Helly") 
    tm.put(42, "Justien")


    tm.remove(17)
    tm.remove(14)
    tm.remove(20)
    tm.remove(35)
    tm.remove(39)


    value_tree = tm.get_set_of_unique_values()

    print("Level Order Print for Tree Map\n")
    tm.level_order_print()

    print("\nItearation for Tree Map\n")

    for i in tm:
        print(i._key, i._value)

    print("\nLevel Order Print for Sub Map\n")
    t = tm.sub_map(15, 13)
    t.level_order_print()

    print("____________RED BLACK_____________")
    rd = TreeSet()
    rd.add(24)
    rd.add(12)
    rd.add(28)
    rd.add(25)
    rd.add(26)
    rd.add(27)
    rd.add(29)
    rd.add(30)

    rd.remove(29)
    rd.remove(12)
    print("\nLevel Order Print for Tree Set\n")
    rd.print()
    print("size", rd._size)

    print("\nChecking contains method:", rd.contains(27))
    print("Largest:", rd.get_largest_element()._data)
    print("Smallest:", rd.get_smallest_element()._data)

       
    rd2 = TreeSet()
    rd2.add(24)
    rd2.add(28)
    rd2.add(25)
    rd2.add(26)
    rd2.add(27)
    rd2.add(30)

    print("Checking whether 2 sets are equal:", rd.equals(rd2))
    print("Getting element in a given index:", rd.get_element_at(5))

hashmap_test()






















