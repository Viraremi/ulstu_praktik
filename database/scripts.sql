CREATE TABLE "SubFed" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"name" VARCHAR(255) NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "SubFed" IS 'Субъект Федерации
Республика Башкортостан, Республика Марий Эл, и тд';


CREATE TABLE "Amount_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	-- Строка 4 в файле
	-- "Численность государственных должностей субъекта Российской Федерации" и тд
	"group" VARCHAR(255) NOT NULL,
	-- Строка 6 в файле
	-- "всего", "замещено, чел.", "количество лиц, находящихся в отпуске по уходу за ребенком"
	"status" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL CHECK(значение),
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Amount_GS" IS '1.1. Кол-во ГС
Количественный состав государственных служащих';
COMMENT ON COLUMN Amount_GS.year IS 'данные за Х год';
COMMENT ON COLUMN Amount_GS.group IS 'Строка 4 в файле
"Численность государственных должностей субъекта Российской Федерации" и тд';
COMMENT ON COLUMN Amount_GS.status IS 'Строка 6 в файле
"всего", "замещено, чел.", "количество лиц, находящихся в отпуске по уходу за ребенком"';


CREATE TABLE "Amount_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 4 в файле
	-- "Численность должностей муниципальной службы" и тд
	"group" VARCHAR(255) NOT NULL,
	-- Строка 6 в файле
	-- "всего", "замещено, чел.", "количество лиц, находящихся в отпуске по уходу за ребенком"
	"status" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Amount_MS" IS '1.2. Кол-во МС
Количественный состав муниципальных служащих';
COMMENT ON COLUMN Amount_MS.group IS 'Строка 4 в файле
"Численность должностей муниципальной службы" и тд';
COMMENT ON COLUMN Amount_MS.status IS 'Строка 6 в файле
"всего", "замещено, чел.", "количество лиц, находящихся в отпуске по уходу за ребенком"';
COMMENT ON COLUMN Amount_MS.year IS 'данные за Х год';


CREATE TABLE "Gender_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"gender" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Gender_GS" IS '2.1. Гендерный ГС
Гендерный состав государственных служащих';
COMMENT ON COLUMN Gender_GS.year IS 'данные за Х год';


CREATE TABLE "Gender_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"gender" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Gender_MS" IS '2.2. Гендерный МС
Гендерный состав муниципальных служащих';
COMMENT ON COLUMN Gender_MS.year IS 'данные за Х год';


CREATE TABLE "Age_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	-- Строка 4 в файле
	-- Категория людей по возрасту
	-- "возраст до 30 лет", "возраст от 31 до 40 лет" и тд
	"category" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Age_GS" IS '3.1. Возраст ГС
Возрастной состав государственных служащих';
COMMENT ON COLUMN Age_GS.category IS 'Строка 4 в файле
Категория людей по возрасту
"возраст до 30 лет", "возраст от 31 до 40 лет" и тд';
COMMENT ON COLUMN Age_GS.year IS 'данные за Х год';


CREATE TABLE "Age_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	-- Строка 4 в файле
	-- Категория людей по возрасту
	-- "возраст до 30 лет", "возраст от 31 до 40 лет" и тд
	"category" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Age_MS" IS '3.2. Возраст МС
Возрастной состав муниципальных служащих';
COMMENT ON COLUMN Age_MS.category IS 'Строка 4 в файле
Категория людей по возрасту
"возраст до 30 лет", "возраст от 31 до 40 лет" и тд';
COMMENT ON COLUMN Age_MS.year IS 'данные за Х год';


CREATE TABLE "EducationalLevel_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- E6-I6 в файле
	-- "бакалавриат", "специалитет", "магистратура"
	"educ_lvl" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "EducationalLevel_GS" IS '4.1. Образовательный уровень ГС
Образовательный уровень государственных служащих
Количество служащих с высшим образованием по уровням образования';
COMMENT ON COLUMN EducationalLevel_GS.educ_lvl IS 'E6-I6 в файле
"бакалавриат", "специалитет", "магистратура"';
COMMENT ON COLUMN EducationalLevel_GS.year IS 'данные за Х год';


CREATE TABLE "EducationalLevel_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- E6-I6 в файле
	-- 
	-- "бакалавриат", "специалитет", "магистратура"
	"educ_lvl" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "EducationalLevel_MS" IS '4.2. Образовательный уровень МС
Образовательный уровень муниципальных служащих
Количество служащих с высшим образованием по уровням образования';
COMMENT ON COLUMN EducationalLevel_MS.educ_lvl IS 'E6-I6 в файле

"бакалавриат", "специалитет", "магистратура"';
COMMENT ON COLUMN EducationalLevel_MS.year IS 'данные за Х год';


CREATE TABLE "Educ_spec_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- K6-S6 в файле
	-- специальность
	"speciality" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Educ_spec_GS" IS '4.1. Образовательный уровень ГС
Образовательный уровень государственных служащих
Количество служащих с высшим образованием по специальности';
COMMENT ON COLUMN Educ_spec_GS.speciality IS 'K6-S6 в файле
специальность';
COMMENT ON COLUMN Educ_spec_GS.year IS 'данные за Х год';


CREATE TABLE "Educ_spec_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- K6-S6 в файле
	-- специальность
	"speciality" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Educ_spec_MS" IS '4.2. Образовательный уровень МС
Образовательный уровень муниципальных служащих
Количество служащих с высшим образованием по специальности';
COMMENT ON COLUMN Educ_spec_MS.speciality IS 'K6-S6 в файле
специальность';
COMMENT ON COLUMN Educ_spec_MS.year IS 'данные за Х год';


CREATE TABLE "AcademicDegree_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"degree" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "AcademicDegree_GS" IS '5.1. Ученая степень ГС
Информация о наличии высших образований и ученых степеней у государственных служащих';
COMMENT ON COLUMN AcademicDegree_GS.year IS 'данные за Х год';


CREATE TABLE "AcademicDegree_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"degree" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "AcademicDegree_MS" IS '5.2. Ученая степень МС
Информация о наличии высших образований и ученых степеней у муниципальных служащих';
COMMENT ON COLUMN AcademicDegree_MS.year IS 'данные за Х год';


CREATE TABLE "Exp_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	-- Строк 4 в файле
	-- категория людей по стажу "до 1 года", "от 1 года до 5 лет" и тд
	"category" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Exp_GS" IS '6.1. Стаж ГС
Состав государственных служащих по стажу ';
COMMENT ON COLUMN Exp_GS.category IS 'Строк 4 в файле
категория людей по стажу "до 1 года", "от 1 года до 5 лет" и тд';
COMMENT ON COLUMN Exp_GS.year IS 'данные за Х год';


CREATE TABLE "Exp_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	-- Строка 4 в файле
	-- категория людей по стажу "до 1 года", "от 1 года до 5 лет" и тд
	"category" VARCHAR(255) NOT NULL,
	"id_SubFed" INTEGER NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Exp_MS" IS '6.2. Стаж МС
Состав муниципальных служащих по стажу ';
COMMENT ON COLUMN Exp_MS.category IS 'Строка 4 в файле
категория людей по стажу "до 1 года", "от 1 года до 5 лет" и тд';
COMMENT ON COLUMN Exp_MS.year IS 'данные за Х год';


CREATE TABLE "Changeability_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Причина увольнения
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Changeability_GS" IS '7. Сменяемость ГС
Сменяемость государственных служащих';
COMMENT ON COLUMN Changeability_GS.category IS 'Причина увольнения';
COMMENT ON COLUMN Changeability_GS.year IS 'данные за Х год';


CREATE TABLE "GosOrgAmount" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "GosOrgAmount" IS '8. Кол-во гос.органов
Информация о количестве государственных органов';
COMMENT ON COLUMN GosOrgAmount.year IS 'данные за Х год';


CREATE TABLE "Сompetitions" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 4 в файле
	-- Категория конкурсов
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Сompetitions" IS '9. Конкурсы
Информация о конкурсах на замещение вакантных должностей государственной службы в органах государственной власти, включении в кадровый резерв';
COMMENT ON COLUMN Сompetitions.category IS 'Строка 4 в файле
Категория конкурсов';
COMMENT ON COLUMN Сompetitions.year IS 'данные за Х год';


CREATE TABLE "CitizenParticipation" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Категория людей
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "CitizenParticipation" IS '10. Участие граждан
Информация об участии граждан в конкурсах на замещение вакантных должностей государственной службы, включении в кадровый резерв';
COMMENT ON COLUMN CitizenParticipation.category IS 'Категория людей';
COMMENT ON COLUMN CitizenParticipation.year IS 'данные за Х год';


CREATE TABLE "Substitution" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Категория людей по причинам земещения + "в возрасте до 30 лет"
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Substitution" IS '11. Замещение
Информация о замещении вакантных должностей государственной службы';
COMMENT ON COLUMN Substitution.category IS 'Категория людей по причинам земещения + "в возрасте до 30 лет"';
COMMENT ON COLUMN Substitution.year IS 'данные за Х год';


CREATE TABLE "Mentoring" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Mentoring" IS '12. Наставничество
Информация о наставничестве на государственной службе';
COMMENT ON COLUMN Mentoring.year IS 'данные за Х год';


CREATE TABLE "ReserveСomposition" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- C5, F5, H5
	-- гос. органы, граждане в резерве, гос. служащие в резерве
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "ReserveСomposition" IS '13. Резерв
Формирование кадрового резерва на государственной службе
Состав резерва и количество государственных органов, сформировавших резерв';
COMMENT ON COLUMN ReserveСomposition.category IS 'C5, F5, H5
гос. органы, граждане в резерве, гос. служащие в резерве';
COMMENT ON COLUMN ReserveСomposition.year IS 'данные за Х год';


CREATE TABLE "ReserveCause" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- J6, L6, N6, P6, R6
	-- Причина внесения в резерв
	"cause" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "ReserveCause" IS '13. Резерв
Формирование кадрового резерва на государственной службе
По причинам внесения в резерв';
COMMENT ON COLUMN ReserveCause.cause IS 'J6, L6, N6, P6, R6
Причина внесения в резерв';
COMMENT ON COLUMN ReserveCause.year IS 'данные за Х год';


CREATE TABLE "Attestation" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Результат аттестации
	"result" VARCHAR(255) NOT NULL,
	-- Строка 6 
	-- "АППГ", "с начала отчетного года"
	"period" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Attestation" IS '14. Аттестация
Аттестация государственных служащих';
COMMENT ON COLUMN Attestation.result IS 'Результат аттестации';
COMMENT ON COLUMN Attestation.period IS 'Строка 6 
"АППГ", "с начала отчетного года"';
COMMENT ON COLUMN Attestation.year IS 'данные за Х год';


CREATE TABLE "Ranks" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 5 в файле
	-- Причина присвоения чина
	"appointmentReason" VARCHAR(255) NOT NULL,
	-- Строка 6 
	-- "АППГ", "с начала отчетного года"
	"period" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "Ranks" IS '15. Чины
Информация о присвоении государственным служащим классных чинов';
COMMENT ON COLUMN Ranks.appointmentReason IS 'Строка 5 в файле
Причина присвоения чина';
COMMENT ON COLUMN Ranks.period IS 'Строка 6 
"АППГ", "с начала отчетного года"';
COMMENT ON COLUMN Ranks.year IS 'данные за Х год';


CREATE TABLE "ProfDev_amount" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 5
	-- Категории граждан по причине направления на профразвитие
	"category" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "ProfDev_amount" IS '17.1. Профразвитие
Профессиональное развитие государственных служащих
Количество служащих, принявших участие в мероприятиях по профессиональному развитию';
COMMENT ON COLUMN ProfDev_amount.category IS 'Строка 5
Категории граждан по причине направления на профразвитие';
COMMENT ON COLUMN ProfDev_amount.year IS 'данные за Х год';


CREATE TABLE "ProfDev_resources" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 5 в файле
	-- "гос заказ", "гос задание" и тд
	"resources" VARCHAR(255) NOT NULL,
	-- Строка 6 в файле
	-- "Оюъем финансирования", "Количество служащих"
	"res_type" VARCHAR(255) NOT NULL,
	"value_type" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "ProfDev_resources" IS '17.2. Профразвитие
Профессиональное развитие государственных служащих
Реализация мероприятий по профессиональному развитию служащих';
COMMENT ON COLUMN ProfDev_resources.resources IS 'Строка 5 в файле
"гос заказ", "гос задание" и тд';
COMMENT ON COLUMN ProfDev_resources.res_type IS 'Строка 6 в файле
"Оюъем финансирования", "Количество служащих"';
COMMENT ON COLUMN ProfDev_resources.year IS 'данные за Х год';


CREATE TABLE "DPO_GS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 4 в файле
	-- Вид ДПО
	"DPO" VARCHAR(255) NOT NULL,
	-- Строка 5 в файле 
	-- "кол-во служащих", "объем финансирования"
	"value_type" VARCHAR(255) NOT NULL,
	-- строка 6
	-- "план", "факт"
	"value_name" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "DPO_GS" IS '17.3. ДПО ГС
Дополнительное профессиональное образование (ДПО) государственных служащих';
COMMENT ON COLUMN DPO_GS.DPO IS 'Строка 4 в файле
Вид ДПО';
COMMENT ON COLUMN DPO_GS.value_type IS 'Строка 5 в файле 
"кол-во служащих", "объем финансирования"';
COMMENT ON COLUMN DPO_GS.value_name IS 'строка 6
"план", "факт"';
COMMENT ON COLUMN DPO_GS.year IS 'данные за Х год';


CREATE TABLE "DPO_GS_other" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 4 в файле 
	-- "кол-во служащих", "объем финансирования"
	"value_type" VARCHAR(255) NOT NULL,
	-- E6-J6
	-- Вид мероприятия
	"DPO_type" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "DPO_GS_other" IS '17.4. ДПО ГС
Иные мероприятия по профессиональному развитию государственных служащих';
COMMENT ON COLUMN DPO_GS_other.value_type IS 'Строка 4 в файле 
"кол-во служащих", "объем финансирования"';
COMMENT ON COLUMN DPO_GS_other.DPO_type IS 'E6-J6
Вид мероприятия';
COMMENT ON COLUMN DPO_GS_other.year IS 'данные за Х год';


CREATE TABLE "DPO_MS" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"id_SubFed" INTEGER NOT NULL,
	-- Строка 5 в файле
	-- Вид образовательной программы
	"DPO_type" VARCHAR(255) NOT NULL,
	"amount" REAL NOT NULL,
	-- данные за Х год
	"year" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

COMMENT ON TABLE "DPO_MS" IS '18. ДПО МС
Дополнительное профессиональное образование (ДПО) муниципальных служащих';
COMMENT ON COLUMN DPO_MS.DPO_type IS 'Строка 5 в файле
Вид образовательной программы';
COMMENT ON COLUMN DPO_MS.year IS 'данные за Х год';


ALTER TABLE "Amount_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Amount_MS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Gender_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Gender_MS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Age_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Age_MS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "EducationalLevel_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "EducationalLevel_MS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Educ_spec_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "AcademicDegree_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "AcademicDegree_MS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Exp_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Exp_MS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Changeability_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "GosOrgAmount"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Сompetitions"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Substitution"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "ReserveСomposition"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "ReserveCause"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Attestation"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Ranks"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "ProfDev_amount"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "CitizenParticipation"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Mentoring"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "ProfDev_resources"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "DPO_GS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "DPO_GS_other"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Educ_spec_MS"
ADD FOREIGN KEY("id_SubFed") REFERENCES "SubFed"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;