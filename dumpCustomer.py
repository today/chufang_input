# -*- coding: utf-8 -*-  
import codecs
import json
import MySQLdb
import os
import shutil
import sys

def dumpToJson( ):
  bigJson = ""
  try:
      conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
      cur=conn.cursor( cursorclass=MySQLdb.cursors.DictCursor )
      cur.execute('SELECT * FROM t_customer ORDER BY id DESC ')
      rs = cur.fetchall()
      
        
      bigJson = json.dumps(rs, ensure_ascii=False,indent=2)
      cur.close()
      conn.close()
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

  return bigJson




if len(sys.argv) != 1 :
  print 'usage: python dumpCustomer.py '
  exit()

# 


all_json =  dumpToJson(  )



"""  将字符串写入文件  """
json_file = codecs.open('./allCustomer.json','w','utf-8')
json_file.write(all_json)
json_file.close()


     







