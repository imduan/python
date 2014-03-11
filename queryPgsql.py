#!/usr/bin/python
# coding: utf-8
import psycopg2
import sys
import os
from datetime import *
import time
import urllib
import urllib2
import httplib 
import json
import codecs
import smtplib
from email.MIMEText import MIMEText

def queryDb():
 
 conn = psycopg2.connect(database="qunar_group", user="doubhor", password="2a31590f-20e1-4d28-8af1-a30495f60e5f", host="l-tuandb2.s.cn6", port="5432")
 cur = conn.cursor()

 offset = 0;
 while(1):
   exeSql="SELECT * from tddg where action=1 and to_timestamp(ac_time)>='{0}'".format('2014-03-05')
   cur.execute(exeSql)
   rows = cur.fetchall()
   offset += 100
   if(len(rows) <= 0):
     break
   for row in rows:
    print row[0]
