from pyzabbix  import ZabbixAPI
import datetime
import time
import sqlite3
import sched
import threading
from login import conn
zapi=conn()
print("connecting to sqlite database...")
#db = sqlite3.connect('/root/sqlite_db/test.db')
s = sched.scheduler(time.time, time.sleep)
def collection():
 host_group=zapi.hostgroup.get()
 #print host_group
 for hgp in host_group:
    grp_name=hgp['name']
    modified_grp=grp_name.replace(' ','-')
    new_grpname=modified_grp.replace('-','_')
    test=hgp['groupid'] 
    problem_count=zapi.problem.get(groupids=test,severities=4,recent=False,source=0,acknowledged=False,countOutput=True)
    print("{} group id {} is = {}".format(new_grpname,test,problem_count))
    data_insertion(new_grpname,problem_count)
 print("Going To Sleep For 60Miniute")
 threading.Timer(3600, collection).start()

def data_insertion(grpname,total_prob):
   db = sqlite3.connect('/root/sqlite_db/test.db')
   print grpname
   print("checking Table existance if not exist then creating this one")
   cursor = db.cursor()
   #cursor.execute("create table if not exists %s (id INTEGER  PRIMARY KEY AUTOINCREMENT, Disaster_alert INTEGER,time INTEGER)" %(grpname)) 
   print("inserting the value....")
   ticks = int(time.time())
   cursor.execute("insert into %s(Disaster_alert,time)values (?,?)"%(grpname),(total_prob,ticks))
   db.commit()

def main():
  collection()
if __name__ == '__main__':
  main()
