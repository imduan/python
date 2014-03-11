#!/usr/bin/python
# coding: utf-8

import sys
from datetime import *
import time
import urllib
import urllib2
import httplib 
import json
import codecs
import MySQLdb

def getDep(seq):
  try:
    exeSql='select * from ttt where seq =\'{0}\''.format(seq);
    #print exeSql
    conn=MySQLdb.connect(host='192.168.1.1',user='ddd',passwd='ddddd',db='dddtab',port=1231)
    cur=conn.cursor()
    cur.execute(exeSql)
    rows = cur.fetchall()
    if(len(rows) == 1):
     #print rows[0][0]
     return rows[0][0]
  except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return None

#ret = getDep('23ass')
#if(ret == 'ddd'):
# print 'ddd'
#elif(ret == 'dd'):
# print 'bb'
#else:
# print 'none'

