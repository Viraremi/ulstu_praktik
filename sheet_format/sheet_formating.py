import pandas as pd
import os

id_SubFed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

ulsk = [
    13
]

# Создаем нужные папки если их нет

def save_to_csv(dataframe, file_path, separator):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    dataframe.to_csv(file_path, sep=separator)

# Функции обработки для полноценных файлов

def full_exel_to_csv(path:str, year, settings):
    print('Обработка ' + settings['sheet'] + '...')
    df = pd.read_excel(path, sheet_name=settings['sheet'], header=None)
    df = df.iloc[settings['iloc_rows'][0]:settings['iloc_rows'][1], settings['iloc_columns'][0]:settings['iloc_columns'][1]] # Обрезаем лишнее
    df = df.drop(settings['drop_column'], axis=1)
    df = df.stack().reset_index(drop=True).to_frame() # Складываем таблицу в одну большую строку
    m_id = pd.MultiIndex.from_product([id_SubFed] + settings['m_id_lists'], names=settings['m_id_names'])
    df = df.set_axis(m_id, axis=0) # Присваиваем мультииндекс
    df.insert(0, 'year', str(year) + '-01-01') # Добавляем колонку "год"
    df = df.rename(columns={0: 'amount'})
    return df

# Функции обработки для файлов только с Ульяновской областью

def ul_exel_to_csv(path:str, year, settings):
    print('Обработка ' + settings['sheet'] + '...')
    df = pd.read_excel(path, sheet_name=settings['sheet'], header=None)
    df = df.iloc[settings['iloc_rows'][0]:settings['iloc_rows'][1], settings['iloc_columns'][0]:settings['iloc_columns'][1]] # Обрезаем лишнее
    df = df.drop(settings['drop_column'], axis=1)
    df = df.dropna(how='any')
    if df.size == 0:
        print('Ошибка ' + settings['sheet'])
        return df
    df = df.stack().reset_index(drop=True).to_frame() # Складываем таблицу в одну большую строку
    m_id = pd.MultiIndex.from_product([ulsk] + settings['m_id_lists'], names=settings['m_id_names'])
    df = df.set_axis(m_id, axis=0) # Присваиваем мультииндекс
    df.insert(0, 'year', str(year) + '-01-01') # Добавляем колонку "год"
    df = df.rename(columns={0: 'amount'})
    return df

#Основной блок

def start_format(sheet_settings, mode: bool, file_path, file_year, save_path, ignore_sheet):

    file_name = file_path.split("/")[-1]

    if mode: #full
        print('\nОткрываем файл ' + file_name)
        for data in sheet_settings.items():
            if data[0] in ignore_sheet: continue
            df = full_exel_to_csv(file_path, file_year, data[1])
            save_to_csv(df, 'CSVs/' + data[1]['csv_path'], ';')
            save_to_csv(df, save_path + '/result/' + data[1]['csv_path'], ';')

    else: #ul
        print('\nОткрываем файл ' + file_name)
        for data in sheet_settings.items():
            if data[0] in ignore_sheet: continue
            df = ul_exel_to_csv(file_path, file_year, data[1])
            if df.size != 0:
                save_to_csv(df, 'CSVs/' + data[1]['csv_path'], ';')
                save_to_csv(df, save_path + '/result/' + data[1]['csv_path'], ';')
    print('SUCCESS')