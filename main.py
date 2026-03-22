import flet as ft

def main(page: ft.Page):
    page.title = "Faza Messenger"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212" # Темный фон как в ТГ
    
    # Список для сообщений
    chat = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    
    # Поле для ввода текста
    new_message = ft.TextField(
        hint_text="Написать сообщение...",
        expand=True,
        border_radius=20,
        bgcolor="#1e1e1e"
    )

    def send_click(e):
        if new_message.value:
            # Добавляем сообщение в список
            chat.controls.append(
                ft.Container(
                    content=ft.Text(new_message.value, size=16),
                    bgcolor="#2b5278", # Синий цвет облачка
                    padding=10,
                    border_radius=10,
                    alignment=ft.alignment.center_left
                )
            )
            new_message.value = ""
            page.update()

    # Собираем экран
    page.add(
        ft.Text("Faza Messenger", size=24, weight="bold", color="white"),
        ft.Divider(height=10, color="transparent"),
        chat,
        ft.Row(
            [new_message, ft.FloatingActionButton(icon=ft.icons.SEND, on_click=send_click)],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
