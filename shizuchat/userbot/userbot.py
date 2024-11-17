import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
import config


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="BADAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING),
            no_updates=False,
            plugins=dict(root="shizuchat.plugin"),
        )
        

    async def start(self):
        print(f"Starting Assistants...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("PBX_CHAT")
                await self.one.join_chat("HEROKUBIN_01")
                await self.one.join_chat("ll_BAD_MUNDA_WORLD_ll ")
                await self.one.join_chat("ll_BAD_ABOUT_ll")

            except:
                pass

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
     
            print(f"Id-Chatbot Started as {self.one.me.first_name}")

        

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Id-Chatbot...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass