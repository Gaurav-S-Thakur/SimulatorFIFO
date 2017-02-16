from fifoServer import FIFOSimulator
from fifoServer import Statistician

import numpy as np
import sys
import matplotlib.pyplot as plt


def test1():
    simulator = FIFOSimulator()
    simulator.run(10)
    simulator.results("print")
    print ("\n-------------------------------------------------------------\n")
    stat = Statistician(simulator.results("get"))
    stat.run()
    
def test2(epochs, num_served, arr, serv, seed):
    collector = []
    headline = "Avg_Service_delay,Max_Service_delay,Min_Total_Delay,Avg_Total_Delay,Max_Total_Delay,Avg_Queue_length,Processor_Idle_Time\n"
    
    for epoch in xrange(epochs):
        try:
            simulator = FIFOSimulator(arr,serv,mean)
            simulator.run(num_served)
            stat = Statistician(simulator.results("get"))
            collector.append(stat.run())
        except:
            print ("Simulation Error")
    with open("stats.csv","w") as fw:
        fw.write(headline)
        for stat in collector:
            strstat = [str(x) for x in stat]
            data = ",".join(strstat)
            fw.write(data)
            fw.write("\n")
        
def test3():
    avg_service_delay = []
    process_queue_length = []
    rho = []
    for serv_time in xrange(1,101):
        param1 = []
        param2 = []
        rho.append(float(serv_time)/100)
        for seed in xrange(1,20):
            try:
                simulator = FIFOSimulator(10,float(serv_time)/10,seed)
                simulator.run(2000)
                stat = Statistician(simulator.results("get"))
                data = stat.run()
                avg_serv_delay = data[0]
                process_queue_len = data[5]
                #param1.append(avg_serv_delay)
                #param2.append(process_queue_len)
                param1.append(avg_serv_delay)
                param2.append(process_queue_len)
            except:
                print ("Simulation Error")
        avg_service_delay.append(np.mean(np.array(param1)))
        process_queue_length.append(np.mean(np.array(param2)))
    headline="Rho,Avg_service_delay,Avg_processQueue_length"
    with open("rhoplots.csv","w") as fw:
        fw.write(headline)
        fw.write("\n")
        for idx in xrange(len(rho)):
            strstat = [str(rho[idx]),str(avg_service_delay[idx]),str(process_queue_length[idx])]
            data = ",".join(strstat)
            fw.write(data)
            fw.write("\n")
    """
    import pdb; pdb.set_trace()
    f, axarr = plt.subplots(2, 1)
    axarr[0, 0].plot(rho, avg_service_length)
    axarr[0, 0].set_title('Rho vs Average Service Waiting Delay')
    axarr[0, 1].scatter(rho, process_queue_length)
    axarr[0, 1].set_title('Rho vs Process Waiting Queue Length')
    plt.show()
    """

def test4():
    processor_idle_time = []
    rho = []
    for serv_time in xrange(1,101):
        param1 = []
        rho.append(float(serv_time)/100)
        for seed in xrange(1000,10000,1000):
            try:
                simulator = FIFOSimulator(10,float(serv_time)/10,seed)
                simulator.run(2000)
                stat = Statistician(simulator.results("get"))
                data = stat.run()
                param1.append(data[6])
            except:
                print ("Simulation Error")
        processor_idle_time.append(np.mean(np.array(param1)))
    headline="Rho,Avg_processor_idleTime"
    #import pdb; pdb.set_trace()
    with open("rhoplotidle.csv","w") as fw:
        fw.write(headline)
        fw.write("\n")
        for idx in xrange(len(rho)):
            strstat = [str(rho[idx]),str(processor_idle_time[idx])]
            data = ",".join(strstat)
            fw.write(data)
            fw.write("\n")    
        
def main():
    if len(sys.argv)<3:
        test3()
        #test4()
        #test1()
        
main()
    