from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

MINI_APP_URL = "https://fatisedghy.github.io/Vpn-miniapp/"

async def start(update, context):
    keyboard = [[
        InlineKeyboardButton("🚀 Open App", web_app=WebAppInfo(url=MINI_APP_URL))
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome!", reply_markup=reply_markup)

app = Application.builder().token("8964587978:AAFt8SxXSWZSAdxC5HErLPoxM7agd9ujB4E").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
