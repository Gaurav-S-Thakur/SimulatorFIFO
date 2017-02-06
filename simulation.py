from fifoServer import FIFOSimulator
from fifoServer import Statistician

def test1():
    simulator = FIFOSimulator()
    simulator.run(5)
    simulator.results("print")
    print ("\n-------------------------------------------------------------\n")
    stat = Statistician(simulator.results("get"))
    stat.run()
    
def test2(epochs, num_served):
    collector = []
    headline = "Avg_Service_delay,Max_Service_delay,Min_Total_Delay,Avg_Total_Delay,Max_Total_Delay,Avg_Queue_length,Processor_Idle_Time\n"
    
    for epoch in xrange(epochs):
        simulator = FIFOSimulator()
        simulator.run(num_served)
        stat = Statistician(simulator.results("get"))
        collector.append(stat.run())
    with open("stats.csv","w") as fw:
        fw.write(headline)
        for stat in collector:
            strstat = [str(x) for x in stat]
            data = ",".join(strstat)
            fw.write(data)
            fw.write("\n")
        
        
def main():
    test2(10,10)
    
if __name__=="__main__":
    main()
    