import json

employee = {"page": 2, "per_page": 6, 'total': 12, 'total_pages': 2}
d1 = {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
      "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg"}
d2 = {"id": 6, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
      "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg"}
d3 = {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
      "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg"}
d4 = {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
      "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg"}
d5 = {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
      "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg"}
d6 = {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
      "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg"}
employee['data'] = [d1, d2, d3, d4, d5, d6]
employee['ad'] = {"company": "StatusCode Weekly", "url": "http://statuscode.org/",
                  "text": "A weekly newsletter focu…he stack end of things."}

f = open("Write.txt", "w", encoding="utf-8")
json.dump(employee, f, ensure_ascii=False)
f.close()
