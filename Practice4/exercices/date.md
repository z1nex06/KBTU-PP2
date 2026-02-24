from datetime import datetime, timedelta

# 1. Subtract five days from current date
```python
current_date = datetime.now()
print(current_date - timedelta(days=5))
```

# 2. Print yesterday, today, tomorrow
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday, today, tomorrow, sep="\n")

# 3. Drop microseconds from datetime
dt_no_ms = datetime.now().replace(microsecond=0)
print(dt_no_ms)

# 4. Calculate two date difference in seconds
date1 = datetime.now()
date2 = datetime.now() - timedelta(hours=2) # example difference
diff = date1 - date2
print(int(diff.total_seconds()))
