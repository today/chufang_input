# -*- coding: utf-8 -*-  

import json
import MySQLdb
import os
import sys
#import shutil

def getRecipe( p_no  ):

  try:
      conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
      cur=conn.cursor()
      
      """ 取出病历信息  """
      sql1 = "select json_id from t_patient where  patient_no='"+ p_no + "' order by id desc"
      print sql1
      cur.execute(sql1)
      temp_p_json_id = cur.fetchone()
      print temp_p_json_id
      
      sql2 = "select json_id from t_recipe where  patient_no='"+ p_no + "' order by id desc"
      print sql2
      cur.execute(sql2)
      temp_c_json_id = cur.fetchone()
      print temp_c_json_id

      
        
      conn.commit()
      cur.close()
      conn.close()
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


# 从命令行参数中取 病历号
patient_no = sys.argv[1]

getRecipe( patient_no )

     







