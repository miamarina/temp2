from uuid import uuid4

from sqlalchemy.orm import Session

from . import models, schemas


def get_pet_by_name(db: Session, name: str):
    return db.query(models.Pet).filter(models.Pet.name == name).first()


def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(name=pet.name, id=uuid4())
    db.add(db_pet)
    db.commit()
    return db_pet
