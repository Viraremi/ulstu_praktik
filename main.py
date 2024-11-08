import pandas as pd

def read_Amount_GS(path: str, year: int):
    id_SubFed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    group = [
        'Численность государственных должностей субъекта Российской Федерации',
        'Численность должностей государственной гражданской службы',
        'Численность должностей, не отнесенных к должностям государственной гражданской службы'
    ]
    status = [
        'Всего',
        'замещено',
        'количество лиц, находящихся в отпуске по уходу за ребенком'
    ]

    df = pd.read_excel(path, sheet_name='1.1. Кол-во ГС', header=None)
    df = df.iloc[6:20, 6:18] # Обрезаем лишнее
    df = df.drop([9, 13, 17], axis=1)
    df = df.stack().reset_index(drop=True).to_frame() # Складываем таблицу в одну большую строку
    m_id = pd.MultiIndex.from_product([id_SubFed, group, status], names=['id_SubFed', 'group', 'status']) # Формируем и присваиваем мультииндекс
    df = df.set_axis(m_id, axis=0)
    df.insert(0, 'year', year) # Добавляем колонку "год"
    df = df.rename(columns={0: 'amount'})
    df.to_csv('Amount_GS.csv', sep=';')

def read_Amount_MS(path: str, year: int):
    id_SubFed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    group = [
        'Численность должностей муниципальной службы',
        'Численность должностей, не отнесенных к должностям муниципальной службы'
    ]
    status = [
        'Всего',
        'замещено',
        'количество лиц, находящихся в отпуске по уходу за ребенком'
    ]

    df = pd.read_excel(path, sheet_name='1.2. Кол-во МС', header=None)
    df = df.iloc[6:20, 6:14] # Обрезаем лишнее
    df = df.drop([9, 13], axis=1)
    df = df.stack().reset_index(drop=True).to_frame() # Складываем таблицу в одну большую строку
    m_id = pd.MultiIndex.from_product([id_SubFed, group, status], names=['id_SubFed', 'group', 'status']) # Формируем и присваиваем мультииндекс
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'value'})
    df.insert(0, 'year', year) # Добавляем колонку "год"
    df.to_csv('Amount_MS.csv', sep=';')

def read_Gender_GS(path: str, year: int):
    id_SubFed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #...

read_Amount_GS('2021.xls', 2021)
read_Amount_MS('2021.xls', 2021)