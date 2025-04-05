from pydantic import BaseModel


class Setting(BaseModel):
    sheet: str
    iloc_rows: list[int]
    iloc_columns: list[int]
    drop_column: list[int]
    m_id_lists: list[list[str]]
    m_id_names: list[str]
    csv_path: str
