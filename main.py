import flet as ft

def main(page: ft.Page):
    page.title = "Faza Messenger"
    page.theme_mode = ft.ThemeMode.DARK
    
    chat = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    new_message = ft.TextField(hint_text="Напишите сообщение...", expand=True)

    def send_click(e):
        if new_message.value:
            chat.controls.append(ft.Text(f"Вы: {new_message.value}"))
            new_message.value = ""
            page.update()

    page.add(
        ft.Text("Faza Messenger Online", size=20, weight="bold"),
        chat,
        ft.Row([new_message, ft.IconButton(icon=ft.icons.SEND, on_click=send_click)])
    )

ft.app(target=main)
