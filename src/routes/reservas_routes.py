import random

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import select

from src.config.database import get_session
from src.models.reservas_model import Reserva
from src.models.voos_model import Voo

reservas_router = APIRouter(prefix="/reservas")


@reservas_router.get("/{id_voo}")
def lista_reservas_voo(id_voo: int):
    with get_session() as session:
        statement = select(Reserva).where(Reserva.voo_id == id_voo)
        reservas = session.exec(statement).all()
        return reservas


@reservas_router.post("")
def cria_reserva(reserva: Reserva):
    with get_session() as session:
        voo = session.exec(select(Voo).where(Voo.id == reserva.voo_id)).first()

        if not voo:
            return JSONResponse(
                content={"message": f"Voo com id {reserva.voo_id} não encontrado."},
                status_code=404,
            )

        if (
            session.exec(
                select(Reserva).where(Reserva.documento == reserva.documento)
            ).first()
            is not None
        ):
            return JSONResponse(
                content={
                    "message": f"Já existe uma reserva para o documento {reserva.documento}"
                },
                status_code=403)

        codigo_reserva = "".join(
            [str(random.randint(0, 999)).zfill(3) for _ in range(2)]
        )

        reserva.codigo_reserva = codigo_reserva
        session.commit()
        session.refresh(reserva)
        return reserva


@reservas_router.post("/{codigo_reserva}/checkin/{num_poltrona}")
def faz_checkin(codigo_reserva: str, num_poltrona: int):
    with get_session() as session:
        reserva = session.exec(select(Reserva).where(Reserva.codigo_reserva == codigo_reserva)).first()

        session.add(reserva)
        if not reserva:
            return JSONResponse(
                content={"message": f"Reserva com código {codigo_reserva} não encontrada."},
                status_code=404,
            )

        if reserva.num_poltrona:
            return JSONResponse(
                content={"message": f"Reserva com código {codigo_reserva} já possui uma poltrona atribuída."},
                status_code=403,
            )

        if (
            session.exec(
                select(Reserva).where(Reserva.num_poltrona == num_poltrona)
            ).first()
            is not None
        ):
            return JSONResponse(
                content={"message": "Poltrona ocupada"},
                status_code=403,
            )

        reserva.num_poltrona = num_poltrona
        session.commit()
        session.refresh(reserva)
        return reserva
