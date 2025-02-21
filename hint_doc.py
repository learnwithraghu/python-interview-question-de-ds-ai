# Investigation Hints Guide

## General Tips
- Always check your data types after loading, especially for timestamps
- Use `pd.to_datetime()` for converting string timestamps
- Remember to handle missing values appropriately
- Print intermediate results to verify your analysis

## Task 1 Hints
1. First hint:
   - For JSON files, use `json.loads()` after reading the file
   - For CSVs, `pd.read_csv()` is your friend

2. If still stuck:
   - Remember to convert timestamps in both card_logs and dining_transactions
   - Use `df.head()` to verify your data loading

## Task 2 Hints
1. First hint:
   - Filter timestamps using `.dt.hour`
   - Consider using `between(19, 21)` for 7 PM - 9 PM

2. If still stuck:
   - Try sorting all events by timestamp using `sort_values()`
   - You might want to combine both access logs and dining data into one timeline

## Task 3 Hints
1. First hint:
   - Focus on the 8 PM hour (hour == 20)
   - Use sets to find differences between groups of passengers

2. If still stuck:
   - Get unique passenger IDs from dining hall entries
   - Compare against unique IDs from dining transactions
   - Look for set operations like set(a) - set(b)

## Task 4 Hints
1. First hint:
   - Group card access data by passenger_id
   - Count number of entries/exits per passenger

2. If still stuck:
   - Use `groupby()` followed by `agg()` to count movements
   - Consider what makes a movement pattern "unusual" (frequency? location changes?)

## Task 5 Hints
1. First hint:
   - Create a scoring system for suspicious behaviors
   - Consider weighting different types of suspicious activity

2. If still stuck:
   - Combine findings from previous tasks into a single dataframe
   - Look for passengers who appear in multiple suspicious categories

## Debugging Tips
- If getting timestamp errors:
  ```python
  print(df['timestamp'].dtype)  # Check data type
  print(df['timestamp'].head())  # Check format
  ```

- If getting merge errors:
  ```python
  print(df1['passenger_id'].nunique())  # Check unique IDs
  print(df2['passenger_id'].nunique())
  ```

- If data seems incorrect:
  ```python
  print(df.info())  # Check data types and null values
  print(df.describe())  # Check basic statistics
  ```

## Helper Code Snippets
```python
# Filter by time range
mask = df['timestamp'].dt.hour.between(start_hour, end_hour)

# Group and count
summary = df.groupby('column').agg({
    'col1': 'count',
    'col2': 'nunique'
})

# Find common/different elements
set_a = set(df1['column'])
set_b = set(df2['column'])
difference = set_a - set_b
```

Remember:
- Take it step by step
- Print intermediate results
- Cross-reference between datasets
- Consider the logical flow of the investigation
- Think about what would make someone's behavior suspicious in real life
