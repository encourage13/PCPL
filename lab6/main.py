from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from datetime import datetime, timedelta
import asyncio

TOKEN = "7293310229:AAFneTcGiMQLCdSU9sY0J7P9eGQuNMEgwCo"

alarms = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Установить будильник", callback_data="set_alarm")],
        [InlineKeyboardButton("Удалить будильник", callback_data="remove_alarm")],
        [InlineKeyboardButton("Список будильников", callback_data="list_alarms")],
        [InlineKeyboardButton("Меню", callback_data="menu")]  # Кнопка меню
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Я бот-будильник. Выберите действие:", reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "set_alarm":
        await query.message.edit_text("Введите время будильника в формате HH:MM.")
    elif query.data == "remove_alarm":
        await remove_alarm(update, context)
    elif query.data == "list_alarms":
        await list_alarms(update, context)
    elif query.data == "menu":
        await menu(update, context)  # Вызов меню


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Установить будильник", callback_data="set_alarm")],
        [InlineKeyboardButton("Удалить будильник", callback_data="remove_alarm")],
        [InlineKeyboardButton("Список будильников", callback_data="list_alarms")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)


# Удаление будильников
async def remove_alarm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    if chat_id in alarms and len(alarms[chat_id]) > 0:
        alarm = alarms[chat_id].pop(0)
        await update.callback_query.message.reply_text(f"Будильник на {alarm['time']} удалён.")
    else:
        await update.callback_query.message.reply_text("У вас нет установленного будильника.")


# Просмотр списка будильников
async def list_alarms(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    if chat_id in alarms and len(alarms[chat_id]) > 0:
        alarm_times = "\n".join([f"Будильник на {alarm['time']}" for alarm in alarms[chat_id]])
        await update.callback_query.message.reply_text(f"Ваши будильники:\n{alarm_times}")
    else:
        await update.callback_query.message.reply_text("У вас нет установленного будильника.")


# Обработка текста для установки будильника
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    text = update.message.text

    try:
        # Парсинг времени
        alarm_time = datetime.strptime(text, '%H:%M').time()
        now = datetime.now()

        # Вычисление времени до будильника
        alarm_datetime = datetime.combine(now.date(), alarm_time)
        if alarm_datetime <= now:
            alarm_datetime += timedelta(days=1)

        time_to_wait = (alarm_datetime - now).total_seconds()
        alarm_str = alarm_datetime.strftime('%H:%M')

        if chat_id not in alarms:
            alarms[chat_id] = []

        alarm_task = asyncio.create_task(send_alarm(context, chat_id, time_to_wait, alarm_str))
        alarms[chat_id].append({"time": alarm_str, "task": alarm_task})

        await update.message.reply_text(f"Будильник установлен на {alarm_str}.")

    except ValueError:
        await update.message.reply_text("Ошибка: введите время в формате HH:MM.")


async def send_alarm(context: ContextTypes.DEFAULT_TYPE, chat_id: int, delay: float, alarm_time: str) -> None:
    await asyncio.sleep(delay)
    await context.bot.send_message(chat_id=chat_id, text=f"⏰ Время вставать! Это ваш будильник на {alarm_time}.")


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("Бот запущен.")
    application.run_polling()


if __name__ == "__main__":
    main()
