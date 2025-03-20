# Cruise Ship Investigation Challenge

## Background
Dive into a real-world-inspired scenario: a theft has occurred aboard a luxurious cruise ship, and you’re tasked with cracking the case. Using Python, you’ll analyze a rich dataset including passenger details, card access logs, and dining records to identify the culprit. This hands-on exercise tests your ability to manipulate data, uncover patterns, and draw logical conclusions—skills essential for technical interviews. Imagine yourself as a data detective, sifting through clues like a passenger’s whereabouts or suspicious dining habits, all while leveraging Python’s powerful data-handling capabilities. Perfect for students and job seekers, this challenge offers a practical, story-driven way to prepare for roles requiring analytical prowess and coding expertise. Can you solve the mystery and prove your data analysis chops?

## Setup
Clone this repository which contains:
- passenger_manifest.csv
- card_access_logs.json
- dining_transactions.csv

## Investigation Tasks

### Task 1: Data Loading & Initial Inspection
**Question**: Load all three datasets and display the first few rows of each. Make sure to handle timestamps appropriately.


### Task 2: Establishing Timeline
**Question**: Between 7 PM and 9 PM, create a timeline of all passenger movements (entries/exits) and dining transactions. Display this in a clear, chronological format.


### Task 3: Identifying Anomalies
**Question**: Find passengers who were in the dining hall during the incident (8 PM) but didn't make any dining transactions. Also identify any passengers who made dining transactions but have no record of entering the dining hall.


### Task 4: Location Analysis
**Question**: Cross-reference the passenger manifest with the access logs to identify:
- Passengers who were in suspicious locations at 8 PM
- Passengers who made unusual movement patterns (multiple entries/exits)
Display your findings with supporting evidence.


### Task 5: Final Analysis
**Question**: Based on your findings from tasks 1-4, identify the most suspicious passenger(s) and explain your reasoning. Support your conclusion with data from all three sources.
