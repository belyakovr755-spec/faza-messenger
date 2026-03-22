import flet as ft
from telethon import TelegramClient, events

# Твои данные (уже вписал их за тебя)
API_ID = 20407135 
API_HASH = 'b18441a1ff607e10a989891a5462e627'
BOT_TOKEN = '8603186150:AAFEwqlQHXPXOdCEbv-g0ocRpkMU8G0znhs'

async def main(page: ft.Page):
    page.title = "Faza Messenger"
    page.theme_mode = ft.ThemeMode.DARK
    chat = ft.ListView(expand=True, spacing=10)
    page.add(ft.Text("Faza Messenger Online", size=25), chat)

ft.app(target=main)
               
