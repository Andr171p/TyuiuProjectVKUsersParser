from pydantic import BaseModel


class UserSchema(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    bdate: str
    sex: int
    country: str
    city: str
    photo: str
