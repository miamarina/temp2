import uuid

from pydantic import BaseModel


class PetBase(BaseModel):
    pass


class PetCreate(BaseModel):
    name: str


class Pet(BaseModel):
    id: uuid.UUID
    name: str

    class Config:
        orm_mode = True
