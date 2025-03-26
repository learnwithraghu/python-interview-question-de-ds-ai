### Cruise Ship Investigation Challenge

#### Background

A high-stakes theft has rocked the luxurious *Ocean Star* cruise ship: a priceless diamond necklace was stolen from the ship's VIP lounge between 8:00 PM and 8:15 PM on March 25, 2025. As a data detective, your mission is to analyze passenger data using Python and pinpoint the culprit. You'll work with three datasets---passenger details, card access logs, and dining records---to uncover clues like suspicious movements, alibi inconsistencies, or unusual behavior. This challenge tests your ability to wrangle data, spot patterns, and draw evidence-based conclusions, mirroring the analytical skills top tech roles demand. Can you crack the case and showcase your coding expertise?

#### Setup

Clone the repository containing:

-   passenger_manifest.csv: Passenger ID, name, cabin number, and VIP status.
-   card_access_logs.json: Timestamps, passenger ID, location (e.g., VIP lounge, dining hall, deck), and action (entry/exit).
-   dining_transactions.csv: Timestamps, passenger ID, and transaction details (e.g., food ordered, cost).

#### Investigation Tasks

**Task 1: Data Loading & Initial Inspection**\
*Question:* Load all three datasets into Python (using pandas or similar) and display the first 5 rows of each. Ensure timestamps are parsed correctly as datetime objects for accurate time-based analysis.

**Task 2: Establishing the Crime Timeline**\
*Question:* Focus on the theft window (8:00 PM to 8:15 PM on March 25, 2025). Create a chronological timeline combining:

-   All passenger movements (entries/exits) from the access logs.
-   All dining transactions.\
    Display the result in a readable format (e.g., a table sorted by timestamp).

**Task 3: Alibi Check -- Dining Hall Discrepancies**\
*Question:* The dining hall is a potential alibi location, as it's far from the VIP lounge. Investigate:

-   Passengers who were in the dining hall (per access logs) at 8:00 PM but have no dining transactions between 7:00 PM and 9:00 PM---did they fake their presence?
-   Passengers with dining transactions at 8:00 PM but no record of entering the dining hall---did they tamper with the system?\
    List these passengers with supporting evidence.

**Task 4: Suspicious Movements**\
*Question:* The VIP lounge is the crime scene. Analyze the access logs and passenger manifest to find:

-   Passengers who entered the VIP lounge between 7:45 PM and 8:15 PM (suspicious proximity to the theft).
-   Passengers with unusual movement patterns between 7:00 PM and 9:00 PM (e.g., multiple entries/exits to the VIP lounge or rapid location changes).\
    Present your findings with timestamps and locations as evidence.

**Task 5: Final Suspect Identification**\
*Question:* Using insights from Tasks 1-4, identify the most likely suspect(s) for the theft. Consider:

-   Presence in or near the VIP lounge during the theft window.
-   Inconsistent alibis (e.g., dining hall discrepancies).
-   Unusual behavior (e.g., erratic movements or VIP status).\
    Explain your reasoning, backing it with specific data from all three datasets (e.g., "Passenger X entered the VIP lounge at 8:02 PM, has no dining alibi, and made three rapid location switches").
