import json
import sheet_settings as stgs
import sheet_formating as frmt

# Читаем настройки форматирования из файла
stgs.get_settings()
with open("all_settings.json", "r", encoding="utf-8") as file:
    sheet_settings = json.load(file)
    print("Настройки форматирования получены!")

flag = False
frmt.start_format(sheet_settings, flag)

