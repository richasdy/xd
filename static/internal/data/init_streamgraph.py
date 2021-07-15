import json

file_name='5_OneCatSevNumOrdered_wide'
pk = 0
new_list = []

with open('{}.json'.format(file_name)) as json_data:
    d = json.load(json_data)    
    for item in d:
        pk+=1
        item = {"model": "internal.streamgraph", "pk": pk, "fields": item}
        new_list.append(item)
        json_data.close()


def list_to_json_file(list_of_dicts, file_name):
    with open(file_name+'.json', 'w') as file:
        json.dump(list_of_dicts, file)
    print('{}.Json file created'.format(file_name))


list_to_json_file(new_list, 'db_streamgraph')