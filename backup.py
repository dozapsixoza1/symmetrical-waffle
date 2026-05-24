import shutil
import os
import time

print("⏳ Начинаю создание бэкапа...")

# Создаем папку backups, если её нет
if not os.path.exists("backups"):
    os.mkdir("backups")
    
# Формируем имя файла
current_time = time.strftime("%Y-%m-%d_%H-%M")
backup_name = f"backups/backup_{current_time}.json"

# Копируем базу данных (если она существует)
if os.path.exists("database.json"):
    try:
        shutil.copyfile("database.json", backup_name)
        print(f"✅ Успешно! Бэкап сохранен как: {backup_name}")
    except Exception as e:
        print(f"❌ Ошибка при копировании: {e}")
else:
    print("❌ Ошибка: Файл database.json не найден. Бэкапить пока нечего!")
