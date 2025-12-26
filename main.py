import os, time

def calc_size(size):
    if size != 512:
        print("Файл НЕ весит 512 киллобайт ровно. Перепиши/добавь мусора")
        return False
    else: 
        return True

def main():
    # запуск 1
    print("Запуск компиляций!")
    time.sleep(0.3)
    name = input("Названия bin файла: ").strip()

    # проверка имени и формирование выходного файла
    if not name.lower().endswith('.bin'):
        outfile = f"{name}.bin"
    else:
        outfile = name
    # Навсякий случай try-expect
    try:
        os.system(f"nasm -f bin boot.asm -o {outfile}")
    except OSError:
        print("Ошибка компила")
    
    # Навсякий случай вторая проверка.
    if os.path.exists(outfile):
        size_kb = os.path.getsize(outfile) 
        calc_size(size_kb)
        exit()
    else:
        print(f"Файл {outfile} не найден — сборка, вероятно, не удалась.")

# ЗАПУСК 2
if __name__ == "__main__":
    main()
