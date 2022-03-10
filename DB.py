from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
import json
import ast
import pandas as pd
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import *

def getCityList():
    client = MongoClient(url)
    db = client["Intern"]
    collection = db["Intern_Data"]
    return json.dumps(collection.distinct('city'))

def getStatus(_id):
    client = MongoClient(url)
    db = client["Intern"]
    collection = db["taskModel"]
    return json.dumps(collection.find_one({"_id" : ObjectId(_id)}, {'_id' : 0 , 'status' : 1}))

def convertToPDF(jsonInp, ids, name):
    d = {}
    for i,j in list(zip(jsonInp,ids)):
        d[str(j['_id'])] = ast.literal_eval(str(i))

    dataframe = pd.DataFrame.from_dict(d, orient="index")
    dataframe.to_excel(name+".xlsx")
    w = Workbook(name+".xlsx")
    w.save(name+"PDF.pdf", SaveFormat.PDF)

def filterCity(cons):
    client = MongoClient(url)
    db = client["Intern"]
    collection = db["Intern_Data"]
    ids = collection.find({'city' : cons}, {'_id' : 1})
    ans = collection.find({'city' : cons}, {'_id' : 0})
    convertToPDF(ans, ids, "Test1")

url = "mongodb+srv://JR-Admin:Prateek1234@bot-a-thon2-0.fkae4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

#filterCity("jaipur")
#getStatus("62298eed67b1e24171b612aa")
#getCityList()
