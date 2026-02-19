import sys
import importlib

def solve():
    # Читаем все входные данные
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        n = int(input_data[0].strip())
    except (ValueError, IndexError):
        return

    for i in range(1, n + 1):
        if i >= len(input_data):
            break
            
        line = input_data[i].strip()
        if not line:
            continue
            
        parts = line.split()
        if len(parts) < 2:
            continue
            
        module_path, attr_name = parts[0], parts[1]
        
        try:
            # Пытаемся импортировать модуль
            mod = importlib.import_module(module_path)
            
            # Проверяем наличие атрибута
            if hasattr(mod, attr_name):
                attr = getattr(mod, attr_name)
                # Проверяем, можно ли его вызвать
                if callable(attr):
                    print("CALLABLE")
                else:
                    print("VALUE")
            else:
                print("ATTRIBUTE_NOT_FOUND")
                
        except ImportError:
            # Если модуль не найден или путь некорректен
            print("MODULE_NOT_FOUND")
        except Exception:
            # На случай специфических ошибок при доступе к атрибутам
            print("ATTRIBUTE_NOT_FOUND")

if __name__ == "__main__":
    solve()