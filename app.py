from env import api_key

from telegram.ext import *
#import Responses as R

ooo = True


def cmd_start(update, context):
    return "hello world "+str(update, context)

def cmd_help(update, context):
    return "helpful message :) "+str(update) + " :::" + str(context)
    

def error(update, context):
    err = f"Update {update} caused error {context.error}"
    print(err)
    return err

def incoming(source, *args, **kwargs):
    text = str(source.message.text)
    print(" ::: incoming ::: ", text, args, kwargs)
    print(source)
    print(":::::::::::::::::::::::::::::::::::::\n\n")
    respond = ""
    if ooo:
        respond = "Sorry we are not operating on the weekends. Please get back to us on sunday, Thanks and have a good one!"
    respond = "ok ok"
    source.message.reply_text(respond)
    


if __name__ == "__main__":
    print(" ::: Welcome To Telegram Integration :::" , api_key)
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", cmd_start))
    dp.add_handler(CommandHandler("help", cmd_help))
    dp.add_handler(MessageHandler(Filters.text, incoming))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()
    
    print("#######################FIN######")
 
    