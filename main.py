import flet as ft

def main(page: ft.Page):
    # Настройки окна
    page.title = "Faza Messenger"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"
    page.padding = 20
    
    # Список для сообщений
    chat_container = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, spacing=10)
    
    # Поле ввода
    message_field = ft.TextField(
        hint_text="Введите сообщение...",
        expand=True,
        border_radius=15,
        bgcolor="#1e1e1e",
        border_color="#333333"
    )

    def on_send_click(e):
        if message_field.value:
            chat_container.controls.append(
                ft.Row([
                    ft.Container(
                        content=ft.Text(message_field.value, color="white", size=16),
                        bgcolor="#2b5278",
                        padding=12,
                        border_radius=ft.border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=0),
                    )
                ], alignment=ft.MainAxisAlignment.END)
            )
            message_field.value = ""
            page.update()

    # Кнопка
    send_button = ft.FloatingActionButton(
        icon=ft.icons.SEND,
        on_click=on_send_click,
        bgcolor="#2b5278"
    )

    # Добавляем всё на страницу
    page.add(
        ft.Text("Faza Messenger", size=28, weight="bold"),
        ft.Divider(color="#333333"),
        chat_container,
        ft.Row([message_field, send_button], spacing=10)
    )

ft.app(target=main)
