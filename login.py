#!/usr/bin/python
from pyzabbix  import ZabbixAPI
def conn():
 zapi=ZabbixAPI(server="http://zabbix.valmet.com/zabbix")
 #zapi=ZabbixAPI(server="http://192.168.112.3/zabbix")
 #zapi=ZabbixAPI(server="http://zabbix-test.valmet.com/zabbix")
 try:
    zapi.login(user="jklrahamta",password="ECE@1109043BJIT#")
    #zapi.login(user="Admin",password="zabbix")
    print("Yes Connected")
 except:
    print("Ops getting issue in connecting....")

 return zapi


