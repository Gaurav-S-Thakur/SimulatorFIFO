class MinHeap(object):
    def __init__(self, elem = [], size = float("Inf")):
        self.elem = []
        self.num = len(self.elem)
        self.limit = size
        
    def isEmpty(self):
        if self.num>0:
            return False
        return True

    def heapify_up(self, index):
        parent = index/2
        lc = 2*parent if 2*parent < self.num else None
        rc = 2*parent+1 if 2*parent+1 < self.num else None
        smallest = parent
        if lc and (self.elem[lc] < self.elem[parent]):
            smallest = lc
        if rc and (self.elem[rc] < self.elem[smallest]):
            smallest = rc
        if not (smallest == parent):        
            temp = self.elem[smallest]
            self.elem[smallest] = self.elem[parent]
            self.elem[parent] = temp
            self.heapify_up(parent)

    def heapify_down(self, index):
        lc = 2*index if 2*index < self.num else None
        rc = 2*index+1 if 2*index+1 < self.num else None
        smallest = index
        if lc and (self.elem[lc] < self.elem[index]):
            smallest = lc
        if rc and (self.elem[rc] < self.elem[smallest]):
            smallest = rc
        if not (smallest == index):
            temp = self.elem[smallest]
            self.elem[smallest] = self.elem[index]
            self.elem[index] = temp
            self.heapify_down(smallest)            

    def add(self,new_elem):
        if self.num < self.limit:
            self.elem.append(new_elem)
            self.num+=1
            self.heapify_up(self.num-1)

    def min(self):
        if not self.isEmpty():
            return self.elem[0]

    def extractMin(self):
        temp = self.elem[0]
        self.elem[0] = self.elem[self.num-1]
        self.elem[self.num-1] = temp
        min_elem = self.elem.pop(self.num-1)
        self.num -= 1
        self.heapify_down(0)
        return min_elem

    def printer(self):
        print self.elem
