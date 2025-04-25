from db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time, Float

class Masajid(Base):
    __tablename__ = "masajid"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    # latitude = Column(Float, nullable=False)
    # longitude = Column(Float, nullable=False)

    fjr = Column(Time, nullable=True)
    zuhr = Column(Time, nullable=True)
    asr = Column(Time, nullable=True)
    maghrib = Column(Time, nullable=True)
    isha = Column(Time, nullable=True)
    jumma = Column(Time, nullable=False)

    have_washroom = Column(Boolean, default=False)
    have_wuzu_area = Column(Boolean, default=False)

    capacity = Column(String, nullable=True)
    school = Column(String, nullable=True) 

    def __str__(self):
        return f"Masjid: {self.name}, Location: ({self.latitude}, {self.longitude})"
    
