"""
Huffman encripture algorithms using heaps builded with Nodes
"""

class Node:
    def __init__(self,data,frequency = None):
        self.data = data
        self.left = None
        self.right = None
        self.father = None
        self.in_left = None
        self.in_right = None
        self.frequency = frequency

    def frequency(self):
        return self.frequency

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.right = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.right   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    def dequeue(self):
        if self.is_empty():
            return None
        out_node = self.head          # copy the value to a local variable
        self.head = self.head.right       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return out_node
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

class Min_heap:
    
    def __init__(self, data = None):
        self.root = data
        self.insert_queue = Queue()
        self.size = 0

    def swap(self, node1, node2):
        
        #print('node 1', node1.data, node1.frequency, node1.left, node1.right, node1.father)
        #print('node 2', node2.data, node2.frequency, node2.left, node2.right, node2.father)
        node1.data, node2.data = node2.data, node1.data
        node1.frequency, node2.frequency = node2.frequency, node1.frequency
        #print('node 1', node1.data, node1.frequency, node1.left, node1.right, node1.father)
        #print('node 2', node2.data, node2.frequency, node2.left, node2.right, node2.father)
        
    def insert(self, new_node):
        if not self.root:
            print('not self.root')
            self.root = new_node
            #new_node.left = new_node.right = new_node.father = None
            #print(new_node.data)
            self.insert_queue.enqueue(new_node)
            self.size += 1
            return
        node = self.insert_queue.head
        #print('sup' ,node.data)
        if not node.left:
            print('not node.left')
            new_node.father = node
            node.left = new_node
            self.heapify(new_node)
            self.insert_queue.enqueue(node.left)
            print(node.data)
        elif not node.right:
            print('not node.right')
            #print('hola')
            new_node.father = node
            node.right = new_node
            self.heapify(node.right)
            self.insert_queue.enqueue(node.right)
            self.insert_queue.dequeue()
        print('la dcha', new_node.data, new_node.right)
        print('la dcha', node.data, node.right)
            
        self.size += 1


    def heapify(self,node):
        while node.father:
            if node.frequency < node.father.frequency:
                self.swap(node, node.father)
            else:
                break
        pass
            
    def pop_min(self):
        if not self.root:
            return None
        out_node = self.root
        node = self.root
        while node.right:
            self.swap(node, node.right)
            node = node.right
        if node.left:
            node.swap(node.left, node)
            node.left = None
        else:
            node = None
        self.size -= 1
        return out_node
    
 
    def __repr__(self):
        pass
    
    def bfs(self):
        lista = []
        root = self.root
        lista.append(root)
        visit_order = []
        #for _ in range(5):
        c = 0
        while len(lista) > 0:
            c += 1
            print(len(lista), visit_order)
            node = lista.pop(0)
            print(node.data)
            if node.left:
                print('left', node.left.data)
                lista.append(node.left)
                
            if node.right:
                print('right', node.right.data)
                lista.append(node.right)
                
            visit_order.append(node.data)
        
        return visit_order
    pass
    
data = 'AAAAAAABBBCCCCCCCDDEEEEEE'
dic = {}
#calculamos frecuencias             
for ch in data:
    if ch not in dic:
        dic[ch] = 0
    dic[ch] += 1
    
#metemos nodos en min_heap
min_heap = Min_heap()
for key in dic:
    print(key)
    min_heap.insert(Node(key, dic[key]))
    print(min_heap.bfs())
    print('\n', 'ARBOL' , '\n')

print('##############')
while min_heap.size > 0 :
    print(min_heap.pop_min().data, end = ', ')
print()
print(min_heap.bfs())

    
while min_heap.size > 1:
    
    node_1 = min_heap.pop_min()
    node_2 = min_heap.pop_min()
    print(node_1.data,node_1.frequency,' || ',node_2.data, node_2.frequency)
    in_node = Node(None, node_1.frequency + node_2.frequency)
    in_node.in_left = node_1
    in_node.in_right = node_2
    
    min_heap.insert(in_node)
    
               

               
    
