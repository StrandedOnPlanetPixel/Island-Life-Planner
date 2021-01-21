import json

with open('villagers.json', 'r') as f:
    jsondict = json.load(f)

for el in jsondict:
    # Delete all the keys!!!
    el.pop('id', None)
    el.pop('file-name', None)
    el.pop('personality', None)
    el.pop('species', None)
    el.pop('gender', None)
    el.pop('subtype', None)
    el.pop('hobby', None)
    el.pop('catch-phrase', None)
    el.pop('icon_uri', None)
    el.pop('image_uri', None)
    el.pop('bubble-color', None)
    el.pop('text-color', None)
    el.pop('saying', None)
    el.pop('catch-translations', None)

    # Re-add name key, but as a single string
    nameArray = el['name']
    name = nameArray['name-USen']
    el['name'] = name

sortedJson = sorted(jsondict, key=lambda item: item['name'])
print(sortedJson)

with open('sorted-villagers.json', 'w') as outfile:
    json.dump(sortedJson, outfile)