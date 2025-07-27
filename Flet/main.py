import flet as ft
import db
import flet_custom as fc
from repository.person import Client
from repository.reservation import Reservation

# <Início da Página>
def main(page: ft.Page):

    # Caracterísiticas da página principal
    page.title = "HotelManage App"
    page.bgcolor = "#439c7e"
    page.window.maximized = True
    page.window.min_height = 900
    page.window.min_width = 1024
    page.fonts = {
        "font1": "storage/assets/fonts/Goodtiming.otf",
        "font2": "storage/assets/fonts/Zekton.otf"
    }
   
    # Barra do software
    appbar = page.appbar = ft.AppBar(
        bgcolor="#04593d",
        center_title=True,
        leading=ft.Icon(
            name=ft.Icons.HOTEL,
            color=ft.Colors.WHITE,
            size=40
        ),
        title=ft.Text(
            value="Hotel Refúgio dos Sonhos",
            color=ft.Colors.WHITE,
            font_family="font1"
        )
    )

    # Estanciando as Classes do FletCustom
    textfields = fc.CustomTextFields()
    filled_buttons = fc.CustomFilledButtons()
    text_buttons = fc.CustomTextButton()
    alert_dialogs = fc.CustomAlertDialog()
    data_tables = fc.CustomDataTable()
    containers = fc.CustomContainers()
    tabs = fc.CustomTabs()
    dropdowns = fc.CustomDropDowns()
    datepicker = fc.CustomDatePicker()

    def show_all_rooms():
        """Criar tabela com dados de todos os quartos"""
        all_rooms: list = db.get_all_rooms() # Lista de todos os quartos
        columns = [ft.DataColumn(ft.Text(str(chave).capitalize(), color="#04593d", font_family="font1", size=18)) for chave in all_rooms[0]]
        rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(item.get(chave, "")), color="#000000", font_family="font2", size=16)) for chave in all_rooms[0]]) for item in all_rooms]
        return data_tables._create_datatable(columns=columns, rows=rows)
    
    def render_rooms_table():
        """Atualizar tabela de quartos"""
        if rooms_table_ref.current:
            rooms_table_ref.current.controls.clear()
            rooms_table_ref.current.controls.append(show_all_rooms())
            rooms_table_ref.current.update()

    def to_lowercase(e):
        """Torna todas as letras minúsculas"""
        e.control.value = e.control.value.lower()
        e.control.update()

    def to_uppercase(e):
        """Torna todas as letras maiúsculas"""
        e.control.value = e.control.value.upper()
        e.control.update()

    def format_phone_number(e):
        """Máscara para preenchimento do telefone"""
        raw = "".join(filter(str.isdigit, e.control.value)) # Remove tudo que não for número
        formatted = ""
        # DDD
        if len(raw) >= 2:
            formatted += f"({raw[:2]})"
        elif len(raw) > 0:
            formatted += f"({raw})"
        # Número de telefone
        if len(raw) > 2:
            phone = raw[2:]
            if len(phone) >= 9:
                formatted += f" {phone[:5]}-{phone[5:9]}"
            elif len(phone) >= 8:
                formatted += f" {phone[:4]}-{phone[4:]}"
            elif len(phone) > 0:
                formatted += f" {phone}"
        e.control.value = formatted
        e.control.update()

    # Variáveis dos refs dos TextFields
        # Cadastro de Clientes
    id_number_submit_ref = ft.Ref[ft.TextField]()
    name_submit_ref = ft.Ref[ft.TextField]()
    phone_submit_ref = ft.Ref[ft.TextField]()
    email_submit_ref = ft.Ref[ft.TextField]()
        # Busca de Clientes
    id_number_ref = ft.Ref[ft.TextField]()
    name_ref = ft.Ref[ft.TextField]()
    phone_ref = ft.Ref[ft.TextField]()
    email_ref = ft.Ref[ft.TextField]()
        # Registro de reservas
    id_reserv_submit_ref = ft.Ref[ft.TextField]()
    client_reserv_ref = ft.Ref[ft.Dropdown]()
    rooms_reserv_ref = ft.Ref[ft.Dropdown]()
    checkin_ref = ft.Ref[ft.TextField]()
    checkout_ref = ft.Ref[ft.TextField]()
    status_reserv_ref = ft.Ref[ft.Dropdown]()
        # Busca de reservas
    id_reserv_search_ref = ft.Ref[ft.TextField]()
    name_reserv_search_ref = ft.Ref[ft.TextField]()
    room_reserv_search_ref = ft.Ref[ft.TextField]()
    checkin_reserv_search_ref = ft.Ref[ft.TextField]()
    checkout_reserv_search_ref = ft.Ref[ft.TextField]()
    status_reserv_search_ref = ft.Ref[ft.TextField]()
        # Tabelas
    clients_table_ref = ft.Ref[ft.Row]()
    rooms_table_ref = ft.Ref[ft.Row]()
    reserv_table_ref = ft.Ref[ft.Row]()
    
    # Variáveis de cadastro de clientes
    id_number_submit = textfields.id_client_submit(ref=id_number_submit_ref, value=db.client_id_autoincrement())
    full_name_submit = textfields.name_client_submit(ref=name_submit_ref, on_blur=to_uppercase)
    phone_number_submit = textfields.phone_client_field(ref=phone_submit_ref, on_blur=format_phone_number, disabled=False)
    email_submit = textfields.email_client_field(ref=email_submit_ref, on_blur=to_lowercase, disabled=False)

    # Variáveis de busca de clientes
    id_number = textfields.id_client_search(ref=id_number_ref, on_submit=lambda e: get_client_data_by_id(e))
    full_name = textfields.name_client_search(ref=name_ref, on_blur=to_uppercase)
    phone_number = textfields.phone_client_field(ref=phone_ref, on_blur=format_phone_number, disabled=True)
    email = textfields.email_client_field(ref=email_ref, on_blur=to_lowercase, disabled= True)

    def clear_submit_form(e):
        """Limpa os campos do formulário de cadastro."""
        # Limpar os campos
        name_submit_ref.current.value = ""
        phone_submit_ref.current.value = ""
        email_submit_ref.current.value = ""
        # Colocar o cursor no campo Nome
        name_submit_ref.current.focus()
        # Atualizar todos os campos
        id_number_submit_ref.current.update()
        name_submit_ref.current.update()
        phone_submit_ref.current.update()
        email_submit_ref.current.update()

    def clear_search_form(e):
        """Limpa os campos do formulário de busca."""
        # Limpar os campos
        id_number_ref.current.value = ""
        name_ref.current.value = ""
        phone_ref.current.value = ""
        email_ref.current.value = ""
        # Colocar o cursor no campo ID
        id_number_ref.current.focus()
        # Desativar os campos
        name_ref.current.disabled=True
        phone_ref.current.disabled=True
        email_ref.current.disabled=True
        # Atualizar todos os campos
        id_number_ref.current.update()
        name_ref.current.update()
        phone_ref.current.update()
        email_ref.current.update()

    def get_clients_ids_names():
        """Cria a lista de opções da seleção de clientes para reserva de quartos."""
        all_clients: list = db.get_not_reserv_clients() # Lista de todos os clientes
        return [ft.DropdownOption(key=str(cliente["nome"]), 
                                  text=cliente["nome"], 
                                  style=ft.ButtonStyle(color="#04593d", text_style=ft.TextStyle(font_family="font2", weight=ft.FontWeight.BOLD))) 
                for cliente in all_clients]

    def render_clients_dropdown():
        """Atualiza a lista de opções da seleção de clientes."""
        client_reserv_ref.current.options = get_clients_ids_names()
        client_reserv_ref.current.value = ""
        client_reserv_ref.current.update()

    def get_rooms_list():
        """Cria a lista de opções da seleção de quartos para reserva."""
        all_rooms: list = db.listar_quartos_disponiveis() # Lista de todos os quartos
        return [ft.DropdownOption(key=str(room["Quarto"]),
                                  text=str(room["Quarto"]) + ": " + room["Tipo do quarto"], 
                                  style=ft.ButtonStyle(color="#04593d", text_style=ft.TextStyle(font_family="font2", weight=ft.FontWeight.BOLD))) 
                for room in all_rooms]

    def render_rooms_dropdown():
        """Atualiza a lista de opções da seleção de quartos."""
        rooms_reserv_ref.current.options = get_rooms_list()
        rooms_reserv_ref.current.value = ""
        rooms_reserv_ref.current.update() 

    def clear_reserv_form(e):
        """Limpa os campos do formulário de cadastro de reservas."""
        # Limpar os campos
        render_clients_dropdown()
        render_rooms_dropdown()
        checkin_ref.current.value = ""
        checkout_ref.current.value = ""
        status_reserv_ref.current.value = ""
        # Atualizar todos os campos
        id_reserv_submit_ref.current.update()
        client_reserv_ref.current.update()
        rooms_reserv_ref.current.update()
        checkin_ref.current.update()
        checkout_ref.current.update()
        status_reserv_ref.current.update()

    def clear_search_reserv(e):
        """Limpa os campos do formulário de busca de reservas."""
        # Limpar os campos
        id_reserv_search_ref.current.value = ""
        name_reserv_search_ref.current.value = ""
        room_reserv_search_ref.current.value = ""
        checkin_reserv_search_ref.current.value = ""
        checkout_reserv_search_ref.current.value = ""
        status_reserv_search_ref.current.value = ""
        # Atualizar campos
        id_reserv_search_ref.current.update()
        name_reserv_search_ref.current.update()
        room_reserv_search_ref.current.update()
        checkin_reserv_search_ref.current.update()
        checkout_reserv_search_ref.current.update()
        status_reserv_search_ref.current.update()

    
    def show_all_reserv_data(e):
        """Criar tabela com dados de todas as reservas"""
        all_reserv: list = db.get_all_reserv() # Lista de todas as reservas
        if not all_reserv:
            return ft.Text("⚠️ Nenhuma reserva cadastrada.", font_family="font1", size=18, color="#000000")
        columns = [ft.DataColumn(ft.Text(str(chave).capitalize(), color="#04593d", font_family="font1", size=18)) for chave in all_reserv[0]]
        rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(item.get(chave, "")), color="#000000", font_family="font2", size=16)) for chave in all_reserv[0]]) for item in all_reserv]
        return data_tables._create_datatable(columns=columns, rows=rows)
    
    def render_reserv_table():
        """Atualizar tabela de reservas"""
        if reserv_table_ref.current:
            reserv_table_ref.current.controls.clear()
            reserv_table_ref.current.controls.append(show_all_reserv_data(None))
            reserv_table_ref.current.update()

    def get_client_data_by_id(e):
        """Coleta os dados do cliente pelo ID do banco de dados e preenche o formulário."""
        id = id_number_ref.current.value
        try:
            if id_number_ref.current.value:
                client = db.get_client_by_id(id)
                # Preencher os campos
                name_ref.current.value = client["nome"]
                phone_ref.current.value = client["telefone"]
                email_ref.current.value = client["email"]
                # Ativar os campos e botões
                name_ref.current.disabled=False
                phone_ref.current.disabled=False
                email_ref.current.disabled=False
                # Atualizar os campos
                name_ref.current.update()
                phone_ref.current.update()
                email_ref.current.update()
            else:
                page.open(err_search)
        except TypeError:
            page.open(err_id)
            id_number_ref.current.focus()

    def show_all_clients_data(e):
        """Criar tabela com dados de todos os clientes"""
        all_clients: list = db.get_all_clients() # Lista de todos os clientes
        if not all_clients:
            return ft.Text("⚠️ Nenhum cliente cadastrado.", font_family="font1", size=18, color="#000000")
        columns = [ft.DataColumn(ft.Text(str(chave).capitalize(), color="#04593d", font_family="font1", size=18)) for chave in all_clients[0]]
        rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(item.get(chave, "")), color="#000000", font_family="font2", size=16)) for chave in all_clients[0]]) for item in all_clients]
        return data_tables._create_datatable(columns=columns, rows=rows)
    
    def render_client_table():
        """Atualizar tabela de clientes"""
        if clients_table_ref.current:
            clients_table_ref.current.controls.clear()
            clients_table_ref.current.controls.append(show_all_clients_data())
            clients_table_ref.current.update()
       
    def update_client(e):
        """Atualiza os dados do cliente no banco de dados pelo ID."""
        upd_client = Client(
            id=id_number_ref.current.value,
            nome=name_ref.current.value.strip(),
            telefone=phone_ref.current.value.strip(),
            email=email_ref.current.value.strip()
        )
        if id_number_ref.current.value:
            id = id_number_ref.current.value
            page.close(confirm_update)
            db.update_client_data(upd_client, id=id)
            page.open(success_update)
            render_client_table() # atualizar tabela de clientes
            clear_search_form(e) # limpar formulário de busca
            render_clients_dropdown() # atualizar o dropdown de clientes na reserva
            id_number_ref.current.focus() # colocar o cursor no campo ID
        else:
            page.open(err_id)

    def remove_client_data_by_id(e):
        """Remove os dados do cliente no banco de dados pelo ID."""
        if id_number_ref.current.value:
            id = id_number_ref.current.value
            page.close(confirm_removal)
            db.remove_client_by_id(id=id)
            page.open(success_removal)
            clear_search_form(e) # limpar formulário de busca
            render_client_table() # atualizar tabela de clientes
            render_clients_dropdown() # atualizar o dropdown de clientes na reserva
            id_number_ref.current.focus() # colocar o cursor no campo ID
        else:
            page.open(err_id)

    def submit_form(e):
        """Coleta os dados do cadastro clientes e adiciona ao banco de dados."""
        if name_submit_ref.current.value and phone_submit_ref.current.value and email_submit_ref.current.value:
            new_client = Client(
                id=id_number_submit_ref.current.value,
                nome=name_submit_ref.current.value.strip(),
                telefone=phone_submit_ref.current.value.strip(),
                email=email_submit_ref.current.value.strip()
            )        
            page.close(confirm_submit) # fecha o pop-up de confirmar cadastro
            db.add_new_client(new_client) # adiciona o objeto Client ao banco de dados
            page.open(success_submit) # abre o pop-up de sucesso
            id_number_submit_ref.current.value = str(db.client_id_autoincrement())
            id_number_submit_ref.current.update() # atualizar o número do id
            clients_table_ref.current.update() # atualizar a tabela de clientes
            render_clients_dropdown() # atualizar o dropdown de clientes na reserva
            clear_submit_form(e) # limpar formulário para novo cadastro
            render_client_table() # atualizar tabela de clientes
        else:
            page.open(err_submit)

    def submit_reserv(e):
        """Coleta os dados da reserva e adiciona ao banco de dados."""
        if client_reserv_ref and rooms_reserv_ref and checkin_ref and checkout_ref and status_reserv_ref:
            new_reserv = Reservation(
                reserv_id=id_reserv_submit_ref.current.value,
                reserv_owner=client_reserv_ref.current.value,
                reserv_room=int(rooms_reserv_ref.current.value),
                check_in=checkin_ref.current.value,
                check_out=checkout_ref.current.value,
                reserv_status=status_reserv_ref.current.value
            )
            page.close(confirm_reserv)
            db.add_new_reserv(new_reserv)
            page.open(success_reserv)
            id_reserv_submit_ref.current.value = str(db.reserv_id_autoincrement())
            render_reserv_table() # atualizar tabela de reservas
            db.update_room_status() # atualizar status do quarto após reserva
            get_rooms_list() # cria uma nova lista com os quartos disponíveis
            id_reserv_submit_ref.current.update()
            reserv_table_ref.current.update()
            clear_reserv_form(e) # limpar formulário de reservas
            render_rooms_table() # atualizar tabela de quartos
        else:
            page.open(err_submit)

    def update_reserv(e):
        """Atualiza os dados de uma reserva no banco de dados pelo ID."""
        upd_reserv = Reservation(
                reserv_id=id_reserv_submit_ref.current.value,
                reserv_owner=client_reserv_ref.current.value,
                reserv_room=int(rooms_reserv_ref.current.value),
                check_in=checkin_ref.current.value,
                check_out=checkout_ref.current.value,
                reserv_status=status_reserv_ref.current.value
            )
        if id_number_ref.current.value:
            id = id_number_ref.current.value
            page.close(confirm_reserv_update)
            db.update_reserv_data(upd_reserv, id=id)
            page.open(success_update)
            render_reserv_table() # atualizar tabela de reservas
            clear_search_reserv(e) # limpar formulário de busca de reservas
            render_reserv_table() # atualizar tabela de reservas
            db.update_room_status() # atualizar status do quarto após reserva
            get_rooms_list() # cria uma nova lista com os quartos disponíveis
            id_reserv_submit_ref.current.update()
            reserv_table_ref.current.update()
            render_clients_dropdown() # atualizar o dropdown de clientes na reserva
            id_reserv_search_ref.current.focus() # colocar o cursor no campo ID
        else:
            page.open(err_id)

    # Variáveis dos FilledButtons
    cadastrar_cliente = filled_buttons.submit_button(on_click=lambda e: page.open(confirm_submit))
    atualizar_cliente = filled_buttons.update_button(on_click=lambda e: page.open(confirm_update))
    remover_cliente = filled_buttons.remove_button(on_click=lambda e: page.open(confirm_removal))
    limpar_cadastro = filled_buttons.clear_button(on_click=clear_submit_form)
    limpar_busca = filled_buttons.clear_button(on_click=clear_search_form)
    cadastrar_reserva = filled_buttons.submit_button(on_click=lambda e: page.open(confirm_reserv))
    atualizar_reserva = filled_buttons.update_button(on_click=lambda e: page.open(confirm_update))
    remover_reserva = filled_buttons.remove_button(on_click=lambda e: page.open(confirm_removal))
    
    # Variáveis dos AlertDialogs
    err_id = alert_dialogs.alert_err(
        content=ft.Text("ID do cliente inexistente."),
        actions=[text_buttons.ok_button(on_click=lambda e: page.close(err_id))])

    err_search = alert_dialogs.alert_err(
        content=ft.Text("Preencha o campo ID do cliente."),
        actions=[text_buttons.ok_button(on_click=lambda e: page.close(err_search))])
    
    err_submit = alert_dialogs.alert_err(
        content=ft.Text("Todos os campos devem ser preenchidos."),
        actions=[text_buttons.ok_button(on_click=lambda e: page.close(err_submit))])
    
    confirm_submit = alert_dialogs.alert_confirm(
        content=ft.Text("Você realmente deseja cadastrar esse cliente?"),
        actions=[
            text_buttons.yes_button(on_click=submit_form),
            text_buttons.no_button(on_click=lambda e: page.close(confirm_submit))
    ])

    confirm_update = alert_dialogs.alert_confirm(
        content=ft.Text("Você realmente deseja atualizar esses dados?"),
        actions=[
            text_buttons.yes_button(on_click=update_client),
            text_buttons.no_button(on_click=lambda e: page.close(confirm_update))
    ])

    confirm_removal = alert_dialogs.alert_confirm(
        content=ft.Text("Você realmente deseja excluir os dados desse cliente?"),
        actions=[
            text_buttons.yes_button(on_click=remove_client_data_by_id),
            text_buttons.no_button(on_click=lambda e: page.close(confirm_removal))
    ])

    confirm_reserv = alert_dialogs.alert_confirm(
        content=ft.Text("Você realmente deseja efetuar essa reserva?"),
        actions=[
            text_buttons.yes_button(on_click=submit_reserv),
            text_buttons.no_button(on_click=lambda e: page.close(confirm_reserv))
    ])

    confirm_reserv_update = alert_dialogs.alert_confirm(
        content=ft.Text("Atualizar os dados dessa reserva?"),
        actions=[
            text_buttons.yes_button(on_click=update_reserv),
            text_buttons.no_button(on_click=lambda e: page.close(confirm_reserv_update))
    ])
    
    success_submit = alert_dialogs.alert_success(
        title=ft.Text("Cliente cadastrado com sucesso!"),
        actions=[text_buttons.ok_button(on_click=lambda e: page.close(success_submit))]
        )
    
    success_update = alert_dialogs.alert_success(
        title=ft.Text("Atualização bem sucedida!"),
        actions=[text_buttons.ok_button(on_click=lambda e: page.close(success_update))]
        )
    
    success_removal = alert_dialogs.alert_success(
        title=ft.Text("Exclusão bem sucedida!"),
        actions=[text_buttons.ok_button(on_click=lambda e: page.close(success_removal))]
        )
    
    success_reserv = alert_dialogs.alert_success(
        title=ft.Text("Reserva feita com sucesso!"),
        actions=[text_buttons.ok_button(on_click=lambda e: page.close(success_reserv))]
        )
    
    # Variáveis de registro de reservas
    id_reserv = textfields.id_reserv_submit(ref=id_reserv_submit_ref, value=db.reserv_id_autoincrement())
    client_reserv = dropdowns.dropdown_client_reserv(label="Cliente",
                                              prefix_icon=ft.Icon(name=ft.Icons.PERSON, color="#04593d"), 
                                              ref=client_reserv_ref,
                                              options=get_clients_ids_names())
    rooms_reserv = dropdowns.dropdown_room_reserv(label="Quarto",
                                              prefix_icon=ft.Icon(name=ft.Icons.DOOR_FRONT_DOOR, color="#04593d"), 
                                              ref=rooms_reserv_ref,
                                              options=get_rooms_list())
    checkin = textfields.checkinout_field(label="Check-in", ref=checkin_ref)
    checkout = textfields.checkinout_field(label="Check-out", ref=checkout_ref)
    calendar_in = text_buttons.calendar_button(on_click=lambda e: page.open(datepicker._create_datepicker(datein_onchange)))
    calendar_out = text_buttons.calendar_button(on_click=lambda e: page.open(datepicker._create_datepicker(dateout_onchange)))
    status_reserv = dropdowns.dropdown_status_reserv(label="Status da Reserva",
                                              prefix_icon=None,
                                              ref=status_reserv_ref,
                                              options=[
                                                  ft.DropdownOption(key="CONFIRMADO", 
                                                                    text="✅Confirmado", 
                                                                    style=ft.ButtonStyle(color="#04593d", text_style=ft.TextStyle(font_family="font2", weight=ft.FontWeight.BOLD))),
                                                  ft.DropdownOption(key="CANCELADO", 
                                                                    text="⛔Cancelado", 
                                                                    style=ft.ButtonStyle(color="#04593d", text_style=ft.TextStyle(font_family="font2", weight=ft.FontWeight.BOLD))),
                                                  ft.DropdownOption(key="PENDENTE", 
                                                                    text="⚠️Pendente", 
                                                                    style=ft.ButtonStyle(color="#04593d", text_style=ft.TextStyle(font_family="font2", weight=ft.FontWeight.BOLD)))
                                              ])
    
    #Variáveis da busca de reservas
    id_reserv_search = textfields.id_reserv_search(ref=id_reserv_search_ref, on_submit=lambda e: db.get_reserv_by_id(e))
    name_reserv_search = textfields.name_reserv_search(ref=name_reserv_search_ref, on_blur=to_uppercase)
    room_reserv_search = textfields.room_reserv_search(ref=room_reserv_search_ref)
    checkin_reserv_search = textfields.checkinout_search(label="Check-in", ref=checkin_reserv_search_ref)
    checkout_reserv_search = textfields.checkinout_search(label="Check-out", ref=checkout_reserv_search_ref)
    status_reserv_search = textfields.status_reserv_search(ref=status_reserv_search_ref)

    # Ações dos calendários (check-in e check-out)
    def datein_onchange(e):
        checkin_ref.current.value = e.control.value.strftime("%d/%m/%Y")
        checkin_ref.current.update()

    def dateout_onchange(e):
        checkout_ref.current.value = e.control.value.strftime("%d/%m/%Y")
        checkout_ref.current.update()

# <BODY> ===============================

    _body = ft.Container(
        bgcolor="#c1f7db",
        expand=True,
        padding=20,
        border_radius=8,
        shadow=ft.BoxShadow(
            blur_radius=5,
            color=ft.Colors.with_opacity(
                opacity=0.6,
                color=ft.Colors.BLACK
            )
        ),
        content=tabs._create_tabs(
            tabs=[
#************** QUARTOS                
                ft.Tab(
                    text="QUARTOS", 
                    icon=ft.Icons.DOOR_FRONT_DOOR, 
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Image(
                                    src="storage/images/hotel.png",
                                    fit=ft.ImageFit.FILL
                                )
                            ),
                            containers._create_container(
                                content=ft.Column(
                                    expand=True,
                                    controls=[
                                        ft.Row([
                                            ft.Icon(name=ft.Icons.DOOR_FRONT_DOOR, size=30, color="#2b7a60"),
                                            ft.Text(value="Tabela de Quartos", size=24, color="#2b7a60", font_family="font1")
                                        ]),
                                        ft.Row(ref=rooms_table_ref, controls=[show_all_rooms()])
                                    ]
                                )
                            )
                        ]
                    )
                ),
#************** CLIENTES               
                ft.Tab(
                    text="CLIENTES", 
                    icon=ft.Icons.PEOPLE_ALT, 
                    content=containers._create_container(
                        content=ft.Column(
                            controls=[
                                ft.Row(height=450, controls=[
                                    ft.Tabs(
                                        selected_index=0,
                                        animation_duration=300,
                                        divider_color="#04593d",
                                        label_color="#04593d",
                                        label_text_style=ft.TextStyle(font_family="font1"),
                                        indicator_border_side=ft.BorderSide(width=5, color="#04593d"),
                                        indicator_padding=5,
                                        unselected_label_color="#7b9c8d",
                                        expand=1,
                                        tabs=[
                                            ft.Tab(
                                                text="Cadastrar Clientes",
                                                icon=ft.Icon(ft.Icons.PERSON_ADD),
                                                content=ft.Container(
                                                    bgcolor=ft.Colors.with_opacity(opacity=0.2, color="#ffffff"),
                                                    padding=ft.Padding(top=10, bottom=10, left=10, right=10),
                                                    border=ft.border.all(width=2, color="#04593d"),
                                                    border_radius=ft.BorderRadius(top_left=6, top_right=6, bottom_left=6, bottom_right=6),
                                                    expand=True,
                                                    content=ft.Column(
                                                        controls=[
                                                            # Cadastro do Cliente
                                                            ft.Row([
                                                                ft.Icon(name=ft.Icons.PERSON_ADD, size=30, color="#2b7a60"),
                                                                ft.Text(value="Cadastrar Cliente", size=24, color="#2b7a60", font_family="font1")
                                                            ]),
                                                            ft.Row([id_number_submit]), # Campo ID do cliente
                                                            ft.Row([full_name_submit]), # Campo nome do cliente
                                                            ft.Row([phone_number_submit]), # Campo fone do cliente
                                                            ft.Row([email_submit]), # Campo e-mail do cliente
                                                            ft.Row([cadastrar_cliente, limpar_cadastro]) # Botões
                                                        ]
                                                    )
                                                )
                                            ),
                                            ft.Tab(
                                                text="Buscar Clientes",
                                                icon=ft.Icon(ft.Icons.PERSON_SEARCH),
                                                content=ft.Container(
                                                    bgcolor=ft.Colors.with_opacity(opacity=0.2, color="#ffffff"),
                                                    padding=ft.Padding(top=10, bottom=10, left=10, right=10),
                                                    border=ft.border.all(width=2, color="#04593d"),
                                                    border_radius=ft.BorderRadius(top_left=6, top_right=6, bottom_left=6, bottom_right=6),
                                                    expand=True,
                                                    content=ft.Column(
                                                        controls=[
                                                            # Busca do Cliente
                                                            ft.Row([
                                                                ft.Icon(name=ft.Icons.PERSON_SEARCH, size=30, color="#2b7a60"),
                                                                ft.Text(value="Buscar Cliente", size=24, color="#2b7a60", font_family="font1")
                                                            ]),
                                                            ft.Row([id_number, # Campo ID de busca do cliente
                                                                    ft.IconButton( # Botão Busca
                                                                        bgcolor="#083b21",
                                                                        icon=ft.Icons.SEARCH,
                                                                        tooltip="Buscar",
                                                                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: "#24965b", ft.ControlState.DEFAULT: "#083b21"}),
                                                                        on_click=get_client_data_by_id
                                                                    )]),   
                                                            ft.Row([full_name]), # Campo nome do cliente
                                                            ft.Row([phone_number]), # Campo fone do cliente
                                                            ft.Row([email]), # Campo e-mail do cliente
                                                            ft.Row([limpar_busca, atualizar_cliente, remover_cliente]) # Botões
                                                        ]
                                                    )
                                                )
                                            )
                                        ]
                                    )
                                ]),
                                ft.Divider(height=2, color="#04593d"),
                                ft.Row(expand=True, controls=[
                                    ft.Container(
                                        padding=10,
                                        expand=True,
                                        margin=ft.Margin(left=2, right=2, bottom=2, top=2),
                                        bgcolor=ft.Colors.with_opacity(opacity=0.2, color="#ffffff"),
                                        border=ft.border.all(width=2, color="#04593d"),
                                        border_radius=ft.BorderRadius(top_left=8, top_right=8, bottom_left=8, bottom_right=8),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(controls=[
                                                    ft.Icon(name=ft.Icons.FORMAT_LIST_NUMBERED, size=30, color="#2b7a60"),
                                                    ft.Text(value="Listagem de Clientes", size=24, color="#2b7a60", font_family="font1")
                                                ]),
                                                ft.Row(ref=clients_table_ref, controls=[show_all_clients_data(None)])
                                            ], 
                                            scroll=ft.ScrollMode.ADAPTIVE
                                        )
                                    )
                                ]),
                            ]
                        )
                    )
                ),
#************** RESERVAS             
                ft.Tab(
                    text="RESERVAS", 
                    icon=ft.Icons.PASTE, 
                    content=containers._create_container(
                        content=ft.Column(
                            controls=[
                                ft.Row(height=450, controls=[
                                    ft.Tabs(
                                        selected_index=0,
                                        animation_duration=300,
                                        divider_color="#04593d",
                                        label_color="#04593d",
                                        label_text_style=ft.TextStyle(font_family="font1"),
                                        indicator_border_side=ft.BorderSide(width=5, color="#04593d"),
                                        indicator_padding=5,
                                        unselected_label_color="#7b9c8d",
                                        expand=1,
                                        tabs=[
                                            ft.Tab(
                                                text="Registrar Reservas",
                                                icon=ft.Icon(ft.Icons.CONTENT_PASTE_GO),
                                                content=ft.Container(
                                                    bgcolor=ft.Colors.with_opacity(opacity=0.2, color="#ffffff"),
                                                    padding=ft.Padding(top=10, bottom=10, left=10, right=10),
                                                    border=ft.border.all(width=2, color="#04593d"),
                                                    border_radius=ft.BorderRadius(top_left=6, top_right=6, bottom_left=6, bottom_right=6),
                                                    expand=True,
                                                    content=ft.Column(
                                                        controls=[
                                                            # Registrar Reserva
                                                            ft.Row([
                                                                ft.Icon(name=ft.Icons.CONTENT_PASTE_GO, size=30, color="#2b7a60"),
                                                                ft.Text(value="Registrar Reserva", size=24, color="#2b7a60", font_family="font1")
                                                            ]),
                                                            ft.Row([id_reserv]), # Campo ID da reserva
                                                            ft.Row([client_reserv]), # Campo seleção do cliente
                                                            ft.Row([rooms_reserv]), # Campo seleção do cliente
                                                            ft.Row([checkin, calendar_in, ft.Container(width=60), checkout, calendar_out]), # campos check-in e check-out
                                                            ft.Row([status_reserv, ft.Container(width=60), cadastrar_reserva]) # campo status e botão cadastrar reserva
                                                        ]
                                                    )
                                                )
                                            ),
                                            ft.Tab(
                                                text="Buscar Reservas",
                                                icon=ft.Icon(ft.Icons.CONTENT_PASTE_SEARCH),
                                                content=ft.Container(
                                                    bgcolor=ft.Colors.with_opacity(opacity=0.2, color="#ffffff"),
                                                    padding=ft.Padding(top=10, bottom=10, left=10, right=10),
                                                    border=ft.border.all(width=2, color="#04593d"),
                                                    border_radius=ft.BorderRadius(top_left=6, top_right=6, bottom_left=6, bottom_right=6),
                                                    expand=True,
                                                    content=ft.Column(
                                                        controls=[
                                                            # Busca da reserva
                                                            ft.Row([
                                                                ft.Icon(name=ft.Icons.CONTENT_PASTE_SEARCH, size=30, color="#2b7a60"),
                                                                ft.Text(value="Buscar Reserva", size=24, color="#2b7a60", font_family="font1"),
                                                            ]),
                                                            ft.Row([id_reserv_search,
                                                                    ft.IconButton( # Botão Busca
                                                                        bgcolor="#083b21",
                                                                        icon=ft.Icons.SEARCH,
                                                                        tooltip="Buscar",
                                                                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: "#24965b", ft.ControlState.DEFAULT: "#083b21"}),
                                                                        on_click=get_client_data_by_id
                                                                    )
                                                            ]),
                                                            ft.Row([name_reserv_search]),
                                                            ft.Row([room_reserv_search]),
                                                            ft.Row([checkin_reserv_search, ft.Container(width=30), checkout_reserv_search]),
                                                            ft.Row([status_reserv_search, ft.Container(width=30), atualizar_reserva, remover_reserva])
                                                        ]
                                                    )
                                                )
                                            )
                                        ]
                                    )
                                ]),
                                ft.Divider(height=2, color="#04593d"),
                                ft.Row(expand=True, controls=[
                                    ft.Container(
                                        padding=10,
                                        expand=True,
                                        margin=ft.Margin(left=2, right=2, bottom=2, top=2),
                                        bgcolor=ft.Colors.with_opacity(opacity=0.2, color="#ffffff"),
                                        border=ft.border.all(width=2, color="#04593d"),
                                        border_radius=ft.BorderRadius(top_left=8, top_right=8, bottom_left=8, bottom_right=8),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(controls=[
                                                    ft.Icon(name=ft.Icons.FORMAT_LIST_NUMBERED, size=30, color="#2b7a60"),
                                                    ft.Text(value="Listagem de Reservas", size=24, color="#2b7a60", font_family="font1")
                                                ]),
                                                ft.Row(ref=reserv_table_ref, controls=[show_all_reserv_data(None)])
                                            ], 
                                            scroll=ft.ScrollMode.ADAPTIVE
                                        )
                                    )
                                ]),
                            ]
                        )
                    )
                )
            ]
        )
    )

    # CONTAINER PRINCIPAL DO BODY
    _stack_main = ft.Stack(
        expand=True,
        controls=[
            _body
        ]
    )

# </BODY> ==============================

    page.add(appbar, _stack_main)
    page.update()

ft.app(target=main)