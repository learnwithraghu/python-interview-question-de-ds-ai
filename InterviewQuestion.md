# Cruise Ship Investigation Challenge

## Background
A theft has occurred on the luxury cruise ship 'SS Data' around 8 PM. As the ship's data analyst, you need to analyze the available data to identify suspicious activities and potential suspects.

## Setup
Clone this repository which contains:
- passenger_manifest.csv
- card_access_logs.json
- dining_transactions.csv

## Investigation Tasks

### Task 1: Data Loading & Initial Inspection
**Question**: Load all three datasets and display the first few rows of each. Make sure to handle timestamps appropriately.
[Cell for loading data]

### Task 2: Establishing Timeline
**Question**: Between 7 PM and 9 PM, create a timeline of all passenger movements (entries/exits) and dining transactions. Display this in a clear, chronological format.
[Cell for timeline analysis]

### Task 3: Identifying Anomalies
**Question**: Find passengers who were in the dining hall during the incident (8 PM) but didn't make any dining transactions. Also identify any passengers who made dining transactions but have no record of entering the dining hall.
[Cell for anomaly detection]

### Task 4: Location Analysis
**Question**: Cross-reference the passenger manifest with the access logs to identify:
- Passengers who were in suspicious locations at 8 PM
- Passengers who made unusual movement patterns (multiple entries/exits)
Display your findings with supporting evidence.
[Cell for location analysis]

### Task 5: Final Analysis
**Question**: Based on your findings from tasks 1-4, identify the most suspicious passenger(s) and explain your reasoning. Support your conclusion with data from all three sources.
[Cell for final analysis and conclusion]