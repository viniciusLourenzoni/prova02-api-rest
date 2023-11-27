from fastapi import APIRouter
from sqlmodel import select

from src.config.database import get_session
from src.models.voos_model import Voo

voos_router = APIRouter(prefix="/voos")


@voos_router.post("")
def cria_voo(voo: Voo):
    with get_session() as session:
        session.add(voo)
        session.commit()
        session.refresh(voo)
        return voo


@voos_router.get("/{id_voo}")
def lista_voo(id_voo: int):
    with get_session() as session:
        statement = select(Voo).where(Voo.id == id_voo)
        voo = session.exec(statement).first()
        return voo
