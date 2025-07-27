from enum import StrEnum


class RoomType(StrEnum):
    SINGLE = "Solteiro"
    DOUBLE = "Casal"
    SUITE = "Suíte"

class RoomStatus(StrEnum):
    AVAILABLE = "Disponivel"
    OCCUPIED = "Ocupado"
    RESERVED = "Reservado"
    OUT_OF_SERVICE = "Fora de uso"

class Room:
    def __init__(self, 
                 room_number: int, 
                 room_type: RoomType, 
                 daily_rate: float,
                 room_status: RoomStatus):
        self.room_number = room_number
        self.room_type = room_type
        self.daily_rate = daily_rate
        self.room_status = room_status

    def to_dict(self):
        """Método para transformar os dados dos quartos em dicionário para salvar no bd."""
        return {
            "Quarto": self.room_number,
            "Tipo do quarto": self.room_type,
            "Taxa diaria ($)": f"{self.daily_rate:.2f}",
            "Status do quarto": self.room_status
        }