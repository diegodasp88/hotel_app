from tinydb import TinyDB, Query
from repository.person import Client
from repository.reservation import Reservation, ReservStatus
import repository.room as rm

client_db = TinyDB("storage/data/client_db.json")
rooms_db = TinyDB("storage/data/rooms_db.json")
reservations_db = TinyDB("storage/data/reserve_db.json")

# <QUARTOS> ============================
# Criando a tabela QUARTOS
rooms_table = rooms_db.table("rooms")

# Definindo os quartos
# rooms = [
#     rm.Room(room_number=101, room_type=rm.RoomType.SINGLE, daily_rate=150.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=102, room_type=rm.RoomType.DOUBLE, daily_rate=220.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=103, room_type=rm.RoomType.SUITE, daily_rate=350.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=201, room_type=rm.RoomType.SINGLE, daily_rate=150.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=202, room_type=rm.RoomType.DOUBLE, daily_rate=220.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=203, room_type=rm.RoomType.SUITE, daily_rate=350.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=301, room_type=rm.RoomType.SINGLE, daily_rate=150.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=302, room_type=rm.RoomType.DOUBLE, daily_rate=220.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
#     rm.Room(room_number=303, room_type=rm.RoomType.SUITE, daily_rate=350.00, room_status=rm.RoomStatus.AVAILABLE).to_dict(),
# ]
# rooms_table.insert_multiple(rooms)

def get_all_rooms():
    """Pega os dados de todos os quartos."""
    return rooms_table.all()

def listar_quartos_disponiveis():
        """Retorna uma lista de todos os quartos com status 'DISPONIVEL'."""
        Quarto = Query()
        return rooms_table.search(Quarto["Status do quarto"] == rm.RoomStatus.AVAILABLE)


# CLIENTES =============================
# Criando a tabela CLIENTES
clients_table = client_db.table("clients")

def client_id_autoincrement():
    """Cria automaticamente o ID do cliente. Retorna um número inteiro sequencial."""
    # Há algum cliente na tabela clients_table?
    if not clients_table.all(): 
    # Se não há...
        return 1
    # Se há...
    else: 
        # Descubrir o ID máximo existente.
        max_id = max(int(client["id"]) for client in clients_table.all())
        # Então acrescente 1 para um novo ID.
        return max_id + 1

def add_new_client(client: Client):
    """Adiciona um novo cliente no banco de dados"""
    clients_table.insert(client.to_dict())

def get_all_clients() -> dict:
    """Pega todos os dados dos clientes no banco de dados"""
    return clients_table.all()

def get_client_by_id(id: int) -> dict:
    """Pega um cliente específico ao informar seu ID"""
    Cliente = Query()
    return clients_table.get(Cliente.id == int(id))

def update_client_data(client: Client, id: int):
    """Atualiza os dados de um cliente no banco de dados pelo seu ID"""
    Cliente = Query()
    if clients_table.contains(Cliente.id == int(id)):
        clients_table.update(client.to_dict(), Cliente.id == int(id))

def remove_client_by_id(id: int) -> dict:
    """Remove o cliente do banco de dados pelo seu ID"""
    Cliente = Query()
    clients_table.remove(Cliente.id == int(id))

# RESERVAS =============================
# Criando a tabela RESERVAS
reserve_table = reservations_db.table("reservations")

def reserv_id_autoincrement():
    """Cria automaticamente o ID do cliente. Retorna um número inteiro sequencial."""
    if not reserve_table.all(): 
        return 1
    else: 
        max_id = max(int(reserve["ID"]) for reserve in reserve_table.all())
        return max_id + 1
    
def add_new_reserv(reserv: Reservation):
    """Adiciona uma nova reserva no banco de dados"""
    reserve_table.insert(reserv.to_dict())

def get_all_reserv() -> dict:
    """Pega todos os dados das reservas no banco de dados"""
    return reserve_table.all()

def get_reserv_by_id(id: int) -> dict:
    """Pega uma reserva específica pelo ID"""
    Reserva = Query()
    return reserve_table.get(Reserva.id == int(id))

def update_reserv_data(reserv: Reservation, id: int):
    """Atualiza os dados de uma reserva no banco de dados pelo ID"""
    Reserva = Query()
    if reserve_table.contains(Reserva.id == int(id)):
        reserve_table.update(reserv.to_dict(), Reserva.id == int(id))

def remove_client_by_id(id: int) -> dict:
    """Remove uma reserva do banco de dados pelo ID"""
    Reserva = Query()
    reserve_table.remove(Reserva.id == int(id))


# ====================================
# FUNÇÕES DE GERENCIAMENTO DE RESERVAS
def update_room_status():
    """Atualiza o status dos quartos para 'RESERVADO' se houver reservas confirmadas."""
    quartos_reservados = [] # lista dos números dos quartos reservados
    for reserva in reserve_table.all():
        status = reserva.get("Status")
        quarto = reserva.get("Quarto")
        if status == "CONFIRMADO":
            quartos_reservados.append(quarto) # preenche a lista de números dos quartos reservados
            for numero in quartos_reservados:
                rooms_table.update({"Status do quarto": rm.RoomStatus.RESERVED}, Query().Quarto == numero) # Muda o status do quarto

def get_not_reserv_clients() -> list:
    """Retorna todos os clientes que não fizeram nenhuma reserva (comparando pelo nome)."""
    nomes_com_reserva = set() # lista de clientes com reservas
    for reserva in reserve_table.all():
        titular = reserva.get("Titular")
        nomes_com_reserva.add(titular.strip().upper())
    return [
        cliente for cliente in clients_table.all()
        if cliente.get("nome", "").strip().upper() not in nomes_com_reserva
    ]
