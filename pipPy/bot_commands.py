from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help')

def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')

# def help_command(update: Update, context: CallbackContext):
#     update.message.reply_text(f'/hi\n/time\n/help')