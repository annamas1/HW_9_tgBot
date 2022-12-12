from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
from bot_commands import *

updater = Updater('5786268103:AAFRBnAdthWoSYvIdMATvgwkQOyB9xNUtug')

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
# aupdater.dispatcher.add_handler(CommandHandler("sum", sum_command))

print('server start')
updater.start_polling()
updater.idle()





#  Библиотека для аналитика
# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()


