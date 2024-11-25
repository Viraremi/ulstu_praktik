import pandas as pd
import json
import os

# id_SubFed = ['Республика Башкортостан',
#              'Республика Марий Эл',
#              'Республика Мордовия',
#              'Республика Татарстан',
#              'Удмуртская Республика',
#              'Чувашская Республика',
#              'Пермский край',
#              'Кировская область',
#              'Нижегородская область',
#              'Оренбургская область',
#              'Пензенская область',
#              'Самарская область',
#              'Саратовская область',
#              'Ульяновская область']

id_SubFed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

ulsk = [
    'Ульяновская область'
]

# Создаем нужные папки если их нет

def save_to_csv(dataframe, file_path, separator):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    dataframe.to_csv(file_path, sep=separator)

# Читаем настройки форматирования из файла

with open("all_settings.json", "r", encoding="utf-8") as file:
    sheet_settings = json.load(file)

# Функции обработки для полноценных файлов

def full_exel_to_csv(path:str, year: int, settings):
    print('Обработка ' + settings['sheet'] + '...')
    df = pd.read_excel('data_xlsx/' + path, sheet_name=settings['sheet'], header=None)
    df = df.iloc[settings['iloc_rows'][0]:settings['iloc_rows'][1], settings['iloc_columns'][0]:settings['iloc_columns'][1]] # Обрезаем лишнее
    df = df.drop(settings['drop_column'], axis=1)
    df = df.stack().reset_index(drop=True).to_frame() # Складываем таблицу в одну большую строку
    m_id = pd.MultiIndex.from_product([id_SubFed] + settings['m_id_lists'], names=settings['m_id_names'])
    df = df.set_axis(m_id, axis=0) # Присваиваем мультииндекс
    df.insert(0, 'year', year) # Добавляем колонку "год"
    df = df.rename(columns={0: 'amount'})
    return df

def full_dpo_gs_to_csv(path: str, year: int, settings):
    print('\nDPO_GS')
    df1 = full_exel_to_csv(path, year, settings['DPO_GS_1'])
    df2 = full_exel_to_csv(path, year, settings['DPO_GS_2'])

    result = pd.concat([df1, df2], axis=0)
    save_to_csv(result, 'CSVs/' + path[:-5] + '/DPO_GS.csv', ';')

def full_dpo_gs_other_to_csv(path: str, year: int, settings):
    print('\nDPO_GS_other')
    df1 = full_exel_to_csv(path, year, settings['DPO_GS_other_1'])
    df2 = full_exel_to_csv(path, year, settings['DPO_GS_other_2'])
    df3 = full_exel_to_csv(path, year, settings['DPO_GS_other_3'])

    result = pd.concat([df1, df2], axis=0)
    result = pd.concat([result, df3], axis=0)
    save_to_csv(result, 'CSVs/' + path[:-5] + '/DPO_GS_other.csv', ';')

# Функции обработки для файлов только с Ульяновской областью

def ul_exel_to_csv(path:str, year: int, settings):
    print('Обработка ' + settings['sheet'] + '...')
    df = pd.read_excel('data_xlsx/' + path, sheet_name=settings['sheet'], header=None)
    df = df.iloc[settings['iloc_rows'][0]:settings['iloc_rows'][1], settings['iloc_columns'][0]:settings['iloc_columns'][1]] # Обрезаем лишнее
    df = df.drop(settings['drop_column'], axis=1)
    df = df.dropna(how='any')
    if df.size == 0:
        print('Ошибка ' + settings['sheet'])
        return df
    df = df.stack().reset_index(drop=True).to_frame() # Складываем таблицу в одну большую строку
    m_id = pd.MultiIndex.from_product([ulsk] + settings['m_id_lists'], names=settings['m_id_names'])
    df = df.set_axis(m_id, axis=0) # Присваиваем мультииндекс
    df.insert(0, 'year', year) # Добавляем колонку "год"
    df = df.rename(columns={0: 'amount'})
    return df

def ul_dpo_gs_to_csv(path: str, year: int, settings):
    print('\nDPO_GS')
    df1 = ul_exel_to_csv(path, year, settings['DPO_GS_1'])
    if df1.size == 0:
        print('Ошибка DPO_GS_1')
        return
    df2 = ul_exel_to_csv(path, year, settings['DPO_GS_2'])
    if df2.size == 0:
        print('Ошибка DPO_GS_2')
        return

    result = pd.concat([df1, df2], axis=0)
    save_to_csv(result, 'CSVs/' + path[:-5] + '/DPO_GS.csv', ';')

def ul_dpo_gs_other_to_csv(path: str, year: int, settings):
    print('\nDPO_GS_other')
    df1 = ul_exel_to_csv(path, year, settings['DPO_GS_other_1'])
    if df1.size == 0:
        print('Ошибка DPO_GS_other_1')
        return
    df2 = ul_exel_to_csv(path, year, settings['DPO_GS_other_2'])
    if df2.size == 0:
        print('Ошибка DPO_GS_other_2')
        return
    df3 = ul_exel_to_csv(path, year, settings['DPO_GS_other_3'])
    if df3.size == 0:
        print('Ошибка DPO_GS_other_3')
        return

    result = pd.concat([df1, df2], axis=0)
    result = pd.concat([result, df3], axis=0)
    save_to_csv(result, 'CSVs/' + path[:-5] + '/DPO_GS_other.csv', ';')

#Основной блок

ignore_sheet = [
    'DPO_GS_1',
    'DPO_GS_2',
    'DPO_GS_other_1',
    'DPO_GS_other_2',
    'DPO_GS_other_3'
]

#Список и обработка ульяновских файлов
print('\nОбработка ульяновских файлов\n')
ul_data_xlsx = {
    '2019_ul.xlsx' : 2019,
    '2020_ul.xlsx' : 2020,
    '2021_ul.xlsx' : 2021,
    '2022_ul.xlsx' : 2022,
    '2023_ul.xlsx' : 2023,
}
for file in ul_data_xlsx.items():
    print('\nОткрываем файл ' + file[0])
    for data in sheet_settings.items():
        if data[0] in ignore_sheet: continue
        df = ul_exel_to_csv(file[0], file[1], data[1])
        if df.size != 0:
            save_to_csv(df, 'CSVs/' + file[0][:-5] + '/' + data[1]['csv_path'], ';')
    ul_dpo_gs_to_csv(file[0], file[1], sheet_settings)
    ul_dpo_gs_other_to_csv(file[0], file[1], sheet_settings)

#Список и обработка полноценных файлов
print('\nОбработка полноценных файлов\n')
full_data_xlsx = {
    '2020_full.xlsx' : 2020,
    '2021_full.xlsx' : 2021,
    '2022_full.xlsx' : 2022,
    '2023_full.xlsx' : 2023,
}
for file in full_data_xlsx.items():
    print('\nОткрываем файл ' + file[0])
    for data in sheet_settings.items():
        if data[0] in ignore_sheet: continue
        df = full_exel_to_csv(file[0], file[1], data[1])
        save_to_csv(df, 'CSVs/' + file[0][:-5] + '/' + data[1]['csv_path'], ';')
    full_dpo_gs_to_csv(file[0], file[1], sheet_settings)
    full_dpo_gs_other_to_csv(file[0], file[1], sheet_settings)

print('SUCCESS')