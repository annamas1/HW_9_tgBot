from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder, ContextTypes



def log(update: Update, context: CallbackContext):
    file = open('logirovanie.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()



