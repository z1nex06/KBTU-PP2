import sys
import json

def apply_patch(source, patch):
    if not isinstance(patch, dict):
        return patch
    if not isinstance(source, dict):
        source = {}

    for key, value in patch.items():
        if value is None:
            if key in source:
                del source[key]
        elif isinstance(value, dict) and key in source and isinstance(source[key], dict):
            source[key] = apply_patch(source[key], value)
        else:
            source[key] = value
    return source

def main():
    # Читаем весь ввод и фильтруем пустые строки
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) < 2:
        return
    
    try:
        source = json.loads(lines[0])
        patch = json.loads(lines[1])
        
        result = apply_patch(source, patch)
        
        # Вывод строго в компактном виде с сортировкой ключей
        print(json.dumps(result, sort_keys=True, separators=(',', ':')))
    except (json.JSONDecodeError, ValueError):
        pass

if __name__ == "__main__":
    main()