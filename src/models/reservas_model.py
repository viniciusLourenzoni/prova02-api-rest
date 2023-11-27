from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.models.voos_model import Voo


class Reserva(SQLModel, table=True):
    __tablename__ = "reservas"
    id: int = Field(default=None, primary_key=True)
    nome: datetime
    documento: str
    codigo_reserva: str
    voo_id: int = Field(nullable=False, foreign_key="voos.id")
    voos: Optional[Voo] = Relationship(back_populates="reservas")
