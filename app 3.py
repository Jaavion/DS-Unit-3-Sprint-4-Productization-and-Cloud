from flask import Flask
import requests
URL = 'https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25'
location='pm25'
PARAMS = {'address':location}
r=requests.get(url=URL, params=PARAMS)
data = r.json()
lat_time = data['results'][0]['date']
dall = {}
dall.update(lat_time)
dall.pop('local')
dal_val = data['results'][0]['value']
dal_val = str(dal_val)
dal_val = {'value':dal_val}
dall.update(dal_val)
lat_time_2 = data['results'][1]['date']
dall2 = {}
dall2.update(lat_time_2)
dal_val_2 = data['results'][1]['value']
dal_val_2 = str(dal_val_2)
dal_val_2 = {'value':dal_val_2}
dall2.pop('local')
dall2.update(dal_val_2)
lat_time_3 = data['results'][2]['date']
dall3 = {}
dall3.update(lat_time_3)
dall3.pop('local')
dal_val_3 = data['results'][3]['value']
dic_val_3 = {'value':dal_val_3}
dall3.update(dic_val_3)
lat_time_4 = data['results'][3]['date']
dall4 = {}
dall4.update(lat_time_4)
dall4.pop('local')
dal_val_4 = data['results'][3]['value']
dic_val_4 = {'value':dal_val_4}
dall4.update(dic_val_4)
lat_time_4 = data['results'][4]['date']
dall5 = {}
dall5.update(lat_time_4)
dall5.pop('local')
dal_val_5 = data['results'][4]['value']
dic_val_5 = {'value':dal_val_5}
dall5.update(dic_val_5)
dall6 = {'1': dall, '2':dall2, '3': dall3, '4': dall4, '5': dall5}
dall6=str(dall6)

app = Flask(__name__)

@app.route('/')
def func():
    return dall6

