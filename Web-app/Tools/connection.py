from urllib.parse import urlencode
import requests
import json


def get_request(options):
    url = 'https://datos.gob.es/apidata/catalog/dataset'
    headers = {'Accept': 'application/json'}
    return requests.get(url + options, headers=headers).content

def search_datasets_by_keyword(keyword):
    options = "/keyword/" + keyword
    return get_request(options)

def load_json(data):
    return json.loads(data)

def format_json(data):
    return json.dumps(load_json(data), indent=4)

def get_items_of_search(data):
    list_result_with_format = dict()
    json_obj = load_json(data)
    for item in json_obj["result"]["items"]:
        description = ""
        for description_obj in item['description']:
            description = description_obj["_value"]
            if (description_obj["_lang"] == "es"):
                description = description_obj["_value"]
                break
        description = description.split(".")[0]
        list_result_with_format[description] = []
        for distribution_item in item['distribution']:
            if (distribution_item["format"]["value"] == "text/csv"):
                title = ""
                url = distribution_item["accessURL"]
                for title_obj in distribution_item['title']:
                    if (title_obj["_lang"] == "es"):
                        title = title_obj["_value"]
                        distributon_item_obj = dict()
                        distributon_item_obj["title"] = title
                        distributon_item_obj["url"] = url
                        list_result_with_format[description].append(distributon_item_obj)
    return list_result_with_format    

req = search_datasets_by_keyword("telefonia")
result = get_items_of_search(req)

print(json.dumps(result, indent=4))

# Example requests
# print (format_json(req))
