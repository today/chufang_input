# -*- coding: utf-8 -*-  

import codecs 
import json
import MySQLdb
import os
import sys
#import shutil

def saveNewRecipe( recipe_str ):
  
  # json 串转 py  对象
  caseObj = json.loads(recipe_str)
  #setDefValue( patientObj, ('patient_no','name','sex','age','phone_no','comment') )
  setDefValue( caseObj, ( 'mobile','dingxing','dingbing' , 'dingzheng','suitnum','comment') )
  

  try:
      conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
      cur=conn.cursor()
      
      """ json串插入数据库  
      sql1 = "insert into t_json (json_string) values ('"+ patientJson + "')"
      cur.execute(sql1)
      temp_p_json_id = conn.insert_id()    """
      
      sql2 = "insert into t_json (json_string) values ('"+ recipe_str + "')"
      cur.execute(sql2)
      temp_c_json_id = conn.insert_id()

      """  患者信息插入数据库  
      sql3 = "insert into t_patient (patient_no, patient_name, sex, age, mobile, comment, json_id) values " \
            + "('" + patientObj['patient_no'] + "','" + patientObj['name'] \
            + "','" + patientObj['sex'] + "','"+patientObj['age'] \
            + "','"+  patientObj['phone_no'] + "','" \
            + patientObj['comment'] + "','" + str(temp_p_json_id) +"'); " 
      cur.execute(sql3)
      temp_p_id = conn.insert_id()     """

      """  处方信息插入数据库  """
      sql4 = "INSERT INTO `t_recipe` ( `recipe_no`, `patient_id`, `patient_no`, " \
            + "`patient_name`, `mobile`, `age`, `sex`, `patient_comment`, " \
            + "`dingxing`, `dingbing`, `dingzheng`, `comment`, " + "`suitnum`, `json_id`) VALUES " \
            + " ( '"+ caseObj['case_no'] + "', '" + "0" +"', '" + caseObj['patient_no']  \
            + "', '" + caseObj['patient_name'] + "', '"+ caseObj['mobile'] + "', '" + caseObj['age']  \
            + "', '" + caseObj['sex'] + "', '"+ caseObj['patient_comment'] + "', '" + caseObj['dingxing']  \
            + "', '"+ caseObj['dingbing'] + "', '"+ caseObj['dingzheng'] +"', '"+ caseObj['comment']  \
            + "', '"+ caseObj['suitnum'] + "', '"+ str(temp_c_json_id) +"' )"
      #print sql4
      cur.execute(sql4)
      temp_c_id = conn.insert_id()

      """  循环插入处方中的药物信息  """
      itemObjs = caseObj['recipe']
      for i in range(0, len(itemObjs)-1):
        itemObj = itemObjs[i];
        sql5 = "INSERT INTO `t_recipe_item` (recipe_id, medicine, count, unit, remark ) VALUES ('" \
              + str(temp_c_id) + "', '" + itemObj['medicine'] + "', '" + str(itemObj['count']) + "', '" \
              + itemObj['unit'] + "', '' )"
        #print sql5
        cur.execute(sql5)
      
      # 删除原有数据
      # 删除 t_json 表中的数据
      sql6 = "DELETE  FROM t_json WHERE id in ( select json_id from t_recipe WHERE recipe_no='" \
                                              + caseObj['case_no'] + "' AND id != '" + str(temp_c_id) + "')"
      print sql6
      cur.execute(sql6)

      # 删除 t_recipe 表中的数据
      sql7 = "DELETE  FROM t_recipe WHERE recipe_no='" + caseObj['case_no'] + "' AND id != '" + str(temp_c_id) + "'"
      print sql7
      cur.execute(sql7)

      conn.commit()
      cur.close()
      conn.close()
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def setDefValue( aDict, akey_list ):
  for akey in akey_list :
    if not aDict.has_key( akey ):
      aDict[akey] = ''

      

all_the_text = ""
jsonfilename = 'data/' + sys.argv[1]
print jsonfilename

if os.path.exists( jsonfilename) :
  file_object = open(jsonfilename)
  try:
      all_the_text = file_object.read()
      # 为了去除BOM 不得不做的检查。
      if all_the_text[:3] == codecs.BOM_UTF8: 
          print "has BOM , Process it ." 
          all_the_text = all_the_text[3:] 
      #print all_the_text
      
      saveNewRecipe( all_the_text )

      # 处理完的文件，移动到另外的文件夹
      #os.rename( jsonfilename, 'data/case_saved/' + sys.argv[1])
  # except Exception as inst:
  #     print type(inst)     # the exception instance
  #     print inst.args      # arguments stored in .args
  #     print inst           # __str__ allows args to printed directly
      
  finally:
       file_object.close( )
else:
  print "FRT Error : file not exist. filename:" + jsonfilename








