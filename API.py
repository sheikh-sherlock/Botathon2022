import requests
from flask import Flask, request
from DB import *
import os

app = Flask(__name__)

@app.route('/')
def f():
    return "Hello to this API for Botathon 2022"

#/start?url=-------------
'''
Recieve url and send to COL
Return task _id
'''
@app.route('/start')
def sendToCOL():
    url = request.args.get('url', method = ['GET'])
    r = requests.get('https://agile-beyond-69978.herokuapp.com/api/v1/start?url='+url)
    if r.status_code == 200:
        return r.json
    return r.status_code


#/status?id=-------------
'''
Return status of given task _id
'''
@app.route('/status')
def statusToApp():
    _id = request.args.get('id', method = ['GET'])
    status = getStatus(_id)
    return status


#/cities
'''
Return distinct cities
'''
@app.route('/cities')
def cityListToApp():
    return getCityList()


#/pdf?city=----------
'''
Return pdf link
'''
@app.route('/pdf')
def cityPDF():
    city = request.args.get('city', method = ['GET'])
    link = filterCity(city)
    return link


if __name__ == '__main__':
    app.run(debug=True)
