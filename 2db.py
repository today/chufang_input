# -*- coding: utf-8 -*-  

import json
import MySQLdb
import os
#import shutil

def saveRecipe( recipe ):
  patientObj = recipeObject['patients']
  caseObj = recipeObject['case']
  

  #caseJson = json.dumps(caseObj, ensure_ascii=False,indent=2)
  caseJson = json.dumps(caseObj, ensure_ascii=False)
  patientJson = json.dumps(patientObj,ensure_ascii=False)
  print caseJson
  print patientJson

  try:
      conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306,db='frt', charset='utf8')
      cur=conn.cursor()
      
      """ json串插入数据库  """
      sql1 = "insert into t_json (json_string) values ('"+ patientJson + "')"
      cur.execute(sql1)
      temp_p_json_id = conn.insert_id()
      
      sql2 = "insert into t_json (json_string) values ('"+ caseJson + "')"
      cur.execute(sql2)
      temp_c_json_id = conn.insert_id()

      """  患者信息插入数据库  """
      sql3 = "insert into t_patient (patient_no, patient_name, sex, age, mobile, comment, json_id) values " \
            + "('" + patientObj['patient_no'] + "','" + patientObj['name'] \
            + "','" + patientObj['sex'] + "','"+patientObj['age'] \
            + "','"+patientObj['phone_no'] + "','"+patientObj['comment'] + "','" + str(temp_p_json_id) +"'); " 
      cur.execute(sql3)
      temp_p_id = conn.insert_id()

      """  处方信息插入数据库  """
      sql4 = "INSERT INTO `t_recipe` ( `recipe_no`, `patient_id`, `patient_name`, " \
            + "`mobile`, `dingxing`, `dingbing`, `dingzheng`, `comment`, " \
            + "`suitnum`, `json_id`) VALUES " \
            + " ( '"+ caseObj['case_no'] + "', '" + str(temp_p_id) +"', '"+ patientObj['name'] \
            + "', '"+ patientObj['phone_no'] + "', '" + caseObj['dingxing'] + "', '"+ caseObj['dingbing'] \
            + "', '"+ caseObj['dingzheng'] +"', '"+ caseObj['comment'] +"', '"+ caseObj['suitnum'] \
            + "', '"+ str(temp_c_json_id) +"' )"
      cur.execute(sql4)
      temp_c_id = conn.insert_id()

      """  循环插入处方中的药物信息  """
      itemObjs = caseObj['recipe']
      for i in range(0, len(itemObjs)-1):
        itemObj = itemObjs[i];
        sql5 = "INSERT INTO `t_recipe_item` (recipe_id, medicine, count, unit, remark ) VALUES ('" \
              + str(temp_c_id) + "', '" + itemObj['medicine'] + "', '" + str(itemObj['count']) + "', '" \
              + itemObj['unit'] + "', '"+ itemObj['remark'] + "' )"
        print sql5
        cur.execute(sql5)
        
        print  conn.insert_id()

   
      conn.commit()
      cur.close()
      conn.close()
   
  except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

all_the_text = ""
if os.path.exists( 'data/case/c2014-5-27_1.json' ) :
  file_object = open('data/case/c2014-5-27_1.json')
  try:
      all_the_text = file_object.read()
      recipeObject = json.loads( all_the_text)

      print recipeObject

      saveRecipe( recipeObject )

      # 处理完的文件，移动到另外的文件夹
      os.rename('data/case/c2014-5-27_1.json','data/case_saved/c2014-5-27_1.json')

  finally:
       file_object.close( )
else:
  print "file not exist."






