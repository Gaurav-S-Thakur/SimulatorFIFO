from utilities import Calendar
from utilities import Event_Record

def test1():
    cal = Calendar()
    cal.add(Event_Record(0,"A",1))
    cal.add(Event_Record(1,"A",4))
    cal.add(Event_Record(0,"E",2))
    cal.add(Event_Record(1,"E",10))
    cal.add(Event_Record(2,"A",5))
    cal.add(Event_Record(3,"A",8))
    cal.add(Event_Record(2,"E",12))
    cal.add(Event_Record(3,"E",15))
    while not(cal.events.isEmpty()):
        print cal.getlatest()
    
test1()
    