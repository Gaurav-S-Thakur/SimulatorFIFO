from heap import MinHeap


class Event_Record(object):
    def __init__(self, pid, typ, timestamp=None):
        self.event_type = typ
        self.pid = pid
        self.timestamp = timestamp 
    
    def __str__(self):
        string = "PID: "+str(self.pid)+", Event_Type: "+str(self.event_type)+", Timestamp: "+str(self.timestamp)
        return string
                
    def isArrival(self):
        if self.event_type == "A":
            return True
        return False

class Calendar(object):
    def __init__(self):
        self.events = MinHeap()
        self.mapper = {}

    def add(self, record):
        self.events.add(record.timestamp)
        if record.timestamp in self.mapper:
            self.mapper[record.timestamp].append(record)
        else:
            self.mapper[record.timestamp]=[record]

    def getlatest(self):
        rec_time = self.events.extractMin();
        rec_list = self.mapper[rec_time]
        # Logic here decides how to handle simultaneous events.
        # Current Implementation - extract departure events first
        record = None
        index = -1
        for idx in range(len(rec_list)):
            if rec_list[idx].event_type == "E":
                index = idx
                break
        if index < 0:
            record = rec_list.pop(0)
        else:
            record = rec_list.pop(index)
        if not len(rec_list):
            del self.mapper[rec_time]
        return record    

class Data_Record(object):
    def __init__(self,pid,arrival=None,service=None,depart=None):
        self.pid = pid
        self.arrival = arrival
        self.service = service
        self.depart = depart
        
    def __str__(self):
        string = "PID: "+str(self.pid)+", Arrival: "+str(self.arrival)+", Service: "+str(self.service)+", Depart: "+str(self.depart)
        return string