from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/pets/{pet_name}", response_model=schemas.Pet)
def read_pet(pet_name: str, db: Session = Depends(get_db)):
    db_pet = crud.get_pet_by_name(db, name=pet_name)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet


@app.post("/pets/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    print(pet)
    return crud.create_pet(db, pet)
