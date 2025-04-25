from typing import Union
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, Request

from db import get_db
import models
from schemas import MasjidBasic, MasjidDetail

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, request: Request):
    query_params = dict(request.query_params)
    return {
        "item_id": item_id,
        "query_params": query_params.get("q")
    }

@app.get("/masajids", response_model=list[MasjidBasic])
def get_masjid_basic(db: Session = Depends(get_db)):
    masajid = db.query(models.Masajid.id, models.Masajid.name).all()
    return [{"id": m.id, "name": m.name} for m in masajid]

@app.get("/masjid/{masjid_id}", response_model=MasjidDetail)
def get_masjid_by_id(masjid_id: int, db: Session = Depends(get_db)):
    masjid = db.query(models.Masajid).filter(models.Masajid.id == masjid_id).first()
    if not masjid:
        raise HTTPException(status_code=404, detail="Masjid not found")
    return masjid

@app.post("/submit")
async def submit_data(request: Request, db: Session = Depends(get_db)):
    query_params_data = dict(request.query_params)
    # data = await request.json()
    # print(data)

    name = query_params_data.get('masjid')
    location = query_params_data.get('location')
    fjr = query_params_data.get('fjr')
    zuhr = query_params_data.get('zuhr')
    asr = query_params_data.get('asr')
    maghrib = query_params_data.get('maghrib')
    isha = query_params_data.get('isha')
    jumma = query_params_data.get('jumma')
    washroom = query_params_data.get('washroom')
    wuzu = query_params_data.get('wuzu')
    capacity = query_params_data.get('capacity')
    school = query_params_data.get('shcool')

    print(name, location, fjr, zuhr, asr, maghrib, isha, jumma, washroom, wuzu, capacity, school)

    new_masjid = models.Masajid(name=name, location=location, fjr=fjr, zuhr=zuhr, asr=asr,maghrib=maghrib, isha=isha, jumma=jumma, have_wuzu_area=bool(wuzu), have_washroom=bool(washroom), capacity=capacity, school=school)

    db.add(new_masjid)
    db.commit()
    db.refresh(new_masjid)
    
    return {"message": "Data saved successfully"}
