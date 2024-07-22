import json
num = 1 
with open("best_grade.json",'w',encoding='UTF-8') as f:
    f.write(json.dumps(num))
    f.close()