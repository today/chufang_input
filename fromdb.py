# -*- coding: utf-8 -*-  
import codecs
import json
import MySQLdb
import os
import shutil
import sys

import mydb

def getRecipe( p_no  ):
  bigJson = ""
  try:
      p_json = mydb.getPatientJson( p_no )

      conn = mydb.getConn()
      cur=conn.cursor()
      
      """ 取出病历信息的 Json_id  """
      sql2 = "select json_id from t_recipe where  patient_no='"+ p_no + "' order by id desc"
      print sql2
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

      """ 所有的Json都取出来了，现在需要拼接字符串了。 """
      full_p_json = '"patients":' + p_json 
      all_c_json = '  '
      for temp_str in c_json_list :
        all_c_json += temp_str + ','
      bigJson = '{ '+ full_p_json + ',' + '"cases":[' + all_c_json[0:-1] + ']' +' }'
      
        
      conn.commit()
      cur.close()
      conn.close()

      print bigJson 
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

  return bigJson

def cp_img():
  for file in os.listdir('old_photos/'): 
    if not os.path.exists('../FRT_aid/img/' + file ):
      shutil.copyfile( 'old_photos/' + file , '../FRT_aid/img/' + file) 



if len(sys.argv) < 2 :
  print 'usage: python getHistory.py patients_no   \n  patients_no is a list of patients number.'
  exit()

# 从命令行参数中取 病历号
patient_no = sys.argv[1]

all_json = "[ "
no_list = patient_no.split(',')
for p_no in no_list:
  p_json_str = getRecipe( p_no )
  all_json += p_json_str + ','


"""  将字符串写入文件  """
json_file = codecs.open('../FRT_aid/data/for_doctor.json','w','utf-8')
json_file.write(all_json[0:-1] + ']')
json_file.close()

cp_img()


     







