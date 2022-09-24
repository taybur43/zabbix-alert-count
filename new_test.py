from pyzabbix  import ZabbixAPI
import datetime
import time
zapi=ZabbixAPI(server="http://192.168.44.4/zabbix")
try:
   #zapi.login(user="userforapi",password="'Pakkass##18!'")
   zapi.login(user="Admin",password="zabbix")
   print("Yes Connected")
   count=0
except:
   print("Ops getting issue in connecting....")

alert_count=zapi.event.get(groupids=24,value=1,severities=4)
print alert_count
print("going To loop")
for insr in alert_count:
    print insr
    print("i am in the loop")
    if (insr['r_eventid']=='0' and insr['severity']=='5' and insr['value']=='1'):
        count=count+1 
print("second for loop is to  be finished")   
print ("found Disater alert=",count)
count=0
print("new loop starting")
