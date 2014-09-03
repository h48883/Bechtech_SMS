#!/usr/bin/env python
#coding:utf-8
import time
import urllib
import csv
import pycurl


class BechSMS(object):
    '''Send short message in batch with BechTech ID'''
    
    def __init__(self,accesskey,secretkey):
        self.__accesskey=accesskey
        self.__secretkey=secretkey
        self.__readcontent()
        self.__readphone()
    
    def __readcontent(self):
        myfile=open('content.txt','r')
        self.__content=myfile.read()
        myfile.close()
    
    def __readphone(self):
        self.phonenumber=[]
        with open('mobile.csv','rb') as f:
            reader=csv.reader(f)
            for line in reader:
                self.phonenumber+=line
    
    def __curl(self):
        c=pycurl.Curl()
        c.setopt(pycurl.URL,self.url)
        c.perform()
        c.close()
    
    def send(self):
        for phone in self.phonenumber:
            params={
                'accesskey':self.__accesskey,
                'secretkey':self.__secretkey,
                'mobile':phone,
                'content':self.__content
                }
            self.url='http://sms.bechtech.cn/Api/send/data/json?%s' %(
                urllib.urlencode(params))
            self.__curl()
            print phone
            time.sleep(.2)


if __name__=="__main__":
    accesskey="" #your accesskey
    secretkey="" #your secretkey
    SMS=BechSMS(accesskey,secretkey)
    SMS.send()
