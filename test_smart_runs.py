import requests
import json
def get_esri_matrix(waypoints, depart_time='now',url='https://mihqww25.us.dominos.com/arcgis/rest/services/Routing/NetworkAnalysis/NAServer/OriginDestinationCostMatrix/solveODCostMatrix?'):
    #convert seconds to milliseconds
    if depart_time != 'now':
        depart_time = depart_time*1000
    order_list = list(waypoints.keys())
    stop_list = [{'attributes' : {'Name' : key}, 'geometry' : {'x' : value[1], 'y' : value[0]}} for key,value in waypoints.items()]
    locations = {'features' : stop_list}
    odcm_data = {'Origins' : json.dumps(locations),
                 'Destinations' : json.dumps(locations),
                 #'Restrictions': ['["Driving an Automobile","Through Traffic Prohibited","Roads Under Construction Prohibited","Avoid Carpool Roads"]'],
                 #'Attribute_Parameter_Values' : json.dumps({'features' : [{'attributes' : {"OBJECTID": 66,"AttributeName": "Driving an Automobile","ParameterName": "Restriction Usage","ParameterValue": "AVOID_HIGH"}}]}),
                 'travelMode': '1',
                 'accumulateAttributeNames':'Miles',
                 #'outputType' : 'esriNAODOutputNoLines',
                 #'timeOfDay': depart_time, #unix time in milliseconds
                 'f': 'json'}
    response = requests.post(url, data=odcm_data, verify=False)
    data = response.json()
    if 'error' in data.keys():
        raise Exception(data['error'])
        error(data['error'])
    matrix = {k:v for k,v in  data['odCostMatrix'].items() if k != 'costAttributeNames'}
    order_map = {str(order_list.index(o)+1) : o for o in order_list}
    order_dict = {order_map[origin] : {order_map[destination] : list(map(lambda x: round(x,2), travels)) for destination, travels in values.items()} for origin, values in matrix.items()}
    return order_dict



waypoints = {'1': (32.4683991, -85.09634419999999),
 '2': (32.4683991, -85.09634419999999),
 '3': (32.4683991, -85.09634419999999),
 '4': (32.4683991, -85.09534419999999),
 'store': (32.474, -85.031)}

data = get_esri_matrix(waypoints)
print(data)

answer = {'1': {'1': [0, 0],
  '2': [0, 0],
  '3': [0, 0],
  '4': [0.02, 0.0],
  'store': [6.96, 4.24]},
 '2': {'1': [0, 0],
  '2': [0, 0],
  '3': [0, 0],
  '4': [0.02, 0.0],
  'store': [6.96, 4.24]},
 '3': {'1': [0, 0],
  '2': [0, 0],
  '3': [0, 0],
  '4': [0.02, 0.0],
  'store': [6.96, 4.24]},
 '4': {'1': [0.02, 0.0],
  '2': [0.02, 0.0],
  '3': [0.02, 0.0],
  '4': [0, 0],
  'store': [6.98, 4.24]},
 'store': {'1': [7.71, 4.29],
  '2': [7.71, 4.29],
  '3': [7.71, 4.29],
  '4': [7.73, 4.29],
  'store': [0, 0]}}





data == answer