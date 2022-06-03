from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5400201806:AAHsMHlC5ctvmhivc8RK2hcwmVsSRYrpoYY").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
















#import emoji

#print(emoji.emojize('Python is :thumbs_up:'))










#from progress.bar import Bar
#import time

#bar = Bar('Processing', max=20)
#for i in range(20):
#    time.sleep(1)
#    # Do some work
#    bar.next()
#bar.finish()