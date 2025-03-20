import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "TOKEN"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

faq_dict = {
    "как получить студенческий": "Студенческий билет выдается в деканате вашего факультета. Для этого обычно нужны документы, подтверждающие личность (паспорт), фотография и справка о зачислении.",
    "где смотреть расписание": "Расписание занятий доступно на официальном сайте вашего вуза или в личном кабинете студента. Часто вузы также размещают расписание в своих телеграм-каналах или мобильных приложениях.",
    "как найти деканат": "Деканат обычно находится в главном корпусе факультета. Уточнить точную аудиторию можно на сайте факультета или у старосты группы.",
    "как получить зачетку": "Зачётная книжка выдаётся либо вместе со студенческим билетом, либо в деканате, в зависимости от внутреннего регламента вуза.",
    "как получить справку о месте учебы": "Справку об обучении можно взять в деканате или в отделе кадров студентов (студенческом офисе). Уточняйте часы приёма на сайте.",
    "где купить учебники": "Иногда учебники можно получить в библиотеке вуза. Также их можно купить в книжном магазине рядом с университетом или заказать онлайн.",
}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "Привет, первокурсник!\n"
        "Я бот, который поможет тебе с основными вопросами по университету.\n\n"
        "Напиши ключевое слово или вопрос. Например:\n"
        "- как получить студенческий\n"
        "- где смотреть расписание\n\n"
        "Чтобы узнать возможные команды, набери /help"
    )
    await message.answer(welcome_text)

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    topics = "\n- " + "\n- ".join(faq_dict.keys())
    help_text = (
        "Доступные FAQ-запросы:\n"
        f"{topics}\n\n"
    )
    await message.answer(help_text)

@dp.message()
async def faq_reply(message: types.Message):
    user_text = message.text.lower().strip()
    
    found_answer = None
    for question_key, answer_value in faq_dict.items():
        if question_key in user_text:
            found_answer = answer_value
            break
    
    if found_answer:
        await message.answer(found_answer)
    else:
        await message.answer(
            "У меня нет ответа на этот вопрос. "
            "Используйте /help для списка доступных тем."
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


