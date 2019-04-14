from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import telegram
import requests
import re 
import os






token = os.environ['API_TOKEN']

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def help_(update, context):
    h = '''
        hello {} 
        commands list:
        /bop to generate new image
        /help to show this text
    '''.format(update.message.from_user['first_name'])
    context.bot.send_chat_action(update.message.chat_id, action=telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=update.message.chat_id, text=h)



def get_url():
    contents = requests.get('https://random.dog/woof.json').json() 
    url = contents['url']
    return url 



def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id 
    context.bot.send_chat_action(chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id=chat_id, photo=url)

    

def main():
   updater = Updater(token, use_context=True)
   db = updater.dispatcher
   db.add_error_handler(MessageHandler(Filters.command, unknown))
   db.add_handler(CommandHandler('bop', bop))
   db.add_handler(CommandHandler('help', help_))
   updater.start_polling()
   updater.idle()


if __name__=='__main__':
    main()
    
