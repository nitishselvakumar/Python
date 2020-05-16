import json

file = open("Read.JSON", "r")
json_data = file.read()
obj = json.loads(json_data)
_id = []
email = []
first_name = []
last_name = []
avatar = []
for i in obj['data']:
    _id.append(i['id'])
    email.append(i['email'])
    first_name.append(i['first_name'])
    last_name.append(i['last_name'])
    avatar.append(i['avatar'])
print(obj['page'])
print(obj['per_page'])
print(obj['total'])
print(obj['total_pages'])
print(_id)
print(email)
print(first_name)
print(last_name)
print(avatar)
