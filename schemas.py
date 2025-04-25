from typing import Optional
from pydantic import BaseModel
from datetime import time


class MasjidBasic(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class MasjidDetail(BaseModel):
    id: int
    name: str
    location: str
    fjr: Optional[time] = None
    zuhr: Optional[time] = None
    asr: Optional[time] = None
    maghrib: Optional[time] = None
    isha: Optional[time] = None
    jumma: time
    have_washroom: bool
    have_wuzu_area: bool
    capacity: Optional[str] = None
    school: Optional[str] = None

    class Config:
        orm_mode = True