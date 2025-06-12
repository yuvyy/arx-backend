from pydantic import BaseModel

class PasswordBase(BaseModel):
    service_name: str
    password: str

class Password(PasswordBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True


