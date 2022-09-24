from pyzabbix  import ZabbixAPI
import datetime
import time
zapi=ZabbixAPI(server="http://192.168.12.3/zabbix")
try
   zapi.login(user="Admin",password="zabbix")
   print("Yes Connected")
   count=0
except:
   print("Ops getting issue in connecting....")
host_group=zapi.hostgroup.get() 
for hgp in host_group:
     print hgp['name']
     test=hgp['groupid']
     #print test
     #count=0
     print("counting event for groupid="+test) 
     alert_count=zapi.event.get(groupids=test,time_from=1543740086)
     print ("going To loop")
     for insr in alert_count:
        print insr
        print("i am in the loop")
        if (insr['r_eventid']=='0' and insr['severity']=='5' and insr['value']=='1'):
            count=count+1 
	print("second for loop is to  be finished")   
     print ("found Disater alert=",count)
     
     count=0
     print("new loop starting")
