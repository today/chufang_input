# -*- coding: utf-8 -*-  
import codecs
import json
import MySQLdb
import os
import sys
#import shutil

def getConn():
  conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
  return conn

def getPatientJson( patientNo ):
  conn = getConn()
  cur=conn.cursor( cursorclass=MySQLdb.cursors.DictCursor )
  
  """ 取出病人信息  """
  sql1 = "select * from t_customer where  patient_no='"+ patientNo + "' order by id desc"
  print sql1  
  cur.execute(sql1)
  result=cur.fetchone()
  bigJson = json.dumps(result, ensure_ascii=False,indent=2)
  cur.close()
  conn.close()
  return bigJson
     





print getPatientJson( '07557' )

