from heap import MinHeap

def test1():
    minhp = MinHeap()
    for idx in range(10):
        minhp.add(idx+1)
        minhp.add(20-idx)
    minhp.printer()
    
    for idx in range(20):
        print minhp.extractMin()
        #minhp.printer()

def test2():
    minhp = MinHeap()
    print minhp.isEmpty()
    minhp.add(1)
    minhp.add(1)
    minhp.add(1)
    minhp.printer()
    print minhp.extractMin()
    print minhp.extractMin()

test1()
