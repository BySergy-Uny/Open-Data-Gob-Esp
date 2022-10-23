from urllib.parse import urlencode
import requests
import re


def get_request(options):
    url = 'https://datos.gob.es/apidata/catalog/dataset'
    headers = {'Accept': 'application/json'}
    return requests.get(url + options, headers=headers).content

def search_datasets_by_keyword(keyword):
    options = "/keyword/" + keyword
    return get_request(options)

print (search_datasets_by_keyword("telefonia"))