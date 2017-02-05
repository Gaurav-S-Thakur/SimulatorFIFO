import matplotlib as plt
import numpy as np

from utilities import Calendar
from utilities import Event_Record
from utilities import Data_Record


class FIFOSimulator(object):
    def __init__(self,preflag = False):
        self.isidle = True
        self.process_queue = []
        self.cal = Calendar()
        self.clock = 0
        self.dataset = {}
        self.pre_gen = preflag

    def schedule(self, record):
        if not self.pre_gen:
            if record.event_type == "A":
                record.timestamp = self.clock + int(np.random.normal(10,5))
            else:
                record.timestamp = self.clock + int(np.random.normal(12,6))
            self.cal.add(record)
            
    def load_calendar(self):
        with open("calendar.txt","r") as fp:
            for line in fp:
                vals = line.split(" ")
                self.cal.add(Event_Record(int(vals[0]),vals[1],int(vals[2])))
                
    def results(self,command):
        if command == "get":
            return self.dataset
        elif command == "print":
            num = len(self.dataset.keys())
            #import pdb; pdb.set_trace()
            for idx in xrange(num):
                print str(idx)+"\tArr: "+str(self.dataset[idx].arrival)+"\tServ: "+str(self.dataset[idx].service)+"\tDep: "+str(self.dataset[idx].depart)
        else:
            "Invalid Command. Use 'get' or 'print' options."
        
    def run(self,N):
        #Simulation till N processes have been served
        currpid = -1
        arrival_pid = 0
        served_pid = 0
        self.schedule(Event_Record(arrival_pid, "A"))
        arrival_pid +=1
        if self.pre_gen:
            self.load_calendar()
        while (served_pid < N):
            event = self.cal.getlatest()
            #print "Curr:"+str(currpid)+" Served:"+str(served_pid)
            #print event
            self.clock = event.timestamp
            currpid = event.pid
            if event.isArrival():
                # Arrival Handler
                self.dataset[currpid] = Data_Record(currpid,self.clock)
                self.schedule(Event_Record(arrival_pid, "A"))
                arrival_pid+=1
                if self.isidle:
                    self.schedule(Event_Record(currpid, "E"))
                    self.dataset[currpid].service = self.clock
                    self.isidle= False
                else:
                    self.process_queue.append(currpid)
            else:
                self.dataset[currpid].depart = self.clock
                served_pid +=1
                if len(self.process_queue):
                    currpid = self.process_queue.pop(0)
                    self.dataset[currpid].service = self.clock
                    self.schedule(Event_Record(currpid, "E"))
                else:
                    self.isidle = True

class Statistician(object):
    def __init__(self,data=None):
        self.dataset = data
        
    def analyzeDelay(self):
        servicedelay = []
        totaldelay = []
        num = len(self.dataset)
        for index in xrange(num):
            record = self.dataset[index]
            servicedelay.append(record.service - record.arrival)
            totaldelay.append(record.depart - record.arrival)
        min_serv_del = min(servicedelay)
        max_serv_del = max(servicedelay)
        min_tot_del = min(totaldelay)
        max_tot_del = max(totaldelay)
        avg_service_delay = float(sum(servicedelay))/num
        avg_total_delay = float(sum(totaldelay))/num
        return [min_serv_del, max_serv_del, avg_service_del, min_tot_del, max_tot_del, avg_total_del]
    
    def get_time_series(self):
        arrivals = []
        departs = []
        num = len(self.dataset)
        for idx in xrange(num):
            record = self.dataset[idx]
            arrivals.append(record.arrival)
            departs.append(record.depart)
        counter = 0
        #print "Arrivals:\t"+str(arrivals)
        #print "Departures:\t"+str(departs)
        idx1 = 0
        idx2 = 0
        timeline = [(0,0)]
        while(idx1 < num and idx2 < num):
            if arrivals[idx1]<departs[idx2]:
                counter +=1
                idx1 +=1
                timeline.append((arrivals[idx1-1],counter))
            else:
                counter -=1
                idx2 +=1
                timeline.append((departs[idx2-1],counter))
        return timeline
    
    def average_quelen(self,timeline):
        
        
    def get_proc_utile(self,timeline):
        

    def analyzeUtilizationParams(self):
        timeline = self.get_time_series()
        avg_quelen = self.average_quelen(timeline)
        processor_utilisation = self.get_proc_util(timeline)
    
    def run(self):
        delay_params = self.analyzeDelay()
        count_params = self.analyzeUtilizationParams()