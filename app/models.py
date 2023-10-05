from sqlalchemy import Column, Integer, String, UUID

from .database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)

