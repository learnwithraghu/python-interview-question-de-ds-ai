### Cruise Ship Investigation Challenge

#### Background

A high-stakes theft has occurred on the luxurious *Ocean Star* cruise ship: a valuable item was stolen from a passenger's cabin between 8:00 PM and 8:15 PM on February 20, 2024. The ship's security team has provided three key datasets to help identify the culprit:

1. **Passenger Manifest**: Contains passenger information including ID, name, cabin number, dining preferences, age, and nationality.
2. **Card Access Logs**: Records every time a passenger's keycard is used to enter or exit their cabin and the dining hall, including timestamps and action type.
3. **Dining Transactions**: Documents all food and beverage purchases made by passengers, including timestamps, items ordered, and payment amounts.

As a data detective, your mission is to analyze these datasets using Python to identify suspicious patterns, verify alibis, and ultimately pinpoint the thief. This challenge tests your ability to work with real-world data, perform time-based analysis, and draw logical conclusions from multiple data sources.

#### Investigation Tasks

**Task 1: Data Loading & Initial Inspection**\
*Question:* Load and examine the three datasets:
- Load passenger_manifest.csv, card_access_logs.json, and dining_transactions.csv into Python using pandas
- Display the first 5 rows of each dataset
- Check for any missing values or data quality issues
- Ensure all timestamp columns are properly parsed as datetime objects

*Hint:* Pay special attention to the different data formats (CSV and JSON) and timestamp formats in each dataset. The card_access_logs.json file contains nested data that needs to be properly flattened.

*Why this task matters:* Understanding the structure and quality of your data is the foundation of any investigation. This step helps identify potential data issues that could affect your analysis and ensures you're working with properly formatted timestamps for accurate timeline reconstruction.

**Task 2: Establishing the Crime Timeline**\
*Question:* Create a comprehensive timeline of events during the theft window (8:00 PM to 8:15 PM) by:
- Analyzing cabin access patterns from the card access logs
- Correlating these with dining hall movements
- Matching with dining transactions
- Sorting all events chronologically
- Presenting the results in a clear, readable format

*Hint:* Consider using pandas' merge operations to combine data from multiple sources. Pay attention to the exact timestamps to ensure accurate sequencing of events. Look for patterns in cabin access and dining hall movements.

*Why this task matters:* A precise timeline helps identify who was where and when during the theft. This chronological view is essential for spotting suspicious movements and verifying alibis, particularly focusing on cabin access patterns during the theft window.

**Task 3: Alibi Verification**\
*Question:* Investigate potential alibi inconsistencies by analyzing:
- Passengers who were recorded in the dining hall during the theft window
- Matching these records with actual dining transactions
- Identifying any discrepancies between access logs and transaction records
- Checking if passengers' dining preferences (Early/Late) align with their actual dining times

*Hint:* Look for cases where a passenger's access log shows them in the dining hall but there are no corresponding transactions, or vice versa. Also consider if their dining preferences match their actual behavior.

*Why this task matters:* Alibi verification is crucial in narrowing down suspects. Inconsistencies between where someone claims to be and the actual evidence can reveal potential deception, especially when considering their stated dining preferences versus actual behavior.
