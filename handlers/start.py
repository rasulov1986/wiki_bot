from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command

start_router: Router = Router()

@start_router.message(Command('start'))
async def start_handler(msg:Message):
    await msg.answer("Salom xush kelibsiz!")

