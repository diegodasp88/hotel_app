from datetime import datetime
from enum import StrEnum
from repository.person import Client
from repository.room import Room
from enum import StrEnum

class ReservStatus(StrEnum):
    CONFIRMADO = "Confirmado"
    CANCELADO = "Cancelado"
    PENDENTE = "Pendente"  # Aguardando pagamento


class Reservation:
    def __init__(self,
                 reserv_id: int, 
                 reserv_owner: str, 
                 reserv_room: int,
                 check_in: datetime,
                 check_out: datetime,
                 reserv_status: ReservStatus):
        self.reserv_id = reserv_id
        self.reserv_owner = reserv_owner
        self.reserv_room = reserv_room
        self.check_in = check_in
        self.check_out = check_out
        self.reserv_status = reserv_status

    def to_dict(self):
        return {
            "ID": self.reserv_id,
            "Titular": self.reserv_owner,
            "Quarto": self.reserv_room,
            "Check-in": self.check_in,
            "Check-out": self.check_out,
            "Status": self.reserv_status
        }
