import pandas as pd
import json
from datetime import datetime, timedelta

# Generate passenger manifest CSV
passengers = [
    {"passenger_id": "P001", "name": "James Wilson", "cabin": "A123", "dining_preference": "Early", "age": 45, "nationality": "British"},
    {"passenger_id": "P002", "name": "Elena Rodriguez", "cabin": "B145", "dining_preference": "Late", "age": 32, "nationality": "Spanish"},
    {"passenger_id": "P003", "name": "Sarah Chen", "cabin": "A125", "dining_preference": "Early", "age": 28, "nationality": "Chinese"},
    {"passenger_id": "P004", "name": "Michael Brown", "cabin": "C201", "dining_preference": "Late", "age": 52, "nationality": "American"},
    {"passenger_id": "P005", "name": "Lisa Thompson", "cabin": "B147", "dining_preference": "Early", "age": 39, "nationality": "Canadian"}
]

# Generate key card access logs JSON
base_time = datetime(2024, 2, 20, 19, 0)  # Crime occurred around 8 PM
card_logs = []
for hour in range(5):  # Generate 5 hours of logs
    for passenger in passengers:
        if passenger["passenger_id"] != "P003":  # Create suspicious absence
            card_logs.append({
                "timestamp": (base_time + timedelta(hours=hour)).strftime("%Y-%m-%d %H:%M:%S"),
                "passenger_id": passenger["passenger_id"],
                "location": "Dining Hall" if hour in [1, 2] else "Cabin",
                "action": "entry" if hour % 2 == 0 else "exit"
            })

# Generate dining transactions CSV
dining_transactions = [
    {"transaction_id": "T001", "passenger_id": "P001", "item": "Seafood Platter", "amount": 45.99, "timestamp": "2024-02-20 19:30:00"},
    {"transaction_id": "T002", "passenger_id": "P002", "item": "Vegetarian Pasta", "amount": 28.50, "timestamp": "2024-02-20 20:15:00"},
    {"transaction_id": "T004", "passenger_id": "P004", "item": "Steak", "amount": 52.99, "timestamp": "2024-02-20 20:00:00"},
    {"transaction_id": "T005", "passenger_id": "P005", "item": "Fish Special", "amount": 38.99, "timestamp": "2024-02-20 19:45:00"}
]

# Save to files
pd.DataFrame(passengers).to_csv("passenger_manifest.csv", index=False)
pd.DataFrame(dining_transactions).to_csv("dining_transactions.csv", index=False)
with open("card_access_logs.json", "w") as f:
    json.dump(card_logs, f, indent=2)

print("Files generated successfully!")