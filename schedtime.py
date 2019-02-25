#!/usr/bin/python
import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(): 
    s.enter(5, 1, print_time, ())  
    print "From print_time", time.time()

def print_some_times():
    print time.time()
    s.enter(5, 1, print_time, ())        
    s.run()

print_some_times()