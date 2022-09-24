#!/usr/bin/python
from pyzabbix  import ZabbixAPI
def conn():
 zapi=ZabbixAPI(server="http://zabbix.test.com/zabbix")
 #zapi=ZabbixAPI(server="http://192.168.112.3/zabbix")
 #zapi=ZabbixAPI(server="http://zabbix-test.test.com/zabbix")
 try:
    zapi.login(user="user_name",password="password")
    #zapi.login(user="Admin",password="zabbix")
    print("Yes Connected")
 except:
    print("Ops getting issue in connecting....")

 return zapi


