import sys
import json
import re

def resolve():
    # Читаем весь ввод сразу
    raw_input = sys.stdin.read().splitlines()
    if not raw_input:
        return
    
    # Парсим JSON и количество запросов
    try:
        data = json.loads(raw_input[0])
        n = int(raw_input[1].strip())
    except:
        return

    # Регулярка для токенов: либо ключ, либо [индекс]
    pattern = re.compile(r'([^.\[\]]+)|\[(\d+)\]')

    for i in range(2, 2 + n):
        if i >= len(raw_input):
            break
        
        query = raw_input[i].strip()
        tokens = pattern.findall(query)
        current = data
        found = True
        
        for key, idx in tokens:
            if key:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    found = False
                    break
            elif idx:
                idx_val = int(idx)
                if isinstance(current, list) and 0 <= idx_val < len(current):
                    current = current[idx_val]
                else:
                    found = False
                    break
        
        if found:
            print(json.dumps(current, separators=(',', ':'), sort_keys=True))
        else:
            print("NOT_FOUND")

if __name__ == "__main__":
    resolve()