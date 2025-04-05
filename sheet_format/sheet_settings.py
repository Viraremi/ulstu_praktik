import json

Amount_GS = {
    'sheet': '1.1. Кол-во ГС',
    'iloc_rows': [6, 20],
    'iloc_columns': [6, 18],
    'drop_column': [9, 13, 14],
    'm_id_lists': [
        [
            'Численность государственных должностей субъекта Российской Федерации',
            'Численность должностей государственной гражданской службы',
            'Численность должностей, не отнесенных к должностям государственной гражданской службы'
        ],
        [
            'Всего', 'замещено', 'количество лиц, находящихся в отпуске по уходу за ребенком'
        ]
    ],
    'm_id_names': ['id_SubFed', 'group', 'status'],
    'csv_path': 'Amount_GS.csv'
}

Amount_MS = {
    'sheet': '1.2. Кол-во МС',
    'iloc_rows': [6, 20],
    'iloc_columns': [6, 14],
    'drop_column': [9, 13],
    'm_id_lists': [
        [
            'Численность должностей муниципальной службы',
            'Численность должностей, не отнесенных к должностям муниципальной службы'
        ],
        [
            'Всего', 'замещено', 'количество лиц, находящихся в отпуске по уходу за ребенком'
        ]
    ],
    'm_id_names': ['id_SubFed', 'group', 'status'],
    'csv_path': 'Amount_MS.csv'
}

Gender_GS = {
    'sheet': '2.1. Гендерный ГС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 6],
    'drop_column': [3, 5],
    'm_id_lists': [
        [
            'мужчины',
            'женщины'
        ]
    ],
    'm_id_names': ['id_SubFed', 'gender'],
    'csv_path': 'Gender_GS.csv'
}

Gender_MS = {
    'sheet': '2.2. Гендерный МС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 6],
    'drop_column': [3, 5],
    'm_id_lists': [
        [
            'мужчины',
            'женщины'
        ]
    ],
    'm_id_names': ['id_SubFed', 'gender'],
    'csv_path': 'Gender_MS.csv'
}

Age_GS = {
    'sheet': '3.1. Возраст ГС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 17],
    'drop_column': [3, 5, 7, 9, 11, 13, 15],
    'm_id_lists': [
        [
            'до 29 лет',
            'от 30 до 35 лет',
            'от 36 до 40 лет',
            'от 41 до 50 лет',
            'от 51 до 60 лет',
            'от 61 до 64 лет',
            'старше 65 года',
            'средний возраст служащих'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'Age_GS.csv'
}

Age_MS = {
    'sheet': '3.2. Возраст МС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 17],
    'drop_column': [3, 5, 7, 9, 11, 13, 15],
    'm_id_lists': [
        [
            'до 29 лет',
            'от 30 до 35 лет',
            'от 36 до 40 лет',
            'от 41 до 50 лет',
            'от 51 до 60 лет',
            'от 61 до 64 лет',
            'старше 65 года',
            'средний возраст служащих'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'Age_MS.csv'
}

EducationLevel_GS = {
    'sheet': '4.1. Образовательный уровень ГС',
    'iloc_rows': [6, 20],
    'iloc_columns': [3, 20],
    'drop_column': [4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    'm_id_lists': [
        [
            'бакалавриат',
            'специалитет',
            'магистратура',
            'среднее профессиональное'
        ]
    ],
    'm_id_names': ['id_SubFed', 'educ_lvl'],
    'csv_path': 'EducationLevel_GS.csv'
}

EducationLevel_MS = {
    'sheet': '4.2. Образовательный уровень МС',
    'iloc_rows': [6, 20],
    'iloc_columns': [3, 20],
    'drop_column': [4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    'm_id_lists': [
        [
            'бакалавриат',
            'специалитет',
            'магистратура',
            'среднее профессиональное'
        ]
    ],
    'm_id_names': ['id_SubFed', 'educ_lvl'],
    'csv_path': 'EducationLevel_MS.csv'
}

Educ_spec_GS = {
    'sheet': '4.1. Образовательный уровень ГС',
    'iloc_rows': [6, 20],
    'iloc_columns': [9, 19],
    'drop_column': [10, 12, 14, 16, 18],
    'm_id_lists': [
        [
            'менеджер ГМУ',
            'экономист, финансист',
            'юрист',
            'инженер',
            'иная специальность'
        ]
    ],
    'm_id_names': ['id_SubFed', 'speciality'],
    'csv_path': 'Educ_spec_GS.csv'
}

Educ_spec_MS = {
    'sheet': '4.2. Образовательный уровень МС',
    'iloc_rows': [6, 20],
    'iloc_columns': [9, 19],
    'drop_column': [10, 12, 14, 16, 18],
    'm_id_lists': [
        [
            'менеджер ГМУ',
            'экономист, финансист',
            'юрист',
            'инженер',
            'иная специальность'
        ]
    ],
    'm_id_names': ['id_SubFed', 'speciality'],
    'csv_path': 'Educ_spec_MS.csv'
}

AcademicDegree_GS = {
    'sheet': '5.1. Ученая степень ГС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 7],
    'drop_column': [3, 5],
    'm_id_lists': [
        [
            'Два и более высших образования',
            'Кандидаты наук',
            'Доктора наук'
        ]
    ],
    'm_id_names': ['id_SubFed', 'degree'],
    'csv_path': 'AcademicDegree_GS.csv'
}

AcademicDegree_MS = {
    'sheet': '5.2. Ученая степень МС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 7],
    'drop_column': [3, 5],
    'm_id_lists': [
        [
            'Два и более высших образования',
            'Кандидаты наук',
            'Доктора наук'
        ]
    ],
    'm_id_names': ['id_SubFed', 'degree'],
    'csv_path': 'AcademicDegree_MS.csv'
}

Exp_GS = {
    'sheet': '6.1. Стаж ГС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 13],
    'drop_column': [3, 5, 7, 9, 11],
    'm_id_lists': [
        [
            'до 1 года',
            'от 1 года до 5 лет',
            'от 5 до 10 лет',
            'от 10 до 15 лет',
            'от 15 до 25 лет',
            '25 лет и выше'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'Exp_GS.csv'
}

Exp_MS = {
    'sheet': '6.2. Стаж МС',
    'iloc_rows': [4, 18],
    'iloc_columns': [2, 13],
    'drop_column': [3, 5, 7, 9, 11],
    'm_id_lists': [
        [
            'до 1 года',
            'от 1 года до 5 лет',
            'от 5 до 10 лет',
            'от 10 до 15 лет',
            'от 15 до 25 лет',
            '25 лет и выше'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'Exp_MS.csv'
}

Changeability_GS = {
    'sheet': '7. Сменяемость ГС',
    'iloc_rows': [4, 18],
    'iloc_columns': [4, 20],
    'drop_column': [5, 7, 9, 11, 13, 16],
    'm_id_lists': [
        [
            'Уволены на отчетную дату по инициативе служащего',
            'Уволены на отчетную дату по соглашению сторон',
            'Уволены на отчетную дату по инициативе представителя нанимателя ',
            'Уволены на отчетную дату по истечению срока срочного служебного контракта',
            'Уволены на отчетную дату по иным основаниям ',
            'Количество служащих уволенных по достижению предельного возраста пребывания на службе',
            'Количество уволенных служащих пребывавших в должности менее 1 года',
            'Количество служащих уволенных в связи с сокращением штатной численности, '
            'преобразованием государственных органов',
            'Количество служащих предупрежденных о предстоящем возможном увольнении',
            'Коэффициент текучести кадров'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'Changeability_GS.csv'
}

GosOrgAmount = {
    'sheet': '8. Кол-во гос.органов',
    'iloc_rows': [5, 19],
    'iloc_columns': [2, 4],
    'drop_column': [],
    'm_id_lists': [
        [
            'Количество государственных органов на отчетную дату',
            'Количество государственных органов на последнюю дату отчета предыдущего года'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'GosOrgAmount.csv'
}

Competition = {
    'sheet': '9. Конкурсы',
    'iloc_rows': [5, 19],
    'iloc_columns': [2, 12],
    'drop_column': [3, 4, 6, 8, 10],
    'm_id_lists': [
        [
            'Общее количество конкурсов',
            'Конкурсы, проводимые повторно',
            'Несостоявшиеся конкурсы',
            'Конкурсы, результаты которых были обжалованы',
            'Общее количество конкурсов на включение в кадровый резерв'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'Competition.csv'
}

CitizenParticipation = {
    'sheet': '10. Участие граждан',
    'iloc_rows': [6, 20],
    'iloc_columns': [2, 17],
    'drop_column': [7, 9, 11, 13, 15],
    'm_id_lists': [
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
    'csv_path': 'CitizenParticipation.csv'
}

Substitution = {
    'sheet': '11. Замещение',
    'iloc_rows': [7, 21],
    'iloc_columns': [3, 17],
    'drop_column': [5, 7, 9, 11, 13, 15],
    'm_id_lists': [
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
    'csv_path': 'Substitution.csv'
}

Mentoring = {
    'sheet': '12. Наставничество',
    'iloc_rows': [7, 21],
    'iloc_columns': [3, 13],
    'drop_column': [5, 8, 10],
    'm_id_lists': [
        [
            'впервые поступившие на гос. службу',
            'впервые поступившие на гос. службу, которым назначены наставники',
            'впервые назначенных на высшие и главные должности гос. службы',
            'впервые назначенных на высшие и главные должности гос. службы, которым назначены наставники',
            'иные случаи установления наставничества',
            'Количество наставников, назначенных распорядительным актом органа',
            'Количество наставников, назначенных распорядительным актом органа, которым произведена доплата'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'Mentoring.csv'
}

ReserveComposition = {
    'sheet': '13. Резерв',
    'iloc_rows': [7, 21],
    'iloc_columns': [1, 16],
    'drop_column': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14],
    'm_id_lists': [
        [
            'Количество государственных органов, сформировавших резерв',
            'граждан',
            'государственных служащих'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'ReserveComposition.csv'
}

ReserveCause = {
    'sheet': '13. Резерв',
    'iloc_rows': [7, 21],
    'iloc_columns': [17, 26],
    'drop_column': [18, 20, 22, 24],
    'm_id_lists': [
        [
            'по результатам конкурса на включение в кадровый резерв',
            'по результатам конкурса на замещение вакантной должности',
            'по результатам аттестации',
            'в связи с сокращением должностей',
            'по основаниям, предусмотренным ч.1 ст. 39 Федерального закона 79-ФЗ'
        ]
    ],
    'm_id_names': ['id_SubFed', 'cause'],
    'csv_path': 'ReserveCause.csv'
}

Attestation = {
    'sheet': '14. Аттестация',
    'iloc_rows': [6, 20],
    'iloc_columns': [3, 11],
    'drop_column': [],
    'm_id_lists': [
        [
            'соответствуют замещаемой должности',
            'соответствуют замещаемой должности и рекомендованы к включению в кадровый резерв',
            'соответствуют замещаемой должности при условии успешного получения дополнительного '
            'профессионального образования',
            'не соответствуют замещаемой должности'
        ],
        [
            'АППГ',
            'с начала отчетного года'
        ]
    ],
    'm_id_names': ['id_SubFed', 'result', 'period'],
    'csv_path': 'Attestation.csv'
}

Ranks = {
    'sheet': '15. Чины',
    'iloc_rows': [6, 20],
    'iloc_columns': [2, 5],
    'drop_column': [3],
    'm_id_lists': [
        [
            'Количество служащих, которым присвоен классный чин',
        ],
        [
            'АППГ',
            'с начала отчетного года'
        ]
    ],
    'm_id_names': ['id_SubFed', 'appointmentReason', 'period'],
    'csv_path': 'Ranks.csv'
}

ProfDev_amount = {
    'sheet': '17.1. Профразвитие',
    'iloc_rows': [6, 20],
    'iloc_columns': [4, 10],
    'drop_column': [],
    'm_id_lists': [
        [
            'решения представителя нанимателя',
            'по результатам аттестации',
            'назначения на иную должность при сокращении должностей или упразднения государственного органа',
            'назначения в порядке должностного роста впервые на должность категории "руководители" или "специалисты"',
            'поступления гражданина на службу впервые',
            'по инициативе служащего'
        ]
    ],
    'm_id_names': ['id_SubFed', 'category'],
    'csv_path': 'ProfDev_amount.csv'
}

ProfDev_resources = {
    'sheet': '17.2. Профразвитие',
    'iloc_rows': [7, 21],
    'iloc_columns': [2, 18],
    'drop_column': [],
    'm_id_lists': [
        [
            'Государственного заказа',
            'Государственного задания',
            'Средств государственного органа',
            'Государственных образовательных сертификатов'
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
    'csv_path': 'ProfDev_resources.csv'
}

DPO_GS_1 = {
    'sheet': '17.3. ДПО ГС',
    'iloc_rows': [6, 20],
    'iloc_columns': [4, 22],
    'drop_column': [6, 7, 8, 9, 10, 15, 16, 17, 18, 19],
    'm_id_lists': [
        [
            'Профессиональная переподготовка',
            'Повышение квалификации'
        ],
        [
            'Количество служащих',
            'Объём финансирования (тыс. руб.)'
        ],
        [
            'план',
            'факт'
        ]
    ],
    'm_id_names': ['id_SubFed', 'DPO', 'value_type', 'value_name'],
    'csv_path': 'DPO_GS_1.csv'
}

DPO_GS_2 = {
    'sheet': '17.3. ДПО ГС',
    'iloc_rows': [6, 20],
    'iloc_columns': [4, 20],
    'drop_column': [4, 5, 6, 11, 12, 13, 14, 15],
    'm_id_lists': [
        [
            'Профессиональная переподготовка',
            'Повышение квалификации'
        ],
        [
            'Количество служащих'
        ],
        [
            'на основании государственных образовательных сертификатов ',
            'в т.ч. за счет средств федерального бюджета',
            'за счет собственных средств',
            'прошедших обучение в дистанционной форме'
        ]
    ],
    'm_id_names': ['id_SubFed', 'DPO', 'value_type', 'value_name'],
    'csv_path': 'DPO_GS_2.csv'
}

DPO_GS_other_1 = {
    'sheet': '17.4. ДПО ГС',
    'iloc_rows': [7, 21],
    'iloc_columns': [4, 8],
    'drop_column': [],
    'm_id_lists': [
        [
            'мероприятия, направленные на получение новых знаний, умений',
            'мероприятия, направленные на обмен опытом'
        ],
        [
            'план',
            'факт'
        ]
    ],
    'm_id_names': ['id_SubFed', 'DPO_type', 'value_type'],
    'csv_path': 'DPO_GS_other_1.csv'
}

DPO_GS_other_2 = {
    'sheet': '17.4. ДПО ГС',
    'iloc_rows': [7, 21],
    'iloc_columns': [8, 10],
    'drop_column': [],
    'm_id_lists': [
        [
            'служебные стажировки',
            'самообразование'
        ],
        [
            'факт'
        ]
    ],
    'm_id_names': ['id_SubFed', 'DPO_type', 'value_type'],
    'csv_path': 'DPO_GS_other_2.csv'
}

DPO_GS_other_3 = {
    'sheet': '17.4. ДПО ГС',
    'iloc_rows': [7, 21],
    'iloc_columns': [10, 12],
    'drop_column': [],
    'm_id_lists': [
        [
            'Объём финансирования, тыс.руб.'
        ],
        [
            'план',
            'факт'
        ]
    ],
    'm_id_names': ['id_SubFed', 'DPO_type', 'value_type'],
    'csv_path': 'DPO_GS_other.csv'
}

DPO_MS = {
    'sheet': '18. ДПО МС',
    'iloc_rows': [5, 19],
    'iloc_columns': [4, 9],
    'drop_column': [5, 7],
    'm_id_lists': [
        [
            'Профессиональная переподготовка',
            'Повышение квалификации',
            'иные образовательные программы'
        ]
    ],
    'm_id_names': ['id_SubFed', 'DPO_type'],
    'csv_path': 'DPO_MS.csv'
}

default_settings = {
    'Amount_GS': Amount_GS,
    'Amount_MS': Amount_MS,
    'Gender_GS': Gender_GS,
    'Gender_MS': Gender_MS,
    'Age_GS': Age_GS,
    'Age_MS': Age_MS,
    'EducationLevel_GS': EducationLevel_GS,
    'EducationLevel_MS': EducationLevel_MS,
    'Educ_spec_GS': Educ_spec_GS,
    'Educ_spec_MS': Educ_spec_MS,
    'AcademicDegree_GS': AcademicDegree_GS,
    'AcademicDegree_MS': AcademicDegree_MS,
    'Exp_GS': Exp_GS,
    'Exp_MS': Exp_MS,
    'Changeability_GS': Changeability_GS,
    'GosOrgAmount': GosOrgAmount,
    'Competition': Competition,
    'CitizenParticipation': CitizenParticipation,
    'Substitution': Substitution,
    'Mentoring': Mentoring,
    'ReserveComposition': ReserveComposition,
    'ReserveCause': ReserveCause,
    'Attestation': Attestation,
    'Ranks': Ranks,
    'ProfDev_amount': ProfDev_amount,
    'ProfDev_resources': ProfDev_resources,
    'DPO_GS_1': DPO_GS_1,
    'DPO_GS_2': DPO_GS_2,
    'DPO_GS_other_1': DPO_GS_other_1,
    'DPO_GS_other_2': DPO_GS_other_2,
    'DPO_GS_other_3': DPO_GS_other_3,
    'DPO_MS': DPO_MS
}


def update_or_reset_settings(settings: dict = None):
    print('Генерация файла настроек...')
    all_settings = default_settings if settings is None else settings
    json_string = json.dumps(all_settings, ensure_ascii=False, indent=4)
    with open("all_settings.json", "w", encoding="utf-8") as file:
        file.write(json_string)
    print('SUCCESS')


def get_json_string():
    try:
        with open("all_settings.json", "r", encoding="utf-8") as file:
            json_string = json.load(file)
            print("Настройки форматирования получены!")
        return json.dumps(json_string, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        return ""


def get_settings():
    try:
        with open("all_settings.json", "r", encoding="utf-8") as file:
            json_string = json.load(file)
            print("Настройки форматирования получены!")
        return json_string
    except FileNotFoundError:
        return {}
