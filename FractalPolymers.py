import cmath
import numpy as np
import matplotlib.pyplot as plt

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data, node1, node2):
        new_node = Node(data, node2)
        node1.set_next(new_node)

    def tail(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count, current
    
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
    
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
class fractal(LinkedList):
    def __init__(self, llist = None):
        self.graph = llist
        self.start = llist.head
        self.size, self.end = llist.tail()
            
    def evolve(self):
        path = self.graph
        x, y = path.head, path.head.next_node
        for i in range(self.size - 1):
            angle =(np.random.rand()<0.5) * np.pi/4.2 #+ (2*np.random.rand()-1)*np.pi/40
            #angle = 30*np.pi/180.0
            z_rot = 1.0/2.0/np.cos(angle)*(np.cos(angle) + 1j*np.sin(angle))
            newpoint = x.data+(y.data-x.data)*z_rot
            #newpoint = x.data*y.data
            path.insert(newpoint, x, y)
            x, y = y, y.get_next()
            self.size += 1
        
    def show(self):
        x = self.graph.head
        for _ in range(self.size):
            print x.data
            x = x.get_next()
    
    def toPoints_(self):
        x = self.graph.head
        l = self.size
        r = np.zeros([l,2])
        for i in range(l):
            r[i,0], r[i,1] = np.real(x.data), np.imag(x.data)
            x = x.get_next()
        return r
    
        
if __name__ == "__main__":
    a = Node(1.0 + 1.0j)
    b = Node(1.0 + 0.0j)
    a.set_next(b)
    graph = LinkedList(a)
    poly = fractal(graph)
    for gen in range(10):
        plt.cla()
        poly.evolve()
        R = poly.toPoints_()
        plt.plot(R[:,0], R[:,1])
        plt.title('Generation #: ' + str(gen))
        start, end = a.data, b.data
        xs, ys = np.array([np.real(start), np.real(end)]), np.array([np.imag(start), np.imag(end)])
        plt.scatter(xs, ys)
        plt.pause(0.2)
        plt.show()
    
    