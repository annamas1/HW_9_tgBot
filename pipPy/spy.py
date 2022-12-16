from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder, ContextTypes


async def log(update: Update, context: ApplicationBuilder):
    file = open('file1.csv', 'a+')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()