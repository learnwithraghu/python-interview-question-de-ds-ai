### Cruise Ship Investigation Challenge

#### Background

A priceless diamond necklace was stolen from the VIP lounge of the *Ocean Star* cruise ship between 8:00 PM and 8:15 PM on March 25, 2025. You're a data detective tasked with finding the thief using Python. You'll analyze three datasets---passenger details, access logs, and dining records---to track movements and spot suspicious behavior. This challenge sharpens your data analysis skills, perfect for tech interviews. Ready to solve the mystery?

#### Setup

Clone the repository containing:

-   passenger_manifest.csv: Passenger ID, name, cabin number, VIP status.
-   card_access_logs.json: Timestamps, passenger ID, location (e.g., VIP lounge, dining hall), action (entry/exit).
-   dining_transactions.csv: Timestamps, passenger ID, transaction details (e.g., food ordered, cost).

#### Investigation Tasks

**Task 1: Load and Peek at the Data**\
*Question:* Load all three datasets into Python and show the first few rows of each.\
*Why:* We need to see what we're working with---passenger names, locations, and transactions are our clues. Make sure timestamps load as dates so we can sort them later. (Hint: Use a pandas function to read files and another to check the top rows.)

**Task 2: Build a Timeline Around the Theft**\
*Question:* Create a timeline of all passenger movements and dining transactions between 7:00 PM and 9:00 PM on March 25, 2025, sorted by time.\
*Why:* The theft happened at 8:00 PM, so we need to know where everyone was before, during, and after. This helps us spot who was near the VIP lounge. (Hint: Filter rows by time and combine datasets, then sort by the timestamp column.)

**Task 3: Check Dining Hall Alibis**\
*Question:* Find passengers who were in the dining hall at 8:00 PM but didn't make a dining transaction between 7:00 PM and 9:00 PM.\
*Why:* The dining hall is far from the VIP lounge, so being there could be an alibi---unless they were faking it by not eating. This flags suspicious passengers without solid excuses. (Hint: Filter access logs for 8:00 PM, then check against dining records.)

**Task 4: Spot Suspects Near the Crime Scene**\
*Question:* Identify passengers who entered the VIP lounge between 7:45 PM and 8:15 PM.\
*Why:* The theft happened in the VIP lounge between 8:00 PM and 8:15 PM, so anyone there right before or during is a prime suspect. (Hint: Filter access logs by time and location, then pull their details.)

**Task 5: Pick the Thief**\
*Question:* Based on your findings, name the most suspicious passenger and explain why, using evidence from all datasets.\
*Why:* This ties everything together---movements, alibis, and passenger info---to catch the thief. We want to see your logic backed by data, like "They were in the VIP lounge at 8:02 PM with no alibi." (Hint: Combine your results and look for patterns, like VIP status or odd behavior.)
