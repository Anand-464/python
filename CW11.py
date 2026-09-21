from tripdata import trip_details
from datetime import datetime
import json

trips = [trip_details("New York", "10-08-2023", "Great trip!"),
        trip_details("Paris", "15-11-2023", "Loved the food!"),
        trip_details("Tokyo", "05-12-2023", "Amazing culture!")
         ]

for x in trips:
    date_object = datetime.strptime(x["date"], "%d-%m-%Y")
    x["date"] = date_object.strftime("%B %d, %Y")
    
json_data = json.dumps(trips)
print(json_data)