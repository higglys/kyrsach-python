
import asyncio
import logging
import os

from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from dotenv import load_dotenv




BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / "token.env")
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

dp = Dispatcher()




LIBRARY = {
    "Учебники": {
        "description": (
            "Учебники по Python\n\n"
            "Выбирай ресурс по своему уровню. "
            "Для начала рекомендую официальное руководство "
            "и интерактивные уроки."
        ),
        "items": [
            (
                "Официальный учебник Python",
                "Основы языка, циклы, функции и структуры данных.",
                "https://docs.python.org/3/tutorial/",
            ),
            (
                "Automate the Boring Stuff",
                "Автоматизация повседневных задач.",
                "https://automatetheboringstuff.com/",
            ),
            (
                "Think Python",
                "Программное мышление и решение задач.",
                "https://greenteapress.com/wp/think-python-3rd-edition/",
            ),
            (
                "Python for Everybody",
                "Python, работа с данными, файлами и вебом.",
                "https://www.py4e.com/book",
            ),
            (
                "LearnPython.org",
                "Интерактивные уроки и упражнения.",
                "https://www.learnpython.org/",
            ),
            (
                "Google Python Class",
                "Уроки и практические упражнения.",
                "https://developers.google.com/edu/python",
            ),
            (
                "Dive Into Python 3",
                "Более глубокое изучение Python 3.",
                "https://diveintopython3.net/",
            ),
            (
                "A Byte of Python",
                "Введение в Python с примерами.",
                "https://python.swaroopch.com/",
            ),
            (
                "Real Python — основы",
                "Статьи и практические руководства.",
                "https://realpython.com/tutorials/basics/",
            ),
            (
                "Learn Python the Hard Way",
                "Обучение через последовательные упражнения.",
                "https://learnpythonthehardway.org/",
            ),
        ],
    },

    "Справочники": {
        "description": (
            "Справочники Python\n\n"
            "Используй их, чтобы уточнить синтаксис, "
            "найти функцию или разобраться с модулем."
        ),
        "items": [
            (
                "Python Standard Library",
                "Справочник по стандартным модулям Python.",
                "https://docs.python.org/3/library/",
            ),
            (
                "Встроенные функции Python",
                "Описание print(), len(), range() и других функций.",
                "https://docs.python.org/3/library/functions.html",
            ),
            (
                "Справочник по синтаксису",
                "Правила языка Python.",
                "https://docs.python.org/3/reference/",
            ),
            (
                "Встроенные типы данных",
                "Строки, списки, словари и множества.",
                "https://docs.python.org/3/library/stdtypes.html",
            ),
            (
                "Работа с файлами — pathlib",
                "Пути, файлы и папки.",
                "https://docs.python.org/3/library/pathlib.html",
            ),
            (
                "Справочник asyncio",
                "Асинхронное программирование.",
                "https://docs.python.org/3/library/asyncio.html",
            ),
            (
                "Справочник unittest",
                "Инструменты автоматического тестирования.",
                "https://docs.python.org/3/library/unittest.html",
            ),
            (
                "Регулярные выражения — re",
                "Поиск текста по шаблонам.",
                "https://docs.python.org/3/library/re.html",
            ),
            (
                "Справочник pandas",
                "Таблицы и анализ данных.",
                "https://pandas.pydata.org/docs/reference/",
            ),
            (
                "Python Packaging User Guide",
                "Установка и распространение пакетов.",
                "https://packaging.python.org/",
            ),
        ],
    },

    "Методички": {
        "description": (
            "Практические методички\n\n"
            "Руководства по разработке программ, "
            "тестированию и созданию Telegram-ботов."
        ),
        "items": [
            (
                "Функции и модули",
                "Организация кода и разделение программы на части.",
                "https://docs.python.org/3/tutorial/modules.html",
            ),
            (
                "Обработка ошибок",
                "Использование try, except и finally.",
                "https://docs.python.org/3/tutorial/errors.html",
            ),
            (
                "Классы и объекты",
                "Основы объектно-ориентированного программирования.",
                "https://docs.python.org/3/tutorial/classes.html",
            ),
            (
                "Виртуальные окружения",
                "Изоляция зависимостей проекта.",
                "https://docs.python.org/3/library/venv.html",
            ),
            (
                "Тестирование — pytest",
                "Проверка функций и поиск ошибок.",
                "https://docs.pytest.org/en/stable/getting-started.html",
            ),
            (
                "Создание Telegram-ботов — aiogram",
                "Обработчики, команды и клавиатуры.",
                "https://docs.aiogram.dev/en/latest/",
            ),
            (
                "HTTP-запросы — Requests",
                "Взаимодействие с веб-сервисами и API.",
                "https://requests.readthedocs.io/en/latest/user/quickstart/",
            ),
            (
                "Базы данных SQLite",
                "Хранение данных и выполнение SQL-запросов.",
                "https://docs.python.org/3/library/sqlite3.html",
            ),
            (
                "Система контроля версий Git",
                "История изменений и управление версиями.",
                "https://git-scm.com/book/en/v2",
            ),
            (
                "Журналирование — logging",
                "Запись событий и ошибок программы.",
                "https://docs.python.org/3/howto/logging.html",
            ),
        ],
    },
}




def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Библиотека")],
        ],
        resize_keyboard=True,
    )


def library_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Учебники")],
            [KeyboardButton(text="Справочники")],
            [KeyboardButton(text="Методички")],
            [KeyboardButton(text="Главное меню")],
        ],
        resize_keyboard=True,
    )


def resource_keyboard(category: str) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text=title,
                url=url,
            )
        ]
        for title, _description, url
        in LIBRARY[category]["items"]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)




@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! Добро пожаловать в библиотеку "
        "учебных материалов по Python.\n\n"
        "Здесь собраны учебники, справочники "
        "и практические методички.\n\n"
        "Нажми «Библиотека», чтобы начать.",
        reply_markup=main_keyboard(),
    )


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Доступные команды:\n\n"
        "/start — приветствие\n"
        "/library — открыть библиотеку\n"
        "/help — список команд\n"
        "/cancel — главное меню",
        reply_markup=main_keyboard(),
    )


@dp.message(Command("library"))
@dp.message(F.text == "Библиотека")
async def library_handler(message: Message):
    await message.answer(
        "Выбери категорию материалов:",
        reply_markup=library_keyboard(),
    )


@dp.message(Command("cancel"))
@dp.message(F.text == "Главное меню")
async def cancel_handler(message: Message):
    await message.answer(
        "Ты вернулся в главное меню.",
        reply_markup=main_keyboard(),
    )




async def show_category(message: Message, category: str):
    data = LIBRARY[category]

    lines = [
        data["description"],
        "",
    ]

    for index, (title, description, _url) in enumerate(
        data["items"],
        start=1,
    ):
        lines.append(f"{index}. {title}")
        lines.append(description)
        lines.append("")

    lines.append("Нажми на кнопку, чтобы открыть ресурс.")

    await message.answer(
        "\n".join(lines),
        reply_markup=resource_keyboard(category),
    )


@dp.message(F.text == "Учебники")
async def textbooks_handler(message: Message):
    await show_category(message, "Учебники")


@dp.message(F.text == "Справочники")
async def reference_books_handler(message: Message):
    await show_category(message, "Справочники")


@dp.message(F.text == "Методички")
async def guides_handler(message: Message):
    await show_category(message, "Методички")




@dp.message()
async def unknown_handler(message: Message):
    await message.answer(
        "Не совсем понял запрос.\n\n"
        "Нажми «Библиотека», чтобы открыть материалы, "
        "или отправь /help.",
        reply_markup=main_keyboard(),
    )




async def main():
    if not TOKEN:
        raise ValueError(
            "Не найден BOT_TOKEN. Проверь файл token.env."
        )

    bot = Bot(token=TOKEN)

    try:
        logging.info("Бот запускается...")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен.")
