from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ContextTypes , ApplicationBuilder
from bot_commands import *
from spy import *

update = ApplicationBuilder().token('5786268103:AAFRBnAdthWoSYvIdMATvgwkQOyB9xNUtug').build()

update.add_handler(CommandHandler("hi", hi_command))
update.add_handler(CommandHandler("time", time_command))
update.add_handler(CommandHandler("help", help_command))
update.add_handler(CommandHandler("sum", sum_command))
update.add_handler(CommandHandler("mult", mult_command))

print('server start')
# update.start_polling()   # не подходит
update.run_polling()
# update.idle()     # не подходит





#  Библиотека для аналитика
# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()


