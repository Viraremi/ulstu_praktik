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

# gender = [
#     'мужчины',
#     'женщины'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, gender], names=['id_SubFed', 'gender'])
# exel_to_csv('data_xlsx/2021x.xlsx', '2.1. Гендерный ГС', 2021, 'CSVs/Gender_GS.csv',
#             [4,18], [2, 6],[3, 5], m_id)
# exel_to_csv('data_xlsx/2021x.xlsx', '2.2. Гендерный МС', 2021, 'CSVs/Gender_MS.csv',
#             [4,18], [2, 6],[3, 5], m_id)
#
# category = [
#     'до 30 лет',
#     'от 31 до 40 лет',
#     'от 41 до 50 лет',
#     'от 51 до 60 лет',
#     'старше 61 года',
#     'средний возраст служащих'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '3.1. Возраст ГС', 2021, 'CSVs/Age_GS.csv',
#             [4,18], [2, 13],[3, 5, 7, 9, 11], m_id)
# exel_to_csv('data_xlsx/2021x.xlsx', '3.2. Возраст МС', 2021, 'CSVs/Age_MS.csv',
#             [4,18], [2, 13],[3, 5, 7, 9, 11], m_id)
#
# educ_lvl = [
#     'бакалавриат',
#     'специалитет',
#     'магистратура',
#     'среднее профессиональное'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, educ_lvl], names=['id_SubFed', 'educ_lvl'])
# exel_to_csv('data_xlsx/2021x.xlsx', '4.1. Образовательный уровень ГС', 2021, 'CSVs/EducationLevel_GS.csv',
#             [6,20], [4, 21],[5,7,9,10,11,12,13,14,15,16,17,18,19], m_id)
# exel_to_csv('data_xlsx/2021x.xlsx', '4.2. Образовательный уровень МС', 2021, 'CSVs/EducationLevel_MS.csv',
#             [6,20], [4, 21],[5,7,9,10,11,12,13,14,15,16,17,18,19], m_id)
#
# speciality = [
#     'менеджер ГМУ',
#     'экономист, финансист',
#     'юрист',
#     'инженер',
#     'иная специальность'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, speciality], names=['id_SubFed', 'speciality'])
# exel_to_csv('data_xlsx/2021x.xlsx', '4.1. Образовательный уровень ГС', 2021, 'CSVs/Educ_spec_GS.csv',
#             [6,20], [10, 20],[11,13,15,17,19], m_id)
# exel_to_csv('data_xlsx/2021x.xlsx', '4.2. Образовательный уровень МС', 2021, 'CSVs/Educ_spec_MS.csv',
#             [6,20], [10, 20],[11, 13, 15, 17, 19], m_id)
#
# degree = [
#     'Два и более высших образования',
#     'Кандидаты наук',
#     'Доктора наук'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, degree], names=['id_SubFed', 'degree'])
# exel_to_csv('data_xlsx/2021x.xlsx', '5.1. Ученая степень ГС', 2021, 'CSVs/AcademicDegree_GS.csv',
#             [4,18], [2, 7],[3, 5], m_id)
# exel_to_csv('data_xlsx/2021x.xlsx', '5.2. Ученая степень МС', 2021, 'CSVs/AcademicDegree_MS.csv',
#             [4,18], [2, 7],[3, 5], m_id)
#
# category = [
#     'до 1 года',
#     'от 1 года до 5 лет',
#     'от 5 до 10 лет',
#     'от 10 до 15 лет',
#     'свыше 15 лет'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '6.1. Стаж ГС', 2021, 'CSVs/Exp_GS.csv',
#             [4,18], [2, 11],[3, 5, 7, 9], m_id)
# exel_to_csv('data_xlsx/2021x.xlsx', '6.2. Стаж МС', 2021, 'CSVs/Exp_MS.csv',
#             [4,18], [2, 11],[3, 5, 7, 9], m_id)
#
# category = [
#     'Уволены на отчетную дату по инициативе служащего',
#     'Уволены на отчетную дату по инициативе представителя нанимателя ',
#     'Уволены на отчетную дату по истечению срока срочного служебного контракта',
#     'Уволены на отчетную дату по иным основаниям ',
#     'Количество служащих уволенных по достижению предельного возраста пребывания на службе',
#     'Количество уволенных служащих пребывавших в должности менее 1 года',
#     'Количество служащих уволенных в связи с сокращением штатной численности, преобразованием государственных органов',
#     'Количество служащих предупрежденных о предстоящем возможном увольнении'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '7. Сменяемость ГС', 2021, 'CSVs/Changeability_GS.csv',
#             [4,18], [4, 16],[5, 7, 9, 11], m_id)
#
# category = [
#     'Количество государственных органов на отчетную дату',
#     'Количество государственных органов на последнюю дату отчета предыдущего года'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '8. Кол-во гос.органов', 2021, 'CSVs/GosOrgAmount.csv',
#             [5,19], [2, 4],[], m_id)
#
# category = [
#     'Общее количество конкурсов',
#     'Конкурсы, проводимые повторно',
#     'Несостоявшиеся конкурсы',
#     'Конкурсы, результаты которых были обжалованы',
#     'Общее количество конкурсов на включение в кадровый резерв'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '9. Конкурсы', 2021, 'CSVs/Competition.csv',
#             [5,19], [2, 10],[4, 6, 8], m_id)
#
# category = [
#     'подали документы на замещение вакантных должностей государственной службы',
#     'в эл. виде подали документы на замещение вакантных должностей государственной службы',
#     'подали документы на включение в кадровый резерв',
#     'в эл. виде подали документы на включение в кадровый резерв',
#     'количество лиц, не допущенных для участия в конкурсе',
#     'количество лиц, не прошедших конкурсный отбор',
#     'количество лиц, назначенных на вакантную должность по результатам конкурса',
#     'количество лиц, включенных в кадровый резерв, по результатам конкурса на замещение',
#     'количество лиц, включенных в кадровый резерв, по результатам конкурса на включение в кадровый резерв',
#     'количество лиц, не участвовавших в конкурсе по причине признания конкурса несостоявшимся'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '10. Участие граждан', 2021, 'CSVs/CitizenParticipation.csv',
#             [6,20], [2, 17],[7, 9, 11, 13, 15], m_id)
#
# category = [
#     'В возрасте до 30 лет',
#     'С установлением испытательного срока',
#     'Количество лиц, назначенных на должности по результатам конкурса',
#     'Количество лиц, назначенных на должности в порядке должностного роста',
#     'Без конкурса, по срочному служебному контракту',
#     'Без конкурса, исполнение обязанностей по которым связано с государственной тайной',
#     'Без конкурса, из кадрового резерва',
#     'Без конкурса, по иным основаниям'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '11. Замещение', 2021, 'CSVs/Substitution.csv',
#             [7,21], [3, 17],[5, 7, 9, 11, 13, 15], m_id)
#
# category = [
#     'впервые поступившие на гос. службу',
#     'впервые поступившие на гос. службу, которым назначены наставники',
#     'впервые назначенных на высшие и главные должности гос. службы',
#     'впервые назначенных на высшие и главные должности гос. службы, которым назначены наставники',
#     'иные случаи установления наставничества',
#     'Назначенные наставники',
#     'Назначенные наставники, которым произведена доплата',
#     'Количество лиц, в отношении которых установленно наставничество'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '12. Наставничество', 2021, 'CSVs/Mentoring.csv',
#             [7,21], [2, 14],[4, 7, 9, 12], m_id)
#
# category = [
#     'Количество государственных органов, сформировавших резерв',
#     'граждан',
#     'государственных служащих'
# ]
# m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
# exel_to_csv('data_xlsx/2021x.xlsx', '13. Резерв', 2021, 'CSVs/ReserveComposition.csv',
#             [6,20], [2, 8],[3, 4, 6], m_id)
#
# def read_ReserveCause(path: str, year: int, csv_path: str):
#     cause = [
#         'по результатам конкурса на включение в кадровый резерв',
#         'по результатам конкурса на замещение вакантной должности',
#         'по результатам аттестации',
#         'в связи с сокращением должностей',
#         'по основаниям, предусмотренным ч.1 ст. 39 Федерального закона 79-ФЗ'
#     ]
#
#     df = pd.read_excel(path, sheet_name='13. Резерв', header=None)
#     df = df.iloc[6:20, 9:18]
#     df = df.drop([10, 12, 14, 16], axis=1)
#     df = df.stack().reset_index(drop=True).to_frame()
#     m_id = pd.MultiIndex.from_product([id_SubFed, cause], names=['id_SubFed', 'cause'])
#     df = df.set_axis(m_id, axis=0)
#     df = df.rename(columns={0: 'amount'})
#     df.insert(0, 'year', year)
#     df.to_csv(csv_path, sep=';')
#
# def read_Attestation(path: str, year: int, csv_path: str):
#     result = [
#         'соответствуют замещаемой должности',
#         'соответствуют замещаемой должности и рекомендованы к включению в кадровый резерв',
#         'соответствуют замещаемой должности при условии успешного получения дополнительного профессионального образования',
#         'не соответствуют замещаемой должности'
#     ]
#     period = [
#         'АППГ',
#         'с начала отчетного года'
#     ]
#
#     df = pd.read_excel(path, sheet_name='14. Аттестация', header=None)
#     df = df.iloc[6:20, 4:12]
#     df = df.stack().reset_index(drop=True).to_frame()
#     m_id = pd.MultiIndex.from_product([id_SubFed, result, period], names=['id_SubFed', 'result', 'period'])
#     df = df.set_axis(m_id, axis=0)
#     df = df.rename(columns={0: 'amount'})
#     df.insert(0, 'year', year)
#     df.to_csv(csv_path, sep=';')
#
# def read_Ranks(path: str, year: int, csv_path: str):
#     appointmentReason = [
#         'присвоен классный чин, без сдачи квалификационного экзамена',
#         'присвоен классный чин, по результатам квалификационного экзамена',
#         'ранее срока, установленного для прохождения службы в предыдущем классном чине'
#     ]
#     period = [
#         'АППГ',
#         'с начала отчетного года'
#     ]
#
#     df = pd.read_excel(path, sheet_name='15. Чины', header=None)
#     df = df.iloc[6:20, 6:17]
#     df = df.drop([7, 9, 11, 13, 15], axis=1)
#     df = df.stack().reset_index(drop=True).to_frame()
#     m_id = pd.MultiIndex.from_product([id_SubFed, appointmentReason, period], names=['id_SubFed', 'appointmentReason', 'period'])
#     df = df.set_axis(m_id, axis=0)
#     df = df.rename(columns={0: 'amount'})
#     df.insert(0, 'year', year)
#     df.to_csv(csv_path, sep=';')
#
# def read_TargetedTraining(path: str, year: int, csv_path: str):
#     categoty = [
#         'Количество граждан, заключивших договор о целевом обучении',
#         'Количество граждан, получивших профессиональное образование в соответствии с договором о целевом обучении',
#         'Количество граждан, поступивших на государственную службу в соответствии с договором о целевом обучении'
#     ]
#     period = [
#         'АППГ',
#         'с начала отчетного года'
#     ]
#
#     df = pd.read_excel(path, sheet_name='16. Целевое обучение', header=None)
#     df = df.iloc[5:19, 2:9]
#     df = df.drop([7], axis=1)
#     df = df.stack().reset_index(drop=True).to_frame()
#     m_id = pd.MultiIndex.from_product([id_SubFed, categoty, period], names=['id_SubFed', 'categoty', 'period'])
#     df = df.set_axis(m_id, axis=0)
#     df = df.rename(columns={0: 'amount'})
#     df.insert(0, 'year', year)
#     df.to_csv(csv_path, sep=';')
#
# def read_ProfDev_amount(path: str, year: int, csv_path: str):
#     categoty = [
#         'решения представителя нанимателя',
#         'по результатам аттестации',
#         'назначения на иную должность при сокращении должностей или упразднения государственного органа',
#         'назначения в порядке должностного роста впервые на должность категории "руководители" или "специалисты"',
#         'поступления гражданина на службу впервые'
#     ]
#
#     df = pd.read_excel(path, sheet_name='17.1. Профразвитие', header=None)
#     df = df.iloc[6:20, 4:9]
#     df = df.stack().reset_index(drop=True).to_frame()
#     m_id = pd.MultiIndex.from_product([id_SubFed, categoty], names=['id_SubFed', 'categoty'])
#     df = df.set_axis(m_id, axis=0)
#     df = df.rename(columns={0: 'amount'})
#     df.insert(0, 'year', year)
#     df.to_csv(csv_path, sep=';')
#
# def read_ProfDev_resources(path: str, year: int, csv_path: str):
#     resources = [
#         'Государственного заказа',
#         'Государственного задания',
#         'Средств государственного органа'
#     ]
#     res_type = [
#         'Объём финансирования (тыс. руб.)',
#         'Количество служащих'
#     ]
#     value_type = [
#         'план',
#         'факт'
#     ]
#
#     df = pd.read_excel(path, sheet_name='17.2. Профразвитие', header=None)
#     df = df.iloc[7:21, 2:14]
#     df = df.stack().reset_index(drop=True).to_frame()
#     m_id = pd.MultiIndex.from_product([id_SubFed, resources, res_type, value_type],
#                                       names=['id_SubFed', 'resources', 'res_type', 'value_type'])
#     df = df.set_axis(m_id, axis=0)
#     df = df.rename(columns={0: 'value'})
#     df.insert(0, 'year', year)
#     df.to_csv(csv_path, sep=';')
#
# def read_DPO_GS():
#     DPO = [
#         'Профессиональная переподготовка',
#         'Повышение квалификации'
#     ]
#     value_type = [
#         'Количество служащих',
#         'Объём финансирования (тыс. руб.)'
#     ]
#     value_name = [
#
#     ]
#
#
#
#
#
#
#
#
#
# # read_ReserveCause('data_xlsx/2021x.xlsx', 2021, 'CSVs/ReserveCause.csv')
# # read_Attestation('data_xlsx/2021x.xlsx', 2021, 'CSVs/Attestation.csv')
# # read_Ranks('data_xlsx/2021x.xlsx', 2021, 'CSVs/Ranks.csv')
# # read_TargetedTraining('data_xlsx/2021x.xlsx', 2021, 'CSVs/TargetedTraining.csv')
# # read_ProfDev_amount('data_xlsx/2021x.xlsx', 2021, 'CSVs/ProfDev_amount.csv')
# # read_ProfDev_resources('data_xlsx/2021x.xlsx', 2021, 'CSVs/ProfDev_resources.csv')