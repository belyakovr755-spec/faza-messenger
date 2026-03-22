import flet as ft
import socket
import threading

def main(page: ft.Page):
    page.title = "FAZA MESSENGER"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B141B"

    # ТВОЙ АДРЕС ИЗ IFCONFIG
    SERVER_IP = "192.168.1.154" 
    PORT = 8888

    chat_display = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, spacing=10)
    
    # Пытаемся создать соединение
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((SERVER_IP, PORT))
    except Exception as e:
        page.add(ft.Text(f"Ошибка: Сервер в Termux не запущен! ({e})", color="red"))

    # Поток для приема сообщений от сервера
    def listen_server():
        while True:
            try:
                data = s.recv(1024)
                if data:
                    chat_display.controls.append(
                        ft.Container(
                            content=ft.Text(data.decode(), size=16),
                            bgcolor="#1D2733", padding=12, border_radius=15
                        )
                    )
                    page.update()
            except:
                break

    threading.Thread(target=listen_server, daemon=True).start()

    msg_input = ft.TextField(hint_text="Написать сообщение...", expand=True, border_radius=25)

    def send_msg(e):
        if msg_input.value:
            try:
                s.send(msg_input.value.encode())
                # Добавляем свое сообщение (справа)
                chat_display.controls.append(
                    ft.Row([
                        ft.Container(
                            content=ft.Text(msg_input.value, size=16),
                            bgcolor="#2B5278", padding=12, border_radius=15
                        )
                    ], alignment=ft.MainAxisAlignment.END)
                )
                msg_input.value = ""
                page.update()
            except:
                page.snack_bar = ft.SnackBar(ft.Text("Нет связи с сервером!"))
                page.snack_bar.open = True
                page.update()

    page.add(
        ft.Text("FAZA P2P", size=24, weight="bold", color="amber"),
        ft.Divider(color="#24303F"),
        chat_display,
        ft.Row([msg_input, ft.FloatingActionButton(icon=ft.icons.SEND, on_click=send_msg)])
    )

ft.app(target=main)
