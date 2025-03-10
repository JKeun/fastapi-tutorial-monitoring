from typing import List, Union
from pandas import Timestamp
from pydantic import BaseModel


class DegreeBase(BaseModel):
    time: Timestamp
    degree: float
    sensor_id: int


class DegreeCreate(DegreeBase):
    pass


class Degree(DegreeBase):
    id: int

    class Config:
        orm_mode = True


class SensorBase(BaseModel):
    administer_id: int


class SensorCreate(SensorBase):
    pass


class Sensor(SensorBase):
    id: int
    degrees: List[Degree] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    sensors: List[Sensor] = []
    disabled: bool = False

    class Config:
        orm_mode = True