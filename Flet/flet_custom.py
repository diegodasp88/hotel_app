import flet as ft
from datetime import datetime

# Classe para customizar as Tabs (Conjunto de Abas)
class CustomTabs:
    def __init__(self):
        self.default_selected_index = 0
        self.default_animation_duration = 300
        self.default_divider_color = "#04593d"
        self.default_label_color = "#04593d"
        self.default_label_text_style = ft.TextStyle(font_family="font1")
        self.default_indicator_border_side = ft.BorderSide(width=5, color="#04593d")
        self.default_indicator_padding = 5
        self.default_unselected_label_color = "#7b9c8d"
        self.default_expand = True

    def _create_tabs(self, tabs, **personalizacoes):
        return ft.Tabs(
            selected_index=self.default_selected_index,
            animation_duration=self.default_animation_duration,
            divider_color=self.default_divider_color,
            label_color=self.default_label_color,
            label_text_style=self.default_label_text_style,
            indicator_border_side=self.default_indicator_border_side,
            indicator_padding=self.default_indicator_padding,
            unselected_label_color=self.default_unselected_label_color,
            expand=self.default_expand,
            tabs=tabs,
            **personalizacoes
        )

# ===================================== 
# Classe para customizar os Containers das páginas
class CustomContainers:
    def __init__(self):
        self.default_bgcolor = ft.Colors.with_opacity(opacity=0.2, color="#ffffff")
        self.default_padding = ft.Padding(top=10, bottom=10, left=10, right=10)
        self.default_border = ft.border.all(width=2, color="#04593d")
        self.default_border_radius = ft.BorderRadius(top_left=6, top_right=6, bottom_left=6, bottom_right=6)
        self.default_expand = True
        self.default_width = None

    def _create_container(self, content, width=int|None, **personalizacoes):
        return ft.Container(
            bgcolor=self.default_bgcolor,
            padding=self.default_padding,
            border=self.default_border,
            border_radius=self.default_border_radius,
            expand=self.default_expand,
            content=content,
            width=width,
            **personalizacoes
        )

# ===================================== 
# Classe para customizar os Textfields
class CustomTextFields:
    def __init__(self):
        self.default_style = ft.TextStyle(font_family="font2", size=18, weight=ft.FontWeight.BOLD)
        self.default_label_style = ft.TextStyle(font_family="font1", color="#2b7a60")
        self.default_color = "#04593d"
        self.default_bgcolor = ft.Colors.with_opacity(opacity=0.4, color="#ffffff")
        self.default_border_color = "#04593d"
        self.default_border_width = 2

    # Método criar TextField
    def _create_field(self, label, prefix_icon, read_only=False, ref=None, **personalizacoes):
        return ft.TextField(
            label=label,
            ref = ref,
            read_only=read_only,
            label_style=self.default_label_style,
            color=self.default_color,
            border_color=self.default_border_color,
            border_width=self.default_border_width,
            bgcolor=self.default_bgcolor,
            prefix_icon=prefix_icon,
            text_style=self.default_style,
            **personalizacoes
        )

    # Método para criar campo ID do cliente na busca
    def id_client_search(self, on_submit, ref=None):
        return self._create_field(
            label="ID:",
            prefix_icon=ft.Icon(name=ft.Icons.NUMBERS, color="#2b7a60"),
            width=150,
            autofocus=True,
            text_align=ft.TextAlign.RIGHT,
            ref=ref,
            on_submit=on_submit
        )
    
    # Método para criar campo ID do cliente no cadastro
    def id_client_submit(self, ref=None, value=None):
        return self._create_field(
            label="ID:",
            value=value,
            read_only=True,
            prefix_icon=ft.Icon(name=ft.Icons.NUMBERS, color="#2b7a60"),
            width=150,
            text_align=ft.TextAlign.RIGHT,
            ref=ref
        )
    
    # Método para criar campo ID do registro de Reservas
    def id_reserv_submit(self, ref=None, value=None):
        return self._create_field(
            label="ID:",
            value=value,
            read_only=True,
            prefix_icon=ft.Icon(name=ft.Icons.NUMBERS, color="#2b7a60"),
            width=150,
            text_align=ft.TextAlign.RIGHT,
            ref=ref
        )
    
    # Método para criar campo ID na busca de Reservas
    def id_reserv_search(self, on_submit, ref=None):
        return self._create_field(
            label="ID:",
            autofocus=True,
            prefix_icon=ft.Icon(name=ft.Icons.NUMBERS, color="#2b7a60"),
            width=150,
            text_align=ft.TextAlign.RIGHT,
            ref=ref,
            on_submit=on_submit
        )
      
    # Método para criar campo nome do cliente na busca
    def name_client_search(self, ref=None, on_blur=None):
        return self._create_field(
            label="Nome completo:",
            prefix_icon=ft.Icon(name=ft.Icons.PERSON_PIN, color="#2b7a60"),
            expand=True,
            disabled=True,
            ref=ref,
            on_blur=on_blur
        )
    
    # Método para criar campo nome do cliente no cadastro
    def name_client_submit(self, ref=None, on_blur=None):
        return self._create_field(
            label="Nome completo:",
            autofocus=True,
            prefix_icon=ft.Icon(name=ft.Icons.PERSON_PIN, color="#2b7a60"),
            expand=True,
            ref=ref,
            on_blur=on_blur
        )
    
    # Método para criar campo nome do titular na busca de reservas
    def name_reserv_search(self, ref=None, on_blur=None):
        return self._create_field(
            label="Titular:",
            prefix_icon=ft.Icon(name=ft.Icons.PERSON_PIN, color="#2b7a60"),
            expand=True,
            disabled=True,
            ref=ref,
            on_blur=on_blur
        )

    # Método para criar campo telefone do cliente
    def phone_client_field(self, disabled, ref=None, on_blur=None):
        return self._create_field(
            label="Telefone:",
            prefix_icon=ft.Icon(name=ft.Icons.CONTACT_PHONE, color="#2b7a60"),
            width=350,
            adaptive=True,
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text="(##) #####-####",
            disabled=disabled,
            ref=ref,
            on_blur=on_blur
        )

    # Método para criar campo e-mail do cliente
    def email_client_field(self, disabled, ref=None, on_blur=None):
        return self._create_field(
            label="E-mail:",
            prefix_icon=ft.Icon(name=ft.Icons.QUICK_CONTACTS_MAIL, color="#2b7a60"),
            width=500,
            adaptive=True,
            keyboard_type=ft.KeyboardType.EMAIL,
            disabled=disabled,
            ref=ref,
            on_blur=on_blur,
            )
    
    # Método para criar campo check-in/out da reserva
    def checkinout_field(self, label, ref=None):
        return self._create_field(
            label=label,
            width=200,
            read_only=True,
            hint_text="Clique -->",
            prefix_icon=ft.Icon(ft.Icons.CALENDAR_MONTH, color="#2b7a60"),
            ref=ref
        )
    
    # Método para criar campo check-in/out da busca de reservas
    def checkinout_search(self, label, ref=None):
        return self._create_field(
            label=label,
            width=200,
            disabled=True,
            prefix_icon=ft.Icon(ft.Icons.CALENDAR_MONTH, color="#2b7a60"),
            ref=ref
        )
    
    # Método para criar campo quarto na busca de reservas
    def room_reserv_search(self, ref=None):
        return self._create_field(
            label="Quarto:",
            prefix_icon=ft.Icon(name=ft.Icons.DOOR_FRONT_DOOR, color="#2b7a60"),
            width=300,
            disabled=True,
            ref=ref,
        )
    
    # Método para criar campo status na busca de reservas
    def status_reserv_search(self, ref=None):
        return self._create_field(
            label="Status:",
            prefix_icon=None,
            width=500,
            disabled=True,
            ref=ref,
        )


# =====================================
# Classe para customizar os Dropdowns
class CustomDropDowns:
    def __init__(self):
        self.default_style = ft.TextStyle(font_family="font2", size=18, weight=ft.FontWeight.BOLD)
        self.default_label_style = ft.TextStyle(font_family="font1", color="#2b7a60")
        self.default_color = "#04593d"
        self.default_bgcolor = {ft.ControlState.DEFAULT: "#c1f7db"}
        self.default_border_color = "#04593d"
        self.default_border_width = 2
        self.default_expand = True
        self.default_filled = True
        self.default_fill_color = ft.Colors.with_opacity(opacity=0.4, color="#ffffff")
        self.default_trailing_icon = ft.Icon(ft.Icons.ARROW_DROP_DOWN, color="#2b7a60")

    # Método para criar o DropDown
    def _creat_dropdown(self, label, ref, options, prefix_icon, **personalizacoes):
        return ft.Dropdown(
            label=label,
            ref=ref,
            options=options,
            menu_height=120,
            filled=self.default_filled,
            fill_color=self.default_fill_color,
            expand=self.default_expand,
            trailing_icon=self.default_trailing_icon,
            label_style=self.default_label_style,
            color=self.default_color,
            border_color=self.default_border_color,
            border_width=self.default_border_width,
            bgcolor=self.default_bgcolor,
            prefix_icon=prefix_icon,
            text_style=self.default_style,
            **personalizacoes
        )
    
    # Método para criar o DropDown do cliente da reserva
    def dropdown_client_reserv(self, label, ref, prefix_icon, options):
        return self._creat_dropdown(
            width=600,
            label=label,
            ref=ref,
            prefix_icon=prefix_icon,
            options=options,
        )
    
    # Método para criar o DropDown do quarto da reserva
    def dropdown_room_reserv(self, label, ref, prefix_icon, options):
        return self._creat_dropdown(
            width=300,
            label=label,
            ref=ref,
            prefix_icon=prefix_icon,
            options=options,
        )
    
    # Método para criar o DropDown do status da reserva
    def dropdown_status_reserv(self, label, ref, prefix_icon, options):
        return self._creat_dropdown(
            width=300,
            label=label,
            ref=ref,
            prefix_icon=prefix_icon,
            options=options,
        )


# =====================================
# Classe para customizar os FilledButtons
class CustomFilledButtons:
    def __init__(self):
        self.default_icon_color = "#00ffa9"
        self.default_color = "#ffffff"
        self.default_bgcolor = {ft.ControlState.HOVERED: "#24965b",ft.ControlState.DEFAULT: "#2b7a60"}
        self.default_style = ft.ButtonStyle(text_style=ft.TextStyle(font_family="font1", size=14), icon_size=20)
        self.default_height = 50
        self.default_width = 150
    
    # Método criar FilledButton
    def _create_filledbutton(self, text, icon, **personalizacoes):
        return ft.FilledButton(
            text = text,
            icon = icon,
            icon_color = self.default_icon_color,
            color = self.default_color,
            bgcolor = self.default_bgcolor,
            style = self.default_style,
            height = self.default_height,
            width = self.default_width,
            **personalizacoes
        )
    
    # Método para criar o botão cadastrar
    def submit_button(self, on_click=None):
        return self._create_filledbutton(
            text="Cadastrar",
            icon=ft.Icons.LIBRARY_ADD_CHECK,
            on_click=on_click
        )
    
    # Método para criar o botão atualizar
    def update_button(self, on_click=None):
        return self._create_filledbutton(
            text="Atualizar",
            icon=ft.Icons.UPDATE,
            on_click=on_click
        )
    
    # Método para criar o botão excluir
    def remove_button(self, on_click=None):
        return self._create_filledbutton(
            text="Excluir",
            icon=ft.Icons.HIGHLIGHT_REMOVE,
            on_click=on_click
        )
    
    # Método para criar o botão limpar
    def clear_button(self, on_click=None):
        return self._create_filledbutton(
            text="Limpar",
            icon=ft.Icons.CLEAR,
            on_click=on_click
        )

# =====================================
# Classe para customizar os TextButtons
class CustomTextButton:
    def __init__(self):
        self.text_style=ft.TextStyle(font_family="font1", size=18, color="#d2ffba")

    # Método para criar um TextButton
    def _create_textbutton(self, text, **personalizacoes):
        return ft.TextButton(
            text=text,
            style=ft.ButtonStyle(
                bgcolor={
                    ft.ControlState.HOVERED: ft.Colors.with_opacity(opacity=0.4, color="#ffffff"),
                    ft.ControlState.DEFAULT: ft.Colors.with_opacity(opacity=0.4, color="#000000")
                },
                text_style=self.text_style
            ),
            **personalizacoes
        )
    # Método para criar o botão SIM
    def yes_button(self, on_click):
        return self._create_textbutton(
            text="Sim",
            on_click=on_click
        )
    
    # Método para criar o botão NÃO
    def no_button(self, on_click):
        return self._create_textbutton(
            text="Não",
            on_click=on_click
        )
    
    # Método para criar o botão OK
    def ok_button(self, on_click):
        return self._create_textbutton(
            text="OK",
            width=50,
            on_click=on_click
        )
    
    # Método para criar o botão calendário
    def calendar_button(self, on_click):
        return self._create_textbutton(
            icon=ft.Icons.CALENDAR_MONTH,
            text="",
            width=36,
            on_click=on_click
        )
    
# =====================================    
# Classe para customizar os AlertDialogs
class CustomAlertDialog:
    def __init__(self):
        self.default_modal = True
        self.title_text_style = ft.TextStyle(font_family="font1", size=24)
        self.content_text_style = ft.TextStyle(font_family="font2", size=18)
        self.elevation = 50
        self.shadow_color = "#000000"

    # Método para criar AlertDialogs
    def _create_alert(self, title, icon, bgcolor, content, actions, **personalizacoes):
        return ft.AlertDialog(
            modal = self.default_modal,
            bgcolor = bgcolor,
            elevation = self.elevation,
            shadow_color = self.shadow_color,
            title_text_style= self.title_text_style,
            content_text_style= self.content_text_style,
            icon = icon,
            title = title,
            content = content,
            actions = actions,
            **personalizacoes
        )
    
    # Método para criar alerta de cadastro de cliente
    def alert_confirm(self, content, actions):
        return self._create_alert(
            title=ft.Text("Por favor, confirme."),
            icon=ft.Icon(ft.Icons.WARNING, color="#ffd500", size=40),
            bgcolor=ft.Colors.with_opacity(opacity=0.4, color="#f5d142"),
            content=content,
            actions=actions
        )
    
    # Método para criar alerta de erro de cadastro
    def alert_err(self, content, actions):
        return self._create_alert(
            title=ft.Text("Erro!"),
            icon=ft.Icon(ft.Icons.ERROR, color="#871400", size=40),
            bgcolor=ft.Colors.with_opacity(opacity=0.4, color="#f55d42"),
            content=content,
            actions=actions
        )
    
    # Método para criar alerta de cadastro com sucesso
    def alert_success(self, title, actions):
        return self._create_alert(
            title=title,
            icon=ft.Icon(ft.Icons.CHECK_CIRCLE, color="#59ff00", size=40),
            bgcolor=ft.Colors.with_opacity(opacity=0.4, color="#6db354"),
            content=None,
            actions=actions
        )

# ===================================== 
# Classe para customizar DataTables
class CustomDataTable:
    def __init__(self):
        self.expand = True
        self.horizontal_lines = ft.BorderSide(width=1, color="#04593d")
        self.heading_text_style = ft.TextStyle(font_family="font1", size=18)
        self.data_text_style = ft.TextStyle(font_family="font2", size=16)

    # Método para criar DataTable
    def _create_datatable(self, columns, rows, **personalizacoes):
        return ft.DataTable(
            columns=columns,
            rows=rows,
            **personalizacoes
        )

# ===================================== 
# Classe para customizar DatePicker
class CustomDatePicker:
    def __init__(self):
        self.default_first_date = datetime.now()
        self.default_current_date = datetime.now()
        self.default_keyboard_type = ft.KeyboardType.DATETIME
        self.default_date_picker_entry_mode = ft.DatePickerEntryMode.CALENDAR

    # Método para criar DatePicker
    def _create_datepicker(self, on_change):
        return ft.DatePicker(
            first_date=self.default_first_date,
            current_date=self.default_current_date,
            keyboard_type=self.default_keyboard_type,
            date_picker_entry_mode=self.default_date_picker_entry_mode,
            on_change=on_change
        )