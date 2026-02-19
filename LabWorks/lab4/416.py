import sys
from datetime import datetime, timedelta

def get_utc_time(s):
    # s = "2026-01-01 10:00:00 UTC+03:00"
    parts = s.strip().split()
    # Соединяем дату и время для парсинга
    dt_str = f"{parts[0]} {parts[1]}"
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    
    # Разбираем часовой пояс UTC+HH:MM
    tz_info = parts[2][3:]  # Отрезаем "UTC" -> "+03:00"
    sign = 1 if tz_info[0] == '+' else -1
    h, m = map(int, tz_info[1:].split(':'))
    
    offset = timedelta(hours=h, minutes=m)
    
    # UTC = Local Time - Offset (если +03:00, вычитаем 3 часа)
    if sign == 1:
        return dt - offset
    else:
        return dt + offset

def main():
    # Читаем все строки и фильтруем пустые
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    if len(lines) < 2:
        return

    try:
        start_utc = get_utc_time(lines[0])
        end_utc = get_utc_time(lines[1])
        
        # Разница в секундах (может быть отрицательной по смыслу end-start, 
        # но обычно в логах end > start)
        duration = (end_utc - start_utc).total_seconds()
        
        print(int(duration))
    except Exception:
        pass

if __name__ == "__main__":
    main()