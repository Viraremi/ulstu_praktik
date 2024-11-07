import pandas as pd

id_SubFed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def read_Amount_GS(path: str, year: int, csv_path: str):
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
    df.to_csv(csv_path, sep=';')

def read_Amount_MS(path: str, year: int, csv_path: str):
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
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year) # Добавляем колонку "год"
    df.to_csv(csv_path, sep=';')

def read_Gender_GS_MS(path: str, sheet: str, year: int, csv_path: str):
    gender = [
        'мужчины',
        'женщины'
    ]

    df = pd.read_excel(path, sheet_name=sheet, header=None)
    df = df.iloc[4:18, 2:6]
    df = df.drop([3, 5], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, gender], names=['id_SubFed', 'gender'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Age_GS_MS(path: str, sheet: str, year: int, csv_path: str):
    category = [
        'до 30 лет',
        'от 31 до 40 лет',
        'от 41 до 50 лет',
        'от 51 до 60 лет',
        'старше 61 года',
        'средний возраст служащих'
    ]

    df = pd.read_excel(path, sheet_name=sheet, header=None)
    df = df.iloc[4:18, 2:13]
    df = df.drop([3, 5, 7, 9, 11], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_EducationLevel_GS_MS(path: str, sheet: str, year: int, csv_path: str):
    educ_lvl = [
        'бакалавриат',
        'специалитет',
        'магистратура',
        'среднее профессиональное'
    ]


    df = pd.read_excel(path, sheet_name=sheet, header=None)
    df = df.iloc[6:20, 4:21]
    df = df.drop([5, 7, 9], axis=1)
    df = df.drop(df.columns[3:13], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, educ_lvl], names=['id_SubFed', 'educ_lvl'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=";")

def read_Educ_spec_GS_MS(path: str, sheet: str, year: int, csv_path: str):
    speciality = [
        'менеджер ГМУ',
        'экономист, финансист',
        'юрист',
        'инженер',
        'иная специальность'
    ]

    df = pd.read_excel(path, sheet_name=sheet, header=None)
    df = df.iloc[6:20, 10:20]
    df = df.drop([11, 13, 15, 17, 19], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, speciality], names=['id_SubFed', 'speciality'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_AcademicDegree_GS_MS(path: str, sheet: str, year: int, csv_path: str):
    degree = [
        'Два и более высших образования',
        'Кандидаты наук',
        'Доктора наук'
    ]

    df = pd.read_excel(path, sheet_name=sheet, header=None)
    df = df.iloc[4:18, 2:7]
    df = df.drop([3, 5], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, degree], names=['id_SubFed', 'degree'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Exp_GS_MS(path: str, sheet: str, year: int, csv_path: str):
    category = [
        'до 1 года',
        'от 1 года до 5 лет',
        'от 5 до 10 лет',
        'от 10 до 15 лет',
        'свыше 15 лет'
    ]

    df = pd.read_excel(path, sheet_name=sheet, header=None)
    df = df.iloc[4:18, 2:11]
    df = df.drop([3, 5, 7, 9], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Changeability_GS(path: str, year: int, csv_path: str):
    category = [
        'Уволены на отчетную дату по инициативе служащего',
        'Уволены на отчетную дату по инициативе представителя нанимателя ',
        'Уволены на отчетную дату по истечению срока срочного служебного контракта',
        'Уволены на отчетную дату по иным основаниям ',
        'Количество служащих уволенных по достижению предельного возраста пребывания на службе',
        'Количество уволенных служащих пребывавших в должности менее 1 года',
        'Количество служащих уволенных в связи с сокращением штатной численности, преобразованием государственных органов',
        'Количество служащих предупрежденных о предстоящем возможном увольнении'
    ]

    df = pd.read_excel(path, sheet_name='7. Сменяемость ГС', header=None)
    df = df.iloc[4:18, 4:16]
    df = df.drop([5, 7, 9, 11], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_GosOrgAmount(path: str, year: int, csv_path: str):
    category = [
        'Количество государственных органов на отчетную дату',
        'Количество государственных органов на последнюю дату отчета предыдущего года'
    ]

    df = pd.read_excel(path, sheet_name='8. Кол-во гос.органов', header=None)
    df = df.iloc[5:19, 2:4]
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Competition(path: str, year: int, csv_path: str):
    category = [
        'Общее количество конкурсов',
        'Конкурсы, проводимые повторно',
        'Несостоявшиеся конкурсы',
        'Конкурсы, результаты которых были обжалованы',
        'Общее количество конкурсов на включение в кадровый резерв'
    ]

    df = pd.read_excel(path, sheet_name='9. Конкурсы', header=None)
    df = df.iloc[5:19, 2:10]
    df = df.drop([4, 6, 8], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_CitizenParticipation(path: str, year: int, csv_path: str):
    category = [
        'подали документы на замещение вакантных должностей государственной службы',
        'в эл. виде подали документы на замещение вакантных должностей государственной службы',
        'подали документы на включение в кадровый резерв',
        'в эл. виде подали документы на включение в кадровый резерв',
        'количество лиц, не допущенных для участия в конкурсе',
        'количество лиц, не прошедших конкурсный отбор',
        'количество лиц, назначенных на вакантную должность по результатам конкурса',
        'количество лиц, включенных в кадровый резерв, по результатам конкурса на замещение',
        'количество лиц, включенных в кадровый резерв, по результатам конкурса на включение в кадровый резерв',
        'количество лиц, не участвовавших в конкурсе по причине признания конкурса несостоявшимся'
    ]

    df = pd.read_excel(path, sheet_name='10. Участие граждан', header=None)
    df = df.iloc[6:20, 2:17]
    df = df.drop([7, 9, 11, 13, 15], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Substitution(path: str, year: int, csv_path: str):
    category = [
        'В возрасте до 30 лет',
        'С установлением испытательного срока',
        'Количество лиц, назначенных на должности по результатам конкурса',
        'Количество лиц, назначенных на должности в порядке должностного роста',
        'Без конкурса, по срочному служебному контракту',
        'Без конкурса, исполнение обязанностей по которым связано с государственной тайной',
        'Без конкурса, из кадрового резерва',
        'Без конкурса, по иным основаниям'
    ]

    df = pd.read_excel(path, sheet_name='11. Замещение', header=None)
    df = df.iloc[7:21, 3:17]
    df = df.drop([5, 7, 9, 11, 13, 15], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Mentoring(path: str, year: int, csv_path: str):
    category = [
        'впервые поступившие на гос. службу',
        'впервые поступившие на гос. службу, которым назначены наставники',
        'впервые назначенных на высшие и главные должности гос. службы',
        'впервые назначенных на высшие и главные должности гос. службы, которым назначены наставники',
        'иные случаи установления наставничества',
        'Назначенные наставники',
        'Назначенные наставники, которым произведена доплата',
        'Количество лиц, в отношении которых установленно наставничество'
    ]

    df = pd.read_excel(path, sheet_name='12. Наставничество', header=None)
    df = df.iloc[7:21, 2:14]
    df = df.drop([4, 7, 9, 12], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_ReserveComposition(path: str, year: int, csv_path: str):
    category = [
        'Количество государственных органов, сформировавших резерв',
        'граждан',
        'государственных служащих'
    ]

    df = pd.read_excel(path, sheet_name='13. Резерв', header=None)
    df = df.iloc[6:20, 2:8]
    df = df.drop([3, 4, 6], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, category], names=['id_SubFed', 'category'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_ReserveCause(path: str, year: int, csv_path: str):
    cause = [
        'по результатам конкурса на включение в кадровый резерв',
        'по результатам конкурса на замещение вакантной должности',
        'по результатам аттестации',
        'в связи с сокращением должностей',
        'по основаниям, предусмотренным ч.1 ст. 39 Федерального закона 79-ФЗ'
    ]

    df = pd.read_excel(path, sheet_name='13. Резерв', header=None)
    df = df.iloc[6:20, 9:18]
    df = df.drop([10, 12, 14, 16], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, cause], names=['id_SubFed', 'cause'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Attestation(path: str, year: int, csv_path: str):
    result = [
        'соответствуют замещаемой должности',
        'соответствуют замещаемой должности и рекомендованы к включению в кадровый резерв',
        'соответствуют замещаемой должности при условии успешного получения дополнительного профессионального образования',
        'не соответствуют замещаемой должности'
    ]
    period = [
        'АППГ',
        'с начала отчетного года'
    ]

    df = pd.read_excel(path, sheet_name='14. Аттестация', header=None)
    df = df.iloc[6:20, 4:12]
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, result, period], names=['id_SubFed', 'result', 'period'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_Ranks(path: str, year: int, csv_path: str):
    appointmentReason = [
        'присвоен классный чин, без сдачи квалификационного экзамена',
        'присвоен классный чин, по результатам квалификационного экзамена',
        'ранее срока, установленного для прохождения службы в предыдущем классном чине'
    ]
    period = [
        'АППГ',
        'с начала отчетного года'
    ]

    df = pd.read_excel(path, sheet_name='15. Чины', header=None)
    df = df.iloc[6:20, 6:17]
    df = df.drop([7, 9, 11, 13, 15], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, appointmentReason, period], names=['id_SubFed', 'appointmentReason', 'period'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_TargetedTraining(path: str, year: int, csv_path: str):
    categoty = [
        'Количество граждан, заключивших договор о целевом обучении',
        'Количество граждан, получивших профессиональное образование в соответствии с договором о целевом обучении',
        'Количество граждан, поступивших на государственную службу в соответствии с договором о целевом обучении'
    ]
    period = [
        'АППГ',
        'с начала отчетного года'
    ]

    df = pd.read_excel(path, sheet_name='16. Целевое обучение', header=None)
    df = df.iloc[5:19, 2:9]
    df = df.drop([7], axis=1)
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, categoty, period], names=['id_SubFed', 'categoty', 'period'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_ProfDev_amount(path: str, year: int, csv_path: str):
    categoty = [
        'решения представителя нанимателя',
        'по результатам аттестации',
        'назначения на иную должность при сокращении должностей или упразднения государственного органа',
        'назначения в порядке должностного роста впервые на должность категории "руководители" или "специалисты"',
        'поступления гражданина на службу впервые'
    ]

    df = pd.read_excel(path, sheet_name='17.1. Профразвитие', header=None)
    df = df.iloc[6:20, 4:9]
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, categoty], names=['id_SubFed', 'categoty'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'amount'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')

def read_ProfDev_resources(path: str, year: int, csv_path: str):
    resources = [
        'Государственного заказа',
        'Государственного задания',
        'Средств государственного органа'
    ]
    res_type = [
        'Объём финансирования (тыс. руб.)',
        'Количество служащих'
    ]
    value_type = [
        'план',
        'факт'
    ]

    df = pd.read_excel(path, sheet_name='17.2. Профразвитие', header=None)
    df = df.iloc[7:21, 2:14]
    df = df.stack().reset_index(drop=True).to_frame()
    m_id = pd.MultiIndex.from_product([id_SubFed, resources, res_type, value_type],
                                      names=['id_SubFed', 'resources', 'res_type', 'value_type'])
    df = df.set_axis(m_id, axis=0)
    df = df.rename(columns={0: 'value'})
    df.insert(0, 'year', year)
    df.to_csv(csv_path, sep=';')
    
def read_DPO_GS():
    DPO = [
        'Профессиональная переподготовка',
        'Повышение квалификации'
    ]
    value_type = [
        'Количество служащих',
        'Объём финансирования (тыс. руб.)'
    ]
    value_name = [

    ]

read_Amount_GS('2021x.xlsx', 2021, 'CSVs/Amount_GS.csv') #'1.1. Кол-во ГС'
read_Amount_MS('2021x.xlsx', 2021, 'CSVs/Amount_MS.csv') #'1.2. Кол-во МС'
read_Gender_GS_MS('2021x.xlsx', '2.1. Гендерный ГС',  2021, 'CSVs/Gender_GS.csv')
read_Gender_GS_MS('2021x.xlsx', '2.2. Гендерный МС',  2021, 'CSVs/Gender_MS.csv')
read_Age_GS_MS('2021x.xlsx', '3.1. Возраст ГС',  2021, 'CSVs/Age_GS.csv')
read_Age_GS_MS('2021x.xlsx', '3.2. Возраст МС',  2021, 'CSVs/Age_MS.csv')
read_EducationLevel_GS_MS('2021x.xlsx', '4.1. Образовательный уровень ГС',  2021, 'CSVs/EducationLevel_GS.csv')
read_EducationLevel_GS_MS('2021x.xlsx', '4.2. Образовательный уровень МС',  2021, 'CSVs/EducationLevel_MS.csv')
read_Educ_spec_GS_MS('2021x.xlsx', '4.1. Образовательный уровень ГС', 2021, 'CSVs/Educ_spec_GS.csv')
read_Educ_spec_GS_MS('2021x.xlsx', '4.2. Образовательный уровень МС', 2021, 'CSVs/Educ_spec_MS.csv')
read_AcademicDegree_GS_MS('2021x.xlsx', '5.1. Ученая степень ГС', 2021, 'CSVs/AcademicDegree_GS.csv')
read_AcademicDegree_GS_MS('2021x.xlsx', '5.2. Ученая степень МС', 2021, 'CSVs/AcademicDegree_MS.csv')
read_Exp_GS_MS('2021x.xlsx', '6.1. Стаж ГС', 2021, 'CSVs/Exp_GS.csv')
read_Exp_GS_MS('2021x.xlsx', '6.2. Стаж МС', 2021, 'CSVs/Exp_MS.csv')
read_Changeability_GS('2021x.xlsx', 2021, 'CSVs/Changeability_GS.csv')
read_GosOrgAmount('2021x.xlsx', 2021, 'CSVs/GosOrgAmount.csv')
read_Competition('2021x.xlsx', 2021, 'CSVs/Competition.csv')
read_CitizenParticipation('2021x.xlsx', 2021, 'CSVs/CitizenParticipation.csv')
read_Substitution('2021x.xlsx', 2021, 'CSVs/Substitution.csv')
read_Mentoring('2021x.xlsx', 2021, 'CSVs/Mentoring.csv')
read_ReserveComposition('2021x.xlsx', 2021, 'CSVs/ReserveComposition.csv')
read_ReserveCause('2021x.xlsx', 2021, 'CSVs/ReserveCause.csv')
read_Attestation('2021x.xlsx', 2021, 'CSVs/Attestation.csv')
read_Ranks('2021x.xlsx', 2021, 'CSVs/Ranks.csv')
read_TargetedTraining('2021x.xlsx', 2021, 'CSVs/TargetedTraining.csv')
read_ProfDev_amount('2021x.xlsx', 2021, 'CSVs/ProfDev_amount.csv')
read_ProfDev_resources('2021x.xlsx', 2021, 'CSVs/ProfDev_resources.csv')
