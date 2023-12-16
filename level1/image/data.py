import json 
import os

def get_path(name_file):
    s = os.getcwd()
    s = os.path.join(s,name_file)
    return s 
def read_json (name_fail):
    name_fail = get_path (name_fail)
    with open (name_fail,"r")as file:
        data = json.load(file)
        return data
    
def write_json (data,name_fail):
    name_fail = get_path(name_fail)
    with open (name_fail,"w")as file:
        json.dump(data,file,indent = 4)
        
notes = {"test1":
         {
             "text":"text1",
             "teg":["teg1","teg2"]

         }}

#write_json(notes,"notes.json")
data = read_json("notes.json")
print(data)
