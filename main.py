import flet as ft

def main(page: ft.Page):
    page.title = "FAZA MESSENGER"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B141B"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    chat_box = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    
    def send_click(e):
        if input_field.value:
            chat_box.controls.append(
                ft.Container(
                    content=ft.Text(input_field.value, size=18),
                    bgcolor="#2B5278",
                    padding=15,
                    border_radius=15
                )
            )
            input_field.value = ""
            page.update()

    input_field = ft.TextField(hint_text="Пиши сюда...", expand=True, border_radius=30)
    
    page.add(
        ft.Text("ЭТО ТВОЁ ПРИЛОЖЕНИЕ!", size=30, weight="bold", color="amber"),
        ft.Divider(),
        chat_box,
        ft.Row([input_field, ft.FloatingActionButton(icon=ft.icons.SEND, on_click=send_click)])
    )

ft.app(target=main)
