import sys
import json

def get_diff(obj1, obj2, path="", diffs=None):
    if diffs is None:
        diffs = {}
    
    # Ключи берем только если это словари
    keys1 = set(obj1.keys()) if isinstance(obj1, dict) else set()
    keys2 = set(obj2.keys()) if isinstance(obj2, dict) else set()
    all_keys = sorted(list(keys1 | keys2))
    
    for key in all_keys:
        new_path = f"{path}.{key}" if path else key
        
        has1 = isinstance(obj1, dict) and key in obj1
        has2 = isinstance(obj2, dict) and key in obj2
        
        val1 = obj1[key] if has1 else "<missing>"
        val2 = obj2[key] if has2 else "<missing>"
        
        if has1 and has2:
            if val1 == val2:
                continue
            if isinstance(val1, dict) and isinstance(val2, dict):
                get_diff(val1, val2, new_path, diffs)
            else:
                v1_s = json.dumps(val1, separators=(',', ':'), sort_keys=True)
                v2_s = json.dumps(val2, separators=(',', ':'), sort_keys=True)
                diffs[new_path] = f"{v1_s} -> {v2_s}"
        else:
            v1_s = "<missing>" if not has1 else json.dumps(val1, separators=(',', ':'), sort_keys=True)
            v2_s = "<missing>" if not has2 else json.dumps(val2, separators=(',', ':'), sort_keys=True)
            diffs[new_path] = f"{v1_s} -> {v2_s}"
            
    return diffs

def main():
    # Читаем через stdin.read().split(), это надежнее всего
    all_input = sys.stdin.read().split('\n')
    lines = [l.strip() for l in all_input if l.strip()]
    
    if len(lines) < 2:
        return
    
    obj1 = json.loads(lines[0])
    obj2 = json.loads(lines[1])
    
    res = get_diff(obj1, obj2)
    
    if not res:
        print("No differences")
    else:
        # Сортируем пути перед выводом
        for p in sorted(res.keys()):
            print(f"{p} : {res[p]}")

if __name__ == "__main__":
    main()