from tracker import record
from datetime import datetime
import json

travel = [record("New York", "10-08-2023", "Great trip!"),
        record("Paris", "15-11-2023", "Loved the food!"),
        record("Tokyo", "05-12-2023", "Amazing culture!")
         ]

for x in travel:
    date_object = datetime.strptime(x["date"], "%d-%m-%Y")
    x["date"] = date_object.strftime("%B %d, %Y")

json_string = json.dumps(travel)
print(json_string)

travel_dict = json.loads(json_string)
print(travel_dict)

for record in travel_dict:
    print(f"City: {record['city']}"
          f"Date: {record['date']}"
          f"Comment: {record['comment']}"
          )