import json

id_SubFed = ['Республика Башкортостан',
             'Республика Марий Эл',
             'Республика Мордовия',
             'Республика Татарстан',
             'Удмуртская Республика',
             'Чувашская Республика',
             'Пермский край',
             'Кировская область',
             'Нижегородская область',
             'Оренбургская область',
             'Пензенская область',
             'Самарская область',
             'Саратовская область',
             'Ульяновская область']

Amount_GS = {
    'sheet' : '1.1. Кол-во ГС',
    'iloc_rows' : [6,20],
    'iloc_columns' : [6, 18],
    'drop_column' : [9, 13, 17],
    'm_id_lists' : [
        id_SubFed,
        [
        'Численность государственных должностей субъекта Российской Федерации',
        'Численность должностей государственной гражданской службы',
        'Численность должностей, не отнесенных к должностям государственной гражданской службы'
        ],
        [
        'Всего',
        'замещено',
        'количество лиц, находящихся в отпуске по уходу за ребенком'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'group', 'status'],
    'csv_path' : 'CSVs/Amount_GS.csv'
}

Amount_MS = {
    'sheet' : '1.2. Кол-во МС',
    'iloc_rows' : [6,20],
    'iloc_columns' : [6, 14],
    'drop_column' : [9, 13],
    'm_id_lists' : [
        id_SubFed,
        [
            'Численность должностей муниципальной службы',
            'Численность должностей, не отнесенных к должностям муниципальной службы'
        ],
        [
        'Всего',
        'замещено',
        'количество лиц, находящихся в отпуске по уходу за ребенком'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'group', 'status'],
    'csv_path' : 'CSVs/Amount_MS.csv'
}

Gender_GS = {
    'sheet' : '2.1. Гендерный ГС',
    'iloc_rows' : [4,18],
    'iloc_columns' : [2, 6],
    'drop_column' : [3, 5],
    'm_id_lists' : [
        id_SubFed,
        [
            'мужчины',
            'женщины'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'gender'],
    'csv_path' : 'CSVs/Gender_GS.csv'
}

Gender_MS = {
    'sheet' : '2.2. Гендерный МС',
    'iloc_rows' : [4,18],
    'iloc_columns' : [2, 6],
    'drop_column' : [3, 5],
    'm_id_lists' : [
        id_SubFed,
        [
            'мужчины',
            'женщины'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'gender'],
    'csv_path' : 'CSVs/Gender_MS.csv'
}

Age_GS = {
    'sheet' : '3.1. Возраст ГС',
    'iloc_rows' : [4,18],
    'iloc_columns' : [2, 13],
    'drop_column' : [3, 5, 7, 9, 11],
    'm_id_lists' : [
        id_SubFed,
        [
            'до 30 лет',
            'от 31 до 40 лет',
            'от 41 до 50 лет',
            'от 51 до 60 лет',
            'старше 61 года',
            'средний возраст служащих'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'category'],
    'csv_path' : 'CSVs/Age_GS.csv'
}

Age_MS = {
    'sheet' : '3.2. Возраст МС',
    'iloc_rows' : [4,18],
    'iloc_columns' : [2, 13],
    'drop_column' : [3, 5, 7, 9, 11],
    'm_id_lists' : [
        id_SubFed,
        [
            'до 30 лет',
            'от 31 до 40 лет',
            'от 41 до 50 лет',
            'от 51 до 60 лет',
            'старше 61 года',
            'средний возраст служащих'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'category'],
    'csv_path' : 'CSVs/Age_MS.csv'
}

EducationLevel_GS = {
    'sheet' : '4.1. Образовательный уровень ГС',
    'iloc_rows' : [6,20],
    'iloc_columns' : [4, 21],
    'drop_column' : [5,7,9,10,11,12,13,14,15,16,17,18,19],
    'm_id_lists' : [
        id_SubFed,
        [
            'бакалавриат',
            'специалитет',
            'магистратура',
            'среднее профессиональное'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'educ_lvl'],
    'csv_path' : 'CSVs/EducationLevel_GS.csv'
}

EducationLevel_MS = {
    'sheet' : '4.2. Образовательный уровень МС',
    'iloc_rows' : [6,20],
    'iloc_columns' : [4, 21],
    'drop_column' : [5,7,9,10,11,12,13,14,15,16,17,18,19],
    'm_id_lists' : [
        id_SubFed,
        [
            'бакалавриат',
            'специалитет',
            'магистратура',
            'среднее профессиональное'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'educ_lvl'],
    'csv_path' : 'CSVs/EducationLevel_MS.csv'
}

Educ_spec_GS = {
    'sheet' : '4.1. Образовательный уровень ГС',
    'iloc_rows' : [6,20],
    'iloc_columns' : [10, 20],
    'drop_column' : [11,13,15,17,19],
    'm_id_lists' : [
        id_SubFed,
        [
            'менеджер ГМУ',
            'экономист, финансист',
            'юрист',
            'инженер',
            'иная специальность'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'speciality'],
    'csv_path' : 'CSVs/Educ_spec_GS.csv'
}

Educ_spec_MS = {
    'sheet' : '4.2. Образовательный уровень МС',
    'iloc_rows' : [6,20],
    'iloc_columns' : [10, 20],
    'drop_column' : [11,13,15,17,19],
    'm_id_lists' : [
        id_SubFed,
        [
            'менеджер ГМУ',
            'экономист, финансист',
            'юрист',
            'инженер',
            'иная специальность'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'speciality'],
    'csv_path' : 'CSVs/Educ_spec_MS.csv'
}

AcademicDegree_GS = {
    'sheet' : '5.1. Ученая степень ГС',
    'iloc_rows' : [4,18],
    'iloc_columns' : [2, 7],
    'drop_column' : [3, 5],
    'm_id_lists' : [
        id_SubFed,
        [
            'Два и более высших образования',
            'Кандидаты наук',
            'Доктора наук'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'degree'],
    'csv_path' : 'CSVs/AcademicDegree_GS.csv'
}

AcademicDegree_MS = {
    'sheet' : '5.2. Ученая степень МС',
    'iloc_rows' : [4,18],
    'iloc_columns' : [2, 7],
    'drop_column' : [3, 5],
    'm_id_lists' : [
        id_SubFed,
        [
            'Два и более высших образования',
            'Кандидаты наук',
            'Доктора наук'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'degree'],
    'csv_path' : 'CSVs/AcademicDegree_MS.csv'
}

Exp_GS = {
    'sheet' : '6.1. Стаж ГС',
    'iloc_rows' : [4, 18],
    'iloc_columns' : [2, 11],
    'drop_column' : [3,5,7,9],
    'm_id_lists' : [
        id_SubFed,
        [
            'до 1 года',
            'от 1 года до 5 лет',
            'от 5 до 10 лет',
            'от 10 до 15 лет',
            'свыше 15 лет'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'category'],
    'csv_path' : 'CSVs/Exp_GS.csv'
}

Exp_MS = {
    'sheet' : '6.2. Стаж МС',
    'iloc_rows' : [4, 18],
    'iloc_columns' : [2, 11],
    'drop_column' : [3,5,7,9],
    'm_id_lists' : [
        id_SubFed,
        [
            'до 1 года',
            'от 1 года до 5 лет',
            'от 5 до 10 лет',
            'от 10 до 15 лет',
            'свыше 15 лет'
        ]
        ],
    'm_id_names' : ['id_SubFed', 'category'],
    'csv_path' : 'CSVs/Exp_MS.csv'
}

Changeability_GS = {
    'sheet': '7. Сменяемость ГС',
    'iloc_rows': [4, 18],
    'iloc_columns': [4, 16],
    'drop_column': [5,7,9,11],
    'm_id_lists': [
        id_SubFed,
        [
            'Уволены на отчетную дату по инициативе служащего',
            'Уволены на отчетную дату по инициативе представителя нанимателя ',
            'Уволены на отчетную дату по истечению срока срочного служебного контракта',
            'Уволены на отчетную дату по иным основаниям ',
            'Количество служащих уволенных по достижению предельного возраста пребывания на службе',
            'Количество уволенных служащих пребывавших в должности менее 1 года',
            'Количество служащих уволенных в связи с сокращением штатной численности, преобразованием государственных органов',
            'Количество служащих предупрежденных о предстоящем возможном увольнении'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'CSVs/Changeability_GS.csv'
}

GosOrgAmount = {
    'sheet': '8. Кол-во гос.органов',
    'iloc_rows': [5, 19],
    'iloc_columns': [2, 4],
    'drop_column': [],
    'm_id_lists': [
        id_SubFed,
        [
            'Количество государственных органов на отчетную дату',
            'Количество государственных органов на последнюю дату отчета предыдущего года'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'CSVs/GosOrgAmount.csv'
}

Competition = {
    'sheet': '9. Конкурсы',
    'iloc_rows': [5, 19],
    'iloc_columns': [2, 10],
    'drop_column': [4, 6, 8],
    'm_id_lists': [
        id_SubFed,
        [
            'Общее количество конкурсов',
            'Конкурсы, проводимые повторно',
            'Несостоявшиеся конкурсы',
            'Конкурсы, результаты которых были обжалованы',
            'Общее количество конкурсов на включение в кадровый резерв'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'CSVs/Competition.csv'
}

CitizenParticipation = {
    'sheet': '10. Участие граждан',
    'iloc_rows': [6, 20],
    'iloc_columns': [2, 17],
    'drop_column': [7, 9, 11, 13, 15],
    'm_id_lists': [
        id_SubFed,
        [
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
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'CSVs/CitizenParticipation.csv'
}

Substitution = {
    'sheet': '11. Замещение',
    'iloc_rows': [7, 21],
    'iloc_columns': [3, 17],
    'drop_column': [5,7,9,11,13,15],
    'm_id_lists': [
        id_SubFed,
        [
            'В возрасте до 30 лет',
            'С установлением испытательного срока',
            'Количество лиц, назначенных на должности по результатам конкурса',
            'Количество лиц, назначенных на должности в порядке должностного роста',
            'Без конкурса, по срочному служебному контракту',
            'Без конкурса, исполнение обязанностей по которым связано с государственной тайной',
            'Без конкурса, из кадрового резерва',
            'Без конкурса, по иным основаниям'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'CSVs/Substitution.csv'
}

Mentoring = {
    'sheet': '12. Наставничество',
    'iloc_rows': [7, 21],
    'iloc_columns': [2, 14],
    'drop_column': [4,7,9,12],
    'm_id_lists': [
        id_SubFed,
        [
            'впервые поступившие на гос. службу',
            'впервые поступившие на гос. службу, которым назначены наставники',
            'впервые назначенных на высшие и главные должности гос. службы',
            'впервые назначенных на высшие и главные должности гос. службы, которым назначены наставники',
            'иные случаи установления наставничества',
            'Назначенные наставники',
            'Назначенные наставники, которым произведена доплата',
            'Количество лиц, в отношении которых установленно наставничество'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'CSVs/Mentoring.csv'
}

ReserveComposition = {
    'sheet': '13. Резерв',
    'iloc_rows': [6, 20],
    'iloc_columns': [2, 8],
    'drop_column': [3,4,6],
    'm_id_lists': [
        id_SubFed,
        [
            'Количество государственных органов, сформировавших резерв',
            'граждан',
            'государственных служащих'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'CSVs/ReserveComposition.csv'
}

ReserveCause = {
    'sheet': '13. Резерв',
    'iloc_rows': [6, 20],
    'iloc_columns': [9, 18],
    'drop_column': [10,12,14,16],
    'm_id_lists': [
        id_SubFed,
        [
            'по результатам конкурса на включение в кадровый резерв',
            'по результатам конкурса на замещение вакантной должности',
            'по результатам аттестации',
            'в связи с сокращением должностей',
            'по основаниям, предусмотренным ч.1 ст. 39 Федерального закона 79-ФЗ'
        ]
    ],
    'm_id_names': ['id_SubFed', 'cause'],
    'csv_path': 'CSVs/ReserveCause.csv'
}

Attestation = {
    'sheet': '14. Аттестация',
    'iloc_rows': [6, 20],
    'iloc_columns': [4, 12],
    'drop_column': [],
    'm_id_lists': [
        id_SubFed,
        [
            'соответствуют замещаемой должности',
            'соответствуют замещаемой должности и рекомендованы к включению в кадровый резерв',
            'соответствуют замещаемой должности при условии успешного получения дополнительного профессионального образования',
            'не соответствуют замещаемой должности'
        ],
        [
            'АППГ',
            'с начала отчетного года'
        ]
    ],
    'm_id_names': ['id_SubFed', 'result', 'period'],
    'csv_path': 'CSVs/Attestation.csv'
}

Ranks = {
    'sheet': '15. Чины',
    'iloc_rows': [6, 20],
    'iloc_columns': [6, 17],
    'drop_column': [7,9,11,13,15],
    'm_id_lists': [
        id_SubFed,
        [
            'присвоен классный чин, без сдачи квалификационного экзамена',
            'присвоен классный чин, по результатам квалификационного экзамена',
            'ранее срока, установленного для прохождения службы в предыдущем классном чине'
        ],
        [
            'АППГ',
            'с начала отчетного года'
        ]
    ],
    'm_id_names': ['id_SubFed', 'appointmentReason', 'period'],
    'csv_path': 'CSVs/Ranks.csv'
}

TargetedTraining = {
    'sheet': '16. Целевое обучение',
    'iloc_rows': [5, 19],
    'iloc_columns': [2, 9],
    'drop_column':[7],
    'm_id_lists': [
        id_SubFed,
        [
            'Количество граждан, заключивших договор о целевом обучении',
            'Количество граждан, получивших профессиональное образование в соответствии с договором о целевом обучении',
            'Количество граждан, поступивших на государственную службу в соответствии с договором о целевом обучении'
        ],
        [
            'АППГ',
            'с начала отчетного года'
        ]
    ],
    'm_id_names': ['id_SubFed', 'categoty', 'period'],
    'csv_path': 'CSVs/TargetedTraining.csv'
}

ProfDev_amount = {
    'sheet': '17.1. Профразвитие',
    'iloc_rows': [6, 20],
    'iloc_columns': [4, 9],
    'drop_column':[],
    'm_id_lists': [
        id_SubFed,
        [
            'решения представителя нанимателя',
            'по результатам аттестации',
            'назначения на иную должность при сокращении должностей или упразднения государственного органа',
            'назначения в порядке должностного роста впервые на должность категории "руководители" или "специалисты"',
            'поступления гражданина на службу впервые'
        ]
    ],
    'm_id_names': ['id_SubFed', 'categoty'],
    'csv_path': 'CSVs/ProfDev_amount.csv'
}

ProfDev_resources = {
    'sheet': '17.2. Профразвитие',
    'iloc_rows': [7, 21],
    'iloc_columns': [2, 14],
    'drop_column': [],
    'm_id_lists': [
        id_SubFed,
        [
            'Государственного заказа',
            'Государственного задания',
            'Средств государственного органа'
        ],
        [
            'Объём финансирования (тыс. руб.)',
            'Количество служащих'
        ],
        [
            'план',
            'факт'
        ]
    ],
    'm_id_names': ['id_SubFed', 'resources', 'res_type', 'value_type'],
    'csv_path': 'CSVs/ProfDev_resources.csv'
}

all_settings = {
    'Amount_GS' : Amount_GS,
    'Amount_MS' : Amount_MS,
    'Gender_GS' : Gender_GS,
    'Gender_MS' : Gender_MS,
    'Age_GS' : Age_GS,
    'Age_MS' : Age_MS,
    'EducationLevel_GS' : EducationLevel_GS,
    'EducationLevel_MS' : EducationLevel_MS,
    'Educ_spec_GS' : Educ_spec_GS,
    'Educ_spec_MS' : Educ_spec_MS,
    'AcademicDegree_GS' : AcademicDegree_GS,
    'AcademicDegree_MS' : AcademicDegree_MS,
    'Exp_GS' : Exp_GS,
    'Exp_MS' : Exp_MS,
    'Changeability_GS' : Changeability_GS,
    'GosOrgAmount' : GosOrgAmount,
    'Competition' : Competition,
    'CitizenParticipation' : CitizenParticipation,
    'Substitution' : Substitution,
    'Mentoring' : Mentoring,
    'ReserveComposition' : ReserveComposition,
    'ReserveCause' : ReserveCause,
    'Attestation' : Attestation,
    'Ranks' : Ranks,
    'TargetedTraining' : TargetedTraining,
    'ProfDev_amount' : ProfDev_amount,
    'ProfDev_resources' : ProfDev_resources
}

json_string = json.dumps(all_settings, ensure_ascii=False, indent=4)
with open("all_settings.json", "w", encoding="utf-8") as file:
    file.write(json_string)