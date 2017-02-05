from fifoServer import FIFOSimulator
from fifoServer import Statistician

def test1():
    simulator = FIFOSimulator()
    simulator.run(5)
    stat = Statistician(simulator.results("get"))
    
def main():
    test1()
    
if __name__=="__main__":
    main()
    