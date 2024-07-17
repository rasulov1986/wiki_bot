from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command
from wiki import wiki_bot

wiki_router: Router = Router()

@wiki_router.message()
async def wiki_handler(msg:Message):
    await msg.answer(wiki_bot(msg.text))