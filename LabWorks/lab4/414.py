import sys
from datetime import datetime, timedelta

def get_ts(s):
    # s = "2025-01-01 UTC+00:00"
    p = s.strip().split()
    dt = datetime.strptime(p[0], "%Y-%m-%d")
    tz = p[1][3:] # Отрезаем "UTC" -> "+00:00"
    sign = 1 if tz[0] == '+' else -1
    h, m = map(int, tz[1:].split(':'))
    offset = timedelta(hours=h, minutes=m)
    if sign == 1:
        return dt - offset
    return dt + offset

def main():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2: return
    try:
        t1 = get_ts(lines[0])
        t2 = get_ts(lines[1])
        diff = abs((t1 - t2).total_seconds())
        print(int(diff // 86400))
    except:
        pass

if __name__ == "__main__":
    main()