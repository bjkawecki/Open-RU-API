import json
import sqlite3

connection = sqlite3.connect("db.sqlite")

with open("json/courses.json", "r") as json_file:
    data = json.load(json_file)
for item in data[:1]:
    print(item)
