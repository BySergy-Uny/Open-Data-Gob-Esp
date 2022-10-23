import requests



def get_request():
    url = 'https://datos.gob.es/apidata/catalog/dataset'
    headers = {'Accept': 'application/json'}
    return requests.get(url, headers=headers).content
 
print (get_request())