# -*- coding: utf-8 -*-  
import codecs
import json
import MySQLdb
import os
import sys
#import shutil

def getRecipe( p_no  ):

  try:
      conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
      cur=conn.cursor()
      
      """ 取出病人信息的Json_id  """
      sql1 = "select json_id from t_patient where  patient_no='"+ p_no + "' order by id desc"
      #print sql1  
      cur.execute(sql1)
      result=cur.fetchone()
      temp_p_json_id = result[0]
      #print temp_p_json_id

      """ 取出病人信息的Json串 """
      sql3 = "select json_string from t_json where  id='"+ str(temp_p_json_id) + "' "
      cur.execute(sql3)
      result=cur.fetchone()
      p_json = result[0]
      #print p_json
      
      """ 取出病历信息的 Json_id  """
      sql2 = "select json_id from t_recipe where  patient_no='"+ p_no + "' order by id desc"
      #print sql2
      cur.execute(sql2)
      allResult=cur.fetchall()
      """ 循环取出每一份病历的json串  """
      c_json_list = []
      for result in allResult:
        temp_c_json_id = result[0]
        #print temp_c_json_id

        sql4 = "select json_string from t_json where  id='"+ str(temp_c_json_id) + "' "
        cur.execute(sql4)
        ajson = cur.fetchone()
        c_json_list.append(ajson[0])
        #print c_json
        
      conn.commit()
      cur.close()
      conn.close()
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

  """ 所有的Json都取出来了，现在需要拼接字符串了。 """
  full_p_json = '"patients":' + p_json 
  all_c_json = '  '
  for temp_str in c_json_list :
    all_c_json += temp_str + ','
  bigJson = '{ '+ full_p_json + ',' + '"cases":[' + all_c_json[0:-1] + ']' +' }'
  print bigJson

  """  将字符串写入文件  """
  json_file = codecs.open('for_doctor.json','w','utf-8')
  json_file.write(bigJson)
  json_file.close()


if len(sys.argv) < 2 :
  print 'usage: python getHistory.py patients_no   \n  patients_no is a list of patients number.'
  exit()

# 从命令行参数中取 病历号
patient_no = sys.argv[1]

getRecipe( patient_no )

     







