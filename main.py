import flet as ft

def main(page: ft.Page):
    page.title = "Faza Messenger"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B141B"  # Глубокий темный цвет
    page.window_width = 400
    page.window_height = 800
    
    # Контейнер для сообщений с прокруткой
    chat = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.ALWAYS,
        spacing=10,
        auto_scroll=True
    )

    # Поле ввода в стиле современного мессенджера
    message_input = ft.TextField(
        hint_text="Сообщение...",
        expand=True,
        border_radius=25,
        bgcolor="#1D2733",
        border_color="transparent",
        content_padding=15,
        on_submit=lambda e: send_message(e)
    )

    def send_message(e):
        if message_input.value:
            # Создаем облачко сообщения
            msg_bubble = ft.Container(
                content=ft.Text(message_input.value, size=16, color="white"),
                bgcolor="#2B5278",
                padding=12,
                border_radius=ft.border_radius.only(
                    top_left=15, top_right=15, bottom_left=15, bottom_right=0
                ),
                alignment=ft.alignment.center_right,
                animate=ft.Animation(600, ft.AnimationCurve.DECELERATE),
            )
            
            chat.controls.append(
                ft.Row([msg_bubble], alignment=ft.MainAxisAlignment.END)
            )
            message_input.value = ""
            page.update()

    # Шапка приложения
    header = ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.BOLT, color="amber", size=30),
            ft.Text("FAZA MESSENGER", size=22, weight="bold", color="white"),
        ]),
        padding=10,
        bgcolor="#1D2733",
        border_radius=10
    )

    # Добавляем элементы на страницу
    page.add(
        header,
        ft.Divider(height=1, color="#24303F"),
        chat,
        ft.Row(
            [
                message_input,
                ft.FloatingActionButton(
                    icon=ft.icons.SEND_ROUNDED,
                    on_click=send_message,
                    bgcolor="#2B5278",
                    mini=True
                )
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
    
