# -*- coding: utf-8 -*-  
import codecs
import json
import MySQLdb
import os
import sys
#import shutil

def get_p( p_no  ):
  bigJson = ""
  try:
      conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
      cur=conn.cursor()
      
      """ 取出病人信息的Json_id  """
      sql1 = "select json_id from t_patient where  patient_no='"+ p_no + "' order by id desc"
      #print sql1  
      cur.execute(sql1)
      result=cur.fetchone()
      if result:
        temp_p_json_id = result[0]
      
        """ 取出病人信息的Json串 """
        sql3 = "select json_string from t_json where  id='"+ str(temp_p_json_id) + "' "
        cur.execute(sql3)
        result=cur.fetchone()
        bigJson = result[0]
      else:
        bigJson = "{}"  
        
      conn.commit()
      cur.close()
      conn.close()
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

  return bigJson

def get_c( c_no ):
  bigJson = ""
  try:
      conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
      cur=conn.cursor()
      
      """ 取出处方信息的Json_id  """
      sql1 = "select json_id from t_recipe where  recipe_no='"+ c_no + "' "
      #print sql1  
      cur.execute(sql1)
      result=cur.fetchone()
      if result:
        temp_c_json_id = result[0]
      
        """ 取出Json串 """
        sql3 = "select json_string from t_json where  id='"+ str(temp_c_json_id) + "' "
        cur.execute(sql3)
        result=cur.fetchone()
        bigJson = result[0]
      else:
        bigJson = "{}"  
        
      conn.commit()
      cur.close()
      conn.close()
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

  return bigJson 


if len(sys.argv) < 3 :
  print 'usage: python db.py cmd param  \n  cmd is a command( load_p|save_p|load_r|save_r ). param is a number or SQL string.'
  exit()

# 从命令行参数中取 参数
param_no = sys.argv[2]

#json_str = get_p( param_no )
json_str = get_c( param_no )

reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'  

print json_str.decode('utf-8')


     







