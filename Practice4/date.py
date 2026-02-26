# Python Date
# 1. Subtract five days from current date
from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date - timedelta(days=5))
# 2. Print yesterday, today, tomorrow
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday, today, tomorrow, sep="\n")
# 3. Drop microseconds from datetime
from datetime import datetime, timedelta

dt_no_ms = datetime.now().replace(microsecond=0)
print(dt_no_ms)
# 4. Calculate two date difference in seconds
from datetime import datetime, timedelta

date1 = datetime.now()
date2 = datetime.now() - timedelta(hours=2) # example difference
diff = date1 - date2
print(int(diff.total_seconds()))
