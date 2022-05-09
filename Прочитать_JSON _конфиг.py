import json

with open('personal.json', 'r', encoding='utf-8') as f:
    a = json.load(f)

for txt in a['personal']:
    print(txt['name'],':',txt['salary'])