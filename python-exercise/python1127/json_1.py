

#json 格式由列表和字典组成
import json

data ={
    "name":["jerry",'nick'],
    "age":26,
    "gender":"female"
}

data1 = json.dumps(data)