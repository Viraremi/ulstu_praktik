import os

from pandas import DataFrame, MultiIndex, read_excel

from sheet_format.model_settings import Setting


class BaseFormater:
    ID_SUB_FED = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    ULSK = [13]

    @staticmethod
    def save_to_csv(dataframe: DataFrame, file_path: str, separator: str) -> None:
        """Создаем нужные папки если их нет и конвертируем DataFrame в CSV"""
        folder = os.path.dirname(file_path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        dataframe.to_csv(file_path, sep=separator)

    @staticmethod
    def data_frame_from_excel(path: str, settings: Setting) -> DataFrame:
        """Получаем DataFrame из файла"""
        df = read_excel(path, sheet_name=settings.sheet, header=None)
        df = df.iloc[settings.iloc_rows[0]:settings.iloc_rows[1],
                     settings.iloc_columns[0]:settings.iloc_columns[1]]  # Обрезаем лишнее
        df = df.drop(settings.drop_column, axis=1)
        return df

    def start_format(self, sheet_settings: [str, Setting], file_path: str, file_year: int, save_path: str,
                     ignore_sheet: set, excel_to_csv=None):
        file_name = file_path.split("/")[-1]

        print('\nОткрываем файл ' + file_name)
        for key, settings in sheet_settings.items():
            if key in ignore_sheet:
                continue
            df = excel_to_csv(file_path, file_year, settings)
            self.save_to_csv(df, 'CSVs/' + settings.csv_path, ';')
            self.save_to_csv(df, save_path + '/result/' + settings.csv_path, ';')


class FullFormater(BaseFormater):
    def excel_to_csv(self, path: str, year: int, settings: Setting) -> DataFrame:
        """Функции обработки для полноценных файлов"""
        print('Обработка ' + settings.sheet + '...')
        df = self.data_frame_from_excel(path, settings)
        df = df.stack().reset_index(drop=True).to_frame()  # Складываем таблицу в одну большую строку
        m_id = MultiIndex.from_product([self.ID_SUB_FED] + settings.m_id_lists, names=settings.m_id_names)
        df = df.set_axis(m_id, axis=0)  # Присваиваем мультииндекс
        df.insert(0, 'year', str(year) + '-01-01')  # Добавляем колонку "год"
        df = df.rename(columns={0: 'amount'})
        return df

    def start_format(self, sheet_settings: [str, Setting], file_path: str, file_year: int, save_path: str,
                     ignore_sheet: set):
        super().start_format(sheet_settings, file_path, file_year, save_path, ignore_sheet, self.excel_to_csv)


class UlskFormater(BaseFormater):
    def excel_to_csv(self, path: str, year: int, settings: Setting) -> DataFrame:
        print('Обработка ' + settings.sheet + '...')
        df = self.data_frame_from_excel(path, settings)
        df = df.dropna(how='any')
        if df.size == 0:
            print('Ошибка ' + settings.sheet)
            return df
        df = df.stack().reset_index(drop=True).to_frame()  # Складываем таблицу в одну большую строку
        m_id = MultiIndex.from_product([self.ULSK] + settings.m_id_lists, names=settings.m_id_names)
        df = df.set_axis(m_id, axis=0)  # Присваиваем мультииндекс
        df.insert(0, 'year', str(year) + '-01-01')  # Добавляем колонку "год"
        df = df.rename(columns={0: 'amount'})
        return df

    def start_format(self, sheet_settings: [str, Setting], file_path: str, file_year: int, save_path: str,
                     ignore_sheet: set):
        super().start_format(sheet_settings, file_path, file_year, save_path, ignore_sheet, self.excel_to_csv)
