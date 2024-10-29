import pandas as pd

from vk.schemas.user import UserSchema

from typing import List


class UsersTable:
    _df: pd.DataFrame = None
    _columns: List[str] = ['user_id', 'first_name', 'last_name', 'bdate', 'sex', 'country', 'city', 'photo']

    def __init__(self, users: List[UserSchema]) -> None:
        self._users = users

    def create(self) -> pd.DataFrame | None:
        self._df = pd.DataFrame(
            data=[user.dict() for user in self._users],
            columns=self._columns
        )
        return self._df

    def save(self) -> None:
        self._df.to_csv(r'C:\Users\andre\Project_Avito_Parser\pythonProject\storage\users.csv')


df = pd.read_csv(r'C:\Users\andre\Project_Avito_Parser\pythonProject\storage\users.csv')
print(df['user_id'])