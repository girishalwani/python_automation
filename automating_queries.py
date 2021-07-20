import os
import re
os.chdir('practice_codes') #E:\python\practice_codes
parent=os.getcwd()

dir = os.path.join(parent,"queries.txt")

print(dir)

final_dir = os.path.join(parent,"final_query_output.txt")

print(final_dir)



file=open(dir,"r")
data=file.read()
print(data)
spl=data.split("\n")
print(spl)

value=[]

for i in spl:
    stage=i.replace("'","''")
    value.append(stage)

file2=open(final_dir,"r+")
for each in value:
    stage = "('curation','data_asset',{value},'time')\n".format(value=each)
    #print(stage)
    final=re.sub(r"\bbdh_curation_stage\b", "%stage_db_name%", stage)
    final = re.sub(r"\btable_name\b", "%table_name%", final)
    final = re.sub(r"\bbdh_analytic_cid\b", "%database_name%", final)
    final = re.sub(r"\bstge_table_name\b", "%stage_table_name%", final)
    print(final)
    file2.write(final)

print(value)
print(value[1])
print(file2.read())


file.close()
