# Task 1: Data Loading & Initial Inspection

# Load required libraries
import pandas as pd
import json
from datetime import datetime

# Load card access logs
with open('../generate_data/card_access_logs.json', 'r') as f:
    card_logs = json.loads(f.read())
card_logs_df = pd.DataFrame(card_logs)
card_logs_df['timestamp'] = pd.to_datetime(card_logs_df['timestamp'])

# Load passenger manifest and dining data
passenger_df = pd.read_csv('../generate_data/passenger_manifest.csv')
dining_df = pd.read_csv('../generate_data/dining_transactions.csv')
dining_df['timestamp'] = pd.to_datetime(dining_df['timestamp'])

# Display first few rows of each dataset
print("Card Access Logs:")
print(card_logs_df.head())
print("\nPassenger Manifest:")
print(passenger_df.head())
print("\nDining Transactions:")
print(dining_df.head())

# Task 2: Establishing Timeline (7 PM - 9 PM)
# Filter card access logs for 7-9 PM
timeline_mask = (card_logs_df['timestamp'].dt.hour.between(19, 21))
timeline_df = card_logs_df[timeline_mask].sort_values('timestamp')

# Filter dining transactions for 7-9 PM
dining_mask = (dining_df['timestamp'].dt.hour.between(19, 21))
dining_timeline = dining_df[dining_mask].sort_values('timestamp')

# Create combined timeline
timeline_df['event_type'] = 'access'
dining_timeline['event_type'] = 'dining'

combined_timeline = pd.concat([
    timeline_df[['timestamp', 'passenger_id', 'location', 'action', 'event_type']],
    dining_timeline[['timestamp', 'passenger_id', 'item', 'amount', 'event_type']]
]).sort_values('timestamp')

print("Combined Timeline of Events (7-9 PM):")
print(combined_timeline)

# Task 3: Identifying Anomalies
# Get passengers in dining hall during 8 PM hour
dining_hall_8pm = card_logs_df[
    (card_logs_df['timestamp'].dt.hour == 20) &
    (card_logs_df['location'] == 'Dining Hall')
]['passenger_id'].unique()

# Get passengers with dining transactions during 8 PM hour
diners_8pm = dining_df[
    dining_df['timestamp'].dt.hour == 20
]['passenger_id'].unique()

# Find anomalies
in_hall_no_purchase = set(dining_hall_8pm) - set(diners_8pm)
purchase_no_entry = set(diners_8pm) - set(dining_hall_8pm)

print("Passengers in dining hall without purchases:", in_hall_no_purchase)
print("Passengers with purchases but no entry record:", purchase_no_entry)

# Get all passenger IDs
all_passengers = passenger_df['passenger_id'].unique()
missing_passengers = set(all_passengers) - set(dining_hall_8pm) - set(diners_8pm)

print("Passengers missing from both logs:", missing_passengers)

# Task 4: Location Analysis
# Focus on 8 PM timeframe
time_8pm = '2024-02-20 20:00:00'

# Get passenger locations at 8 PM
locations_8pm = card_logs_df[
    (card_logs_df['timestamp'] <= time_8pm)
].sort_values('timestamp').groupby('passenger_id').last()

# Get suspicious movement patterns (multiple entries/exits)
movement_patterns = card_logs_df[
    (card_logs_df['timestamp'].dt.hour.between(19, 21))
].groupby('passenger_id').agg({
    'action': 'count',
    'location': lambda x: len(x.unique())
}).reset_index()

suspicious_movements = movement_patterns[
    (movement_patterns['action'] > 2) |  # More than 2 swipes
    (movement_patterns['location'] > 1)   # Multiple locations
]

print("Passenger Locations at 8 PM:")
print(locations_8pm[['location', 'action']])
print("\nSuspicious Movement Patterns:")
print(suspicious_movements)

# Task 5: Final Analysis
# Combine all suspicious indicators
suspicious_indicators = pd.DataFrame(index=passenger_df['passenger_id'])

# Indicator 1: No dining purchase but in dining hall
suspicious_indicators['no_purchase'] = suspicious_indicators.index.isin(in_hall_no_purchase)

# Indicator 2: Suspicious movement patterns
suspicious_indicators['suspicious_movement'] = suspicious_indicators.index.isin(suspicious_movements['passenger_id'])

# Indicator 3: Near dining hall location (assuming A cabins are near)
suspicious_indicators['near_dining'] = passenger_df.set_index('passenger_id')['cabin'].str.startswith('A')

# Calculate suspicion score
suspicious_indicators['suspicion_score'] = suspicious_indicators.sum(axis=1)

# Get most suspicious passenger(s)
most_suspicious = suspicious_indicators[suspicious_indicators['suspicion_score'] == suspicious_indicators['suspicion_score'].max()]

# Get their details
suspect_details = passenger_df[passenger_df['passenger_id'].isin(most_suspicious.index)]

print("Most Suspicious Passenger(s):")
print(suspect_details)
print("\nSuspicion Indicators:")
print(suspicious_indicators.loc[most_suspicious.index])