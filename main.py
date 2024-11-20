import pandas as pd
import json

def exel_to_csv(path:str, year: int, settings):
    df = pd.read_excel(path, sheet_name=settings['sheet'], header=None)
    df = df.iloc[settings['iloc_rows'][0]:settings['iloc_rows'][1], settings['iloc_columns'][0]:settings['iloc_columns'][1]] # Обрезаем лишнее
    df = df.drop(settings['drop_column'], axis=1)
    df = df.stack().reset_index(drop=True).to_frame() # Складываем таблицу в одну большую строку
    m_id = pd.MultiIndex.from_product(settings['m_id_lists'], names=settings['m_id_names'])
    df = df.set_axis(m_id, axis=0) # Присваиваем мультииндекс
    df.insert(0, 'year', year) # Добавляем колонку "год"
    df = df.rename(columns={0: 'amount'})
    df.to_csv(settings['csv_path'], sep=';')
    return df

with open("all_settings.json", "r", encoding="utf-8") as file:
    settings = json.load(file)

for data in settings.items():
    exel_to_csv('data_xlsx/2021x.xlsx', 2021, data[1])

#DPO_GS
# read_ReserveCause('data_xlsx/2021x.xlsx', 2021, 'CSVs/ReserveCause.csv')
# read_Attestation('data_xlsx/2021x.xlsx', 2021, 'CSVs/Attestation.csv')
# read_Ranks('data_xlsx/2021x.xlsx', 2021, 'CSVs/Ranks.csv')
# read_TargetedTraining('data_xlsx/2021x.xlsx', 2021, 'CSVs/TargetedTraining.csv')
# read_ProfDev_amount('data_xlsx/2021x.xlsx', 2021, 'CSVs/ProfDev_amount.csv')
# read_ProfDev_resources('data_xlsx/2021x.xlsx', 2021, 'CSVs/ProfDev_resources.csv')