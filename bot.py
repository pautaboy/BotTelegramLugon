from telegram.ext import Updater, CommandHandler


def star(update, context):

    update.message.reply_text('Hola Cirwelos!')


if __name__ == '__main__':

   updater = Updater(token='5425494826:AAH_sKAJpVx-yUzzGcQrL1v2YYxAqt--2no', use_context=True)

   dp = updater.dispatcher

   dp.add_handler(CommandHandler('star', star))

   updater.start_polling()
   updater.idle()
