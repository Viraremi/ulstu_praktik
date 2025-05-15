import json

from config_project import Const
from sheet_format.model_settings import Setting

def update_or_reset_settings(settings: dict[str, Setting]) -> None:
    print('Обновление файла настроек...')
    for key, value in settings.items():
        settings[key] = value.model_dump()
    json_string = json.dumps(settings, ensure_ascii=False, indent=4)
    with open(Const.SETTINGS_FILE, "w", encoding="utf-8") as file:
        file.write(json_string)
    print('SUCCESS')


def get_json_string() -> str:
    try:
        with open(Const.SETTINGS_FILE, "r", encoding="utf-8") as file:
            json_string = json.load(file)
            print("Настройки форматирования получены!")
        return json.dumps(json_string, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        return ""


def get_settings() -> dict[str, Setting]:
    try:
        with open(Const.SETTINGS_FILE, "r", encoding="utf-8") as file:
            dict_data: dict = json.load(file)
            print("Настройки форматирования получены!")
        for key, value in dict_data.items():
            dict_data[key] = Setting(**value)
        return dict_data
    except FileNotFoundError:
        return {}
